This is a web-based application to track networking relationships and document conversations. Built in python using the Flask framework.


create a virtual environment:
$ python -m venv virt

to activate virtual environment:
$ source virt/Scripts/activate

to see what is installed:
$ pip freeze

to intsall flask:
$ pip install flask

create first python file:
$ touch hello.py

to deactiveate virtural environment:
$ deactiveate



OLD ----------------------------------------------------------------------------------------------------------------->
In Bash window:

create and/or activate virtual environment:
$ python -m venv virt
$ source virt/Scripts/activate

to deactiveate virtural environment:
$ deactiveate

to intsall flask:
$ pip install flask

to see what is installed:
$ pip freeze

to create first python file:
$ touch hello.py

to run flask app in development mode:
'FLASK_ENV' is deprecated and will not be used in Flask 2.3. Use 'FLASK_DEBUG' instead.
$ flask --app hello --debug run

----------------- GitHub ----------------- 
" Create an ssh key for windows users "

$ cd ~/ 
$ pwd
$ mkdir .ssh
$ cd .ssh
$ clear
$ ssh-keygen.exe
(hit enter)
(hit enter)
(hit enter)
$ ls
$ cat id_rsa.pub
( copy and past key to GitHub account)

# Before pushing project to GitHub we need to exclude the virtual environment
$ touch .gitignore

# Initalizing Git for version control (make sure virtual environment is active)
https://codemy.com/git/
$ git config --global user.name "Llewellyn Thomas"
$ git config --global user.email "thomas.llewy@gmail.com"
$ git config --global push.default matching
$ git config --global alias.co checkout
$ git init

# to "turn it on"
$ git add .
$ git commit -am 'inital commit'

# set up repository on GitHub
…or push an existing repository from the command line
$ git remote add origin https://github.com/LlewyThomas/FlaskFridays.git
$ git branch -M main
$ git push -u origin main

# Update changes and push to GitHub
$ git add .
$ git commit -am 'Update Description'
$ git push

----------------- Bootstrap -----------------
https://getbootstrap.com/docs/5.3/getting-started/introduction/#quick-start

instert 'quick start' code into base.html file
create a div with class container and instert {% block content %} ect.  into the html body

for a var bar it is recommended to create a navbar.html file and use a {% inculde 'navbar.hmtl' %} in base.html


----------------- What The Forms -----------------
https://flask-wtf.readthedocs.io/
$ pip install flask-wtf
make sure a bunch of methods is imported into the python file
...
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

Creat a secret key (CSRF Token)
app.config['SECRET_KEY'] = ""

----------------- Flask pop up messages -----------------
from flask import flash
flash messages do not have to be passed to the render_template() method

----------------- SQLAlchemy -----------------
In terminal:
$ pip install flask-sqlalchemy
In Flask app file:
...
from flask_sqlalchemy import SQLAlchemy
...

to add database to app:
...
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
...
" URI - Uniform Resourse Indicator - leads to where database is"
- starting with SQLlite

# Create Model for Database
...

To create/ initialize the data base:
Python Interpter in Git Bash terminal:
$ winpty py
>>> from hello import app, db
>>> app.app_context().push()
>>> db.create_all()
>>> exit()

Then create a form class in the python app
Then create route and a function
...

----------------- MySQL-----------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'

"install all three connectors, only one needs to work, for some reason some don't work"
pip install mysql-connector
pip install mysql-connector-python
pip install mysql-connector-python-rf

create database with python commands - 'create_db.py'
...
# Python Code to Initialize MySQL DB
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

my_cursor = mydb.cursor() 

# commented out as to no not whipe data from 'users' db if it already exists
# my_cursor.execute("CREATE DATABASE users")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
...


pip install pymysql
pip install cryptography

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql...

>>> from hello import app,db
>>> with app.app_context():
>>>     db.create_all()
