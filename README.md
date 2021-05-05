# CourseCatalog

CourseCatalog is API project on Django
This api allows you to view, create, delete, and change courses

##Installation

To work with this API you need install this prodject:

$ git clone https://github.com/Koreandel/CourseCatalog.git

Create virtual enviroment:

$ python3 -m venv

And install the dependencies:

(env)$ pip install -r requirements.txt


Or add courses_api folder to your project and add it po installed apps:

INSTALLED_APPS = [
    'courses_api',
    ....
]

##Tests

This project has Course_Api.postman_collection.json file to add collection to Postman with tests for all requests

Also unittest:

I use requests to create all tests so first of all you need runserver from the root

$./manage.py runserver

And after that

$./manage.py test


P.S.This is my first test, so sory about this strange things))
