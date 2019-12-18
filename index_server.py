#!/usr/bin/env python3

import os
import threading
from socketserver import ThreadingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

users = {}

fail_form = '''<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Login Fail</title>
</head>

<body>
 <form method="GET">
  <h2>Sorry</h2>
  <br>
  <button type="submit">Return</button>
 </form>
</body>

<pre>
{}
</pre>
</html>
'''

success_form = '''<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Welcome</title>
</head>

<body>
 <h2>Welcome</h2>
</body>
<pre>
{}
</pre>
</html>
'''

class IndexHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(303)
    self.send_header('Location', 'http://voidcypherplay.com:80')
    self.end_headers()

  def do_POST(self):
    length = int(self.headers.get('Content-length', 0))

    data = self.rfile.read(length).decode()

    print(data)

    username = parse_qs(data)["username"][0]

    password = parse_qs(data)["pw"][0]

    is_login = parse_qs(data)["islogin"][0]

    send_form = success_form

    if is_login == 'true':
      if username not in users:
        send_form = fail_form.format("user not exist")
      elif password != users[username]:
        send_form = fail_form.format("wrong password")
      else:
        send_form = success_form.format(username)
    else:
      if username in users:
        send_form = fail_form.format("user existed, please try another")
      else:
        users.update({username:password})
        send_form = success_form.format(username)

    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(send_form.encode())

class ThreadHTTPServer(ThreadingMixIn, HTTPServer):
  pass

if __name__ == '__main__':
  server_addr = ('', 8000)
  httpd = ThreadHTTPServer(server_addr, IndexHandler)
  httpd.serve_forever()
