# Trivia API Project

This project is a nice game ^ـ^ , in which players (users) can test their knowledge in answering trivial questions as they show them a set of categories and the degree of difficulty for each question.

## Project task

A nice challenge is to create an API and a set of tests to ensure that the game functions properly, including:
 1- Display questions and the ability to show and hide them.
 2- Display questions by category and classification of degree of difficulty.
 3- The ability to delete questions.
 4- Adding questions that must include the question and the answer, and determining the category and degree of difficulty.
 5- The ability to search for questions in the search box.
 6- Play, the ability to play in choosing random questions to play all the questions or to select a specific category.
 7- finally,Results are paginated in groups of 10.

## To start

### Installing Dependencies
Software developers using this project should install (Python3, pip3, node, and npm).

### Frontend Dependencies
This project uses NPM to manage program dependencies. NPM relies on the package.json file located in the front-end directory of this repository. After cloning open Terminal and install:

Going to the / frontend directory and running:

```bash
  npm install
```

Then:
```
"dependencies": {
  "corsproxy": "^1.5.0",
  "jquery": "^3.5.1",
  "react": "^16.13.1",
  "react-dom": "^16.13.1",
  "react-router-dom": "^5.2.0",
  "react-scripts": "^3.0.1"
```


### Backend Dependencies
Once the virtual environment is set up and running, install the dependencies by going to the / backend directory and running:

 ```bash
   pip3 install -r requirements.txt
 ```
## Running the Frontend
--------------------------------------------------------------------------------
 The frontend app was built using create-react-app. In order to run the app in development mode use npm start.

 ```bash
   npm start
 ```
  The http://localhost:3000 will run in the browser.

## Running the Server
--------------------------------------------------------------------------------
From within the backend directory first make sure you are working using your created virtual environment.
To run the server must be you write three  :

```bash
 export FLASK_APP=flaskr
 export FLASK_ENV=development
 flask run
```

## Testing
--------------------------------------------------------------------------------
In order to perform the test process, it is necessary to create new data for the test:

```bash
  dropdb trivia_test
  createdb trivia_test
  psql trivia_test < trivia.psql
  python test_flaskr.py
```
The first line to drop DataBase has the same name, if any
The second line is to create a DataBase trivia_test
The third line is to link the data in the project folder (trivia.psql)
The last line runs the test test_flaskr.py


## Getting Started
--------------------------------------------------------------------------------
Base URL: Currently this application is only hosted locally, the backend is hosted at http://127.0.0.1:5000/
Authentication: This version does not require authentication or API keys.
--------------------------------------------------------------------------------

### Error Handling
Errors are returned as JSON in the following format:

```bash
{   
    "success": False,
    "error": 400,
    "message": "Bad Request"
}
```
#### The API will return three types of errors:

400 – Bad Request
404 – Resource Not Found
422 – Unprocessable

## Endpoints
--------------------------------------------------------------------------------
### GET /questions
General:

Returns a list questions.
Results are paginated in groups of 10.
Also returns list of categories and total number of questions.
Example: curl http://127.0.0.1:5000/questions?page=2

```bash
{
"categories": {
"1": "Science",
"2": "Art",
"3": "Geography",
"4": "History",
"5": "Entertainment",
"6": "Sports"
},
"questions": [
{
"answer": "Escher",
"category": 2,
"difficulty": 1,
"id": 16,
"question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
},
{
"answer": "Mona Lisa",
"category": 2,
"difficulty": 3,
"id": 17,
"question": "La Giaconda is better known as what?"
},
{
"answer": "One",
"category": 2,
"difficulty": 4,
"id": 18,
"question": "How many paintings did Van Gogh sell in his lifetime?"
},
{
"answer": "Jackson Pollock",
"category": 2,
"difficulty": 2,
"id": 19,
"question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
},
{
"answer": "The Liver",
"category": 1,
"difficulty": 4,
"id": 20,
"question": "What is the heaviest organ in the human body?"
},
{
"answer": "Alexander Fleming",
"category": 1,
"difficulty": 3,
"id": 21,
"question": "Who discovered penicillin?"
},
{
"answer": "Blood",
"category": 1,
"difficulty": 4,
"id": 22,
"question": "Hematology is a branch of medicine involving the study of what?"
},
{
"answer": "Scarab",
"category": 4,
"difficulty": 4,
"id": 23,
"question": "Which dung beetle was worshipped by the ancient Egyptians?"
},
{
"answer": "",
"category": 1,
"difficulty": 1,
"id": 50,
"question": "How are you?"
},
{
"answer": "Hydrogen, Oxygen",
"category": 1,
"difficulty": 1,
"id": 62,
"question": "What are the components of water?"
}
],
"success": true,
"total_questions": 20
}

```
--------------------------------------------------------------------------------
### DELETE /questions/<int:id>
General:

Deletes a question by id using url parameters.
Returns id of deleted question upon success.
Example: curl http://127.0.0.1:5000/questions/9 -X DELETE

```bash
{
"deleted": 9,
"success": true
}
```
--------------------------------------------------------------------------------
### GET /categories
General: Returns a list categories.

Example: curl http://127.0.0.1:5000/categories

```bash
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```
--------------------------------------------------------------------------------
### POST /questions
This endpoint either creates a new question or returns search results.

If no search term is included in request:
General:

Creates a new question using JSON request parameters.
Returns JSON object with newly created question, as well as paginated questions.
Example: curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{ "question":"what is the cause of the current virus outbreak?", "answer": "covid-19", "difficulty": 2, "category": "1" }'


```bash
{
  "created": 63,
  "question_created": "what is the cause of the current virus outbreak?",
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```

#### If search term is included in request:
General:

Searches for questions using search term in JSON request parameters.
Returns JSON object with paginated matching questions.
Example: curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "what"}'

```bash
{
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Hydrogen, Oxygen",
      "category": 1,
      "difficulty": 1,
      "id": 62,
      "question": "What are the components of water?"
    },
    {
      "answer": "covid-19",
      "category": 1,
      "difficulty": 2,
      "id": 63,
      "question": "what is the cause of the current virus outbreak?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```

--------------------------------------------------------------------------------
### GET /categories/<int:id>/questions
General:

Gets questions by category id using url parameters.
Returns JSON object with paginated matching questions.
Example: curl http://127.0.0.1:5000/categories/2/questions

```bash
{
  {
    "current_category": "Art",
    "questions": [
      {
        "answer": "Escher",
        "category": 2,
        "difficulty": 1,
        "id": 16,
        "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
      },
      {
        "answer": "Mona Lisa",
        "category": 2,
        "difficulty": 3,
        "id": 17,
        "question": "La Giaconda is better known as what?"
      },
      {
        "answer": "One",
        "category": 2,
        "difficulty": 4,
        "id": 18,
        "question": "How many paintings did Van Gogh sell in his lifetime?"
      },
      {
        "answer": "Jackson Pollock",
        "category": 2,
        "difficulty": 2,
        "id": 19,
        "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
      }
    ],
    "success": true,
    "total_questions": 19
  }
}
```
--------------------------------------------------------------------------------
### POST /quizzes
General:

Allows users to play the quiz game.
Uses JSON request parameters of category and previous questions.
Returns JSON object with random question not among previous questions.
Example: curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [20, 21], "quiz_category": {"type": "Science", "id": "6"}}'

```bash
{
  "question": {
    "answer": "Uruguay",
    "category": 6,
    "difficulty": 4,
    "id": 11,
    "question": "Which country won the first ever soccer World Cup in 1930?"
  },
  "success": true
}
```
## Finally
--------------------------------------------------------------------------------
All other project files, including the models and frontend, were created by Udacity.
--------------------------------------------------------------------------------

## References
--------------------------------------------------------------------------------
[virtual-environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

[Flask](https://flask-wtf.readthedocs.io/en/stable/)

[Miguelgrinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination)

[Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)

[w3schools](https://www.w3schools.com/python/ref_string_strip.asp)


