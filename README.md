# Microservices with Docker, Flask, and React
[![Build Status](https://travis-ci.org/yadra/testdriven-app.svg?branch=main)](https://travis-ci.org/yadra/testdriven-app)


commands:

 docker-compose -f docker-compose-dev.yml up -d --build 
 
 docker-compose -f docker-compose-dev.yml run users python manage.py recreate-db
  
 docker-compose -f docker-compose-dev.yml run users python manage.py seed-db
 
 docker-compose -f docker-compose-dev.yml run users python manage.py db init
 
 docker-compose -f docker-compose-dev.yml run users python manage.py db migrate
 
 docker-compose -f docker-compose-dev.yml run users python manage.py db upgrade