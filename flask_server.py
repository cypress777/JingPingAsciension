#!/usr/bin/env python3

from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

from database_utils import DatabaseException, init_database
from database_setup import Base, DatabaseName, UserInfo

from utils import infoLogger, errorLogger, debugLogger, ErrorCodes

DatabaseSession = None

def query_userinfo(username):
   try:
    return DatabaseSession.query(UserInfo).filter_by(name=username).first()
  except:
    raise DatabaseException('during query user\'s info')
 

def has_username(username):
  global DatabaseSessioin
  try:
    userinfo = query_userinfo(username)
    return (userinfo != None)
  except:
    raise

def is_valid_log_in(username, password):
  global DatabaseSessioin

  userinfo = None
  try:
    userinfo = query_userinfo(username)
  except:
    raise

  if userinfo == None or userinfo.password != password:
    return False
  return True

def log_in_user(username):
  return 'log in success'

def is_valid_sign_up(username, password):
  global DatabaseSessioin

  userinfo = None
  try:
    userinfo = query_userinfo(username)
  except:
    raise

  if userinfo != None:
    return False
  return True
 

def sign_up_user(username):
  try:
    new_user = UserInfo(name=username, password=password)
    DatabaseSession.add(new_user)
    DatabaseSession.commit()
  except:
    raise

  return 'sign up success'

@app.route('/', methods=['GET', 'POST'])
@app.route('/en', methods=['GET', 'POST'])
def Welcome():
  return render_template('hello.html')

@app.route('/login', methods=['GET', 'POST'])
def Login():
  error = None
  if request.method == 'POST':
    if is_valid_log_in(request.form['username'], request.form['password']):
      return log_in_user(username)
    else:
      error = 'Invalid log in: Wrong username/password'
  return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def Signup():
  error = None
  if request.method == 'POST':
    if is_valid_sign_up(request.form['username'], request.form['password']):
      return sign_up_user(username)
    else:
      if has_username(username):
        error = 'Invalid sign up: Username has been taken'
      else:
        error = 'Invalid password: password should be letters and numbers'
  return render_template('signup.html')

if __name__ == '__main__':
  try:
    DatabaseSession = init_database(DatabaseName, Base)
    app.debug = False
    app.run(host = '0.0.0.0', port = 8000)
  except KeyboardInterrupt:
    errorLogger('^C closing server')
  except DatabaseException as e:
    errorLogger(e, sys.exc_info())

