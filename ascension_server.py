#!/usr/bin/env python3

from flask import Flask, render_template, request, url_for, redirect, flash
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
  return render_template('welcome.html', welcome_info='Welcome Back', username=username)

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

def sign_up_user(username, password):
  try:
    new_user = UserInfo(name=username, password=password)
    DatabaseSession.add(new_user)
    DatabaseSession.commit()
  except:
    raise

  return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/en', methods=['GET', 'POST'])
def Welcome():
  return render_template('hello.html')

@app.route('/login', methods=['GET', 'POST'])
def Login():
  error = None

  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    if is_valid_log_in(username, password):
      return log_in_user(username)
    else:
      error = 'Invalid log in: Wrong username/password'
    flash(error)

  return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def Signup():
  error = None

  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    if is_valid_sign_up(username, password):
      return sign_up_user(username, password)
    else:
      if has_username(username):
        error = 'Invalid sign up: Username has been taken'
      else:
        error = 'Invalid password: password should be letters and numbers'
      flash(error)

  return render_template('signup.html')

if __name__ == '__main__':
  try:
    DatabaseSession = init_database(DatabaseName, Base)
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
  except KeyboardInterrupt:
    errorLogger('^C closing server')
  except DatabaseException as e:
    errorLogger(e, sys.exc_info())
  finally:
    if DatabaseSession != None:
      DatabaseSession.close()
