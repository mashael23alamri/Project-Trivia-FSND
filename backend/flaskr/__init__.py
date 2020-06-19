import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from flask_migrate import Migrate
from models import setup_db, Question, Category


QUESTIONS_PER_PAGE = 10

#for paginating questions#
#the auxiliary way to take question number and request#
#references:https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination#
def paginate_questions(request, selection):
    #Get the page number or one page if it is not included#
    page = request.args.get('page', 1, type=int)
    #Determine the start and end of the questions that are viewed using QUESTIONS_PER_PAGE#
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    #formatting of questions#
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]
    #the questions I want to return to the user#
    return current_questions


def create_app(test_config=None):
  #create and configure the app
  app = Flask(__name__)
  setup_db(app)
  


  #@TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  #now set up CORS, Allow '*' for origins#
  #references:https://flask-cors.readthedocs.io/en/latest/#
  CORS(app, resource={'/': {'origins': '*'}})

  #@TODO: Use the after_request decorator to set Access-Control-Allow
  #it works when a request is received that triggers this#
  @app.after_request
  def after_request(res):
     #access control#
     res.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,true')
     #access control methods#
     res.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
     return res


  #@TODO:create an endpoint to handle GET requests for all available categories.
  #handle GET requests for all categories#
  @app.route('/categories') #name the endpoint must be same name url in QuizView.js#
  def get_categories():
      #get all categories and add list#
      categories = Category.query.all()
      categories_list = {}
      for category in categories:
          categories_list[category.id] = category.type
      #abort 404 when it does not find categories#
      if (len(categories_list) == 0):
          abort(404)

      #return data#
      return jsonify({
         'success': True,
         'categories': categories_list
      })

      '''
      @TODO:
      Create an endpoint to handle GET requests for questions,
      including pagination (every 10 questions).
      This endpoint should return a list of questions,
      number of total questions, current category, categories.

      TEST: At this point, when you start the application
      you should see questions and categories generated,
      ten questions per page and pagination at the bottom of the screen for three pages.
      Clicking on the page numbers should update the questions.
      '''
  #handle GET requests for all questions..
  @app.route('/questions') #name the endpoint must be same name url in QuestionView.js#
  def get_questions():
      #get all questions and pagination#
      selection = Question.query.all()
      total_questions = len(selection)
      paginated = paginate_questions(request, selection)
      #get all categories and add list#
      categories = Category.query.all()
      categories_list = {}
      for category in categories:
          categories_list[category.id] = category.type
      #abort 404 when it does not find questions#
      if (len(categories_list) == 0):
          abort(404)
      #return data#
      return jsonify({
          'success': True,
          'questions': paginated,
          'total_questions': total_questions,
          'categories': categories_list
      })

      '''
      @TODO:
      Create an endpoint to DELETE question using a question ID.

      TEST: When you click the trash icon next to a question, the question will be removed.
      This removal will persist in the database and when you refresh the page.
      '''

  #delete question using a question ID#
  @app.route('/questions/<int:id>', methods=['DELETE']) #name the endpoint must be same name url in QuestionView.js#
  def delete_question(id):
    #Try#
      try:
           #get the question by id#
           #references:https://docs-sqlalchemy.readthedocs.io/ko/latest/orm/query.html#sqlalchemy.orm.query.Query.one_or_none#
           question = Question.query.filter_by(id=id).one_or_none()
           #abort 404 when it does not find questions#
           if question is None:
              abort(404)
           #delete question#
           question.delete()
           #return#
           return jsonify({
              'success': True,
              'deleted': id
             })

    #except:
      except:
             #abort When an error occurs when the question is deleted#
              abort(422)

      '''
      @TODO:
      Create an endpoint to POST a new question,
      which will require the question and answer text,
      category, and difficulty score.

      TEST: When you submit a question on the "Add" tab,
      the form will clear and the question will appear at the end of the last page
      of the questions list in the "List" tab.
      '''

      '''
      @TODO:
      Create a POST endpoint to get questions based on a search term.
      It should return any questions for whom the search term
      is a substring of the question.

      TEST: Search by any phrase. The questions list will update to include
      only question that include that string within their question.
      Try using the word "title" to start.
      '''

  #post a new questions#
  @app.route('/questions', methods=['POST']) #name the endpoint must be same name url in QuestionView.js#
  def post_question():
        #load a request body#
        body = request.get_json()
        #if search term is found#
        if(body.get('searchTerm')):
           search_term = body.get('searchTerm')

           #get all questions that has the search term substring#
           #use when like search i=insensitive to case#
           selection = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()

           # 404 if no results found#
           if (len(selection) == 0):
                abort(404)

           #paginated#
           paginated = paginate_questions(request, selection)

           #return#
           return jsonify({
              'success': True,
              'questions': paginated,
              'total_questions': len(Question.query.all())
            })
        #if no search term, create new question#

        else:
            #load data from body#
            new_question = body.get('question')
            new_answer = body.get('answer')
            new_difficulty = body.get('difficulty')
            new_category = body.get('category')

            #make sure all fields have data#
            if ((new_question is None) or (new_answer is None)
                    or (new_difficulty is None) or (new_category is None)):
                      abort(422)

        try:
             #create and insert new question#
             question = Question(question=new_question, answer=new_answer,
             difficulty=new_difficulty, category=new_category )
             #insert in database#
             question.insert()

             #get all questions and paginate#
             selection = Question.query.order_by(Question.id).all()
             paginated = paginate_questions(request, selection)

             #return#
             return jsonify({
                'success': True,
                'created': question.id,
                'question_created': question.question,
                'questions': paginated,
                'total_questions': len(Question.query.all())
             })

        except:
               #abortion is not possible if there is an exception#
                abort(422)



  #get to questions based on category#
  @app.route('/categories/<int:id>/questions')#name the endpoint must be same name url in QuestionView.js#
  def  get_questions_by_category(id):
       #get category by id #
       category = Category.query.filter_by(id=id).one_or_none()

       #abort 400 when category is not found#
       if (category is None):
            abort(400)

       #get the matching questions#
       selection = Question.query.filter_by(category=category.id).all()

       #paginated#
       paginated = paginate_questions(request, selection)

       #return#
       return jsonify({
            'success': True,
            'questions': paginated,
            'total_questions': len(Question.query.all()),
            'current_category': category.type
          })

  #create a POST endpoint to get questions to play the quiz#
  @app.route('/quizzes', methods=['POST']) #name the endpoint must be same name url in QuizView.js#
  def get_random():
      #load a request body#
      body = request.get_json()

      #get the previous questions
      previous_questions = body.get('previous_questions')

      #get all category#
      category = body.get('quiz_category')

      #abort 400 if previous_questions or category is not found#
      if ((category is None) or (previous_questions is None)):
            abort(400)

      #load questions all questions if ALL is selected#
      if(category['id'] == 0):
          questions = Question.query.all()
      else:
      #load questions for given category#
          questions = Question.query.filter_by(category=category['id']).all()
      #total number of questions#
      total = len(questions)
      #choose a random question#
      def get_random_question():
          #references:https://docs.python.org/3/library/random.html#random.randrange
          return questions[random.randrange(0, len(questions), 1)]

      #checks if the question has already been used#
      def check_if_used(question):
          used = False
          for q in previous_questions:
              if(q == question.id):
                  used = True

          return used

      #get random question#
      question = get_random_question()

      #check if it is used, perform until an unused question is found#
      while (check_if_used(question)):
          question = get_random_question()

          #if all questions have been tried, come back without a question#
          #necessary if the category contains less than 5 questions#
          if(len(previous_questions) == total):
             #return#
             return jsonify({
                 'success': True
              })

      #return#
      return jsonify({
            'success': True,
            'question': question.format()
         })


  #create error handlers for all expected errors#
  #status code 400#
  @app.errorhandler(400)
  def  bad_request(error):
       return jsonify({
           'success': False,
           'error': 400,
           'message': 'Bad Request'
      }),400

  #status code 404#
  @app.errorhandler(404)
  def  not_found(error):
      return jsonify({
          'success': False,
          'error': 404,
          'message': 'Resource Not Found'
      }),404

  #status code 422#
  @app.errorhandler(422)
  def  unprocessable(error):
      return jsonify({
          'success': False,
          'error': 422,
          'message': 'Unprocessable'
     }),422


  return app
