# Questioner 

[![Build Status](https://travis-ci.org/Mupa1/Questioner.svg?branch=develop)](https://travis-ci.org/Mupa1/Questioner) [![Coverage Status](https://coveralls.io/repos/github/Mupa1/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/Mupa1/Questioner?branch=develop)   

## Framework/Tech Used
python 3.6.7 and Flask   
   
## Overview
Crowd source questions for a meetup.__Questioner__ helps the meetup organizer prioritize questions to be answered. Other uses can vote on asked questions and they bubble to the top or bottom of the log.

## Installation and Deployment
1. Git clone https://github.com/Mupa1/Questioner.git and cd into the folder
2. Create a virtual environment and activate it   
   > python3 venv env   
   > source .env   
3. Install all dependancies   
    > pip install -r requirements.txt
4. Run the application
    > source .env   
    > flask run   
    
## Test the implementation of the end points
__Run tests__   
using pytest or py.test on root folder of Questioner folder   
Set FLASK_CONFIG to testing on your .env file before running tests.   

    source .env   
    pytest 

__Test the Coverage__   

    pytest --cov=app  
       
## Test the application enpoints
Test endpoints using postman
> Run the application, and with the server started, test against the endpoints provided below in postman
>   ```http://localhost:5000/api/v1/<endpoint>```

#### Endpoint to test

Method | Endpoint | Description
------------ | ------------- | -----------
POST | /api/v1/meetups | Create a meetup record
GET | /api/v1/meetups/upcoming | Fetch all upcoming meetup records
GET | /api/v1/meetups/<meetup_id> | Fetch a specific meetup record
PATCH | /api/v1/questions/<question_id>/upvote | Upvote (increase vote by 1) a specific question
PATCH | /api/v1/qestions/<question_id>/downvote | Downvote (decrease vote by 1) a specific question
POST | /api/v1/meetups/<meetup_id>/rsvp| Respond to meetups rsvp
GET | /api/v1/meetups/<meetup_id>| Fetch a specific meetup record




