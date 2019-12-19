#!/usr/bin/env python3

import os
import sys
import threading
from socketserver import ThreadingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from index_forms import fail_form, login_form, signup_form

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database_setup import Base, DatabaseName, UserInfo

from utils import infoLogger, errorLogger, debugLogger

ErrorCodes = {404 : 'page not found/n\n'}

class DatabaseException(Exception): pass
DatabaseSession = None

class IndexHandler(BaseHTTPRequestHandler):
  global DatabaseSession, ErrorCodes

  def do_GET(self):
    try:
      self.send_response(303)
      self.send_header('Location', 'http://voidcypherplay.com:80')
      self.end_headers()
    except IOError:
      self.send_error(404, ErrorCodes[404])
   
  def do_POST(self):
    try:
      length = int(self.headers.get('Content-length', 0))
  
      data = self.rfile.read(length).decode()
  
      username = parse_qs(data)['username'][0]
      password = parse_qs(data)['pw'][0]
      is_login = parse_qs(data)['islogin'][0]

      userinfo = DatabaseSession.query(UserInfo).filter_by(name=username).first()

      user_existed = (userinfo != None)
      password_matched = (user_existed and userinfo.password == password)

      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
 
      if is_login == 'true':
        if not user_existed:
          self.wfile.write(fail_form.format('user not exist').encode())
        elif not password_matched:
          self.wfile.write(fail_form.format('wrong password').encode())
        else:
          self.wfile.write(login_form.format(username).encode())
      else:
        if user_existed:
          self.wfile.write(fail_form.format('user existed, please try another').encode())
        else:
          new_user = UserInfo(name=username, password=password)
          DatabaseSession.add(new_user)
          DatabaseSession.commit()

          self.wfile.write(signup_form.format(username).encode())
    except:
      errorLogger('unknown error', sys.exc_info())
      try:
        self.send_response(303)
        self.send_header('Location', 'http://voidcypherplay.com:80')
        self.end_headers()
      except IOError:
        self.send_error(404, ErrorCodes[404])

class ThreadHTTPServer(ThreadingMixIn, HTTPServer):
  pass

def initDataBase():
  global DatabaseSession
  try:
    engine = create_engine('sqlite:///{}'.format(DatabaseName),
      connect_args={'check_same_thread': False},
      poolclass=StaticPool, echo=True)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind = engine)
    DatabaseSession = DBSession()
    infoLogger('database inited')
  except:
    raise DatabaseException('during database init')


if __name__ == '__main__':
  httpd = None
  try:
    initDataBase()
    server_addr = ('', 8000)
    httpd = ThreadHTTPServer(server_addr, IndexHandler)
    infoLogger('server running')
    httpd.serve_forever()
  except KeyboardInterrupt:
    errorLogger('^C closing server')
  except DatabaseException as de:
    print(de, sys.exc_info())
  finally:
    if httpd != None:
      httpd.socket.close()
    if DatabaseSession != None:
      DatabaseSession.close()

