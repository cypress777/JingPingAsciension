#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

memory = []

form = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"
  <meta name="viewport" contnet="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible content="ie=edge">
  <title>Ascention</title>
  <style>
    label, input, button {{
      margin: 8px;
    }}
  </style>
</head>

<body>
  <form method="POST">
    <h2>Ascention Login</h2>
    <label for="username">Username:</label>
    <input type="text" name="username" id="username">
    <br>
    <label for="pw">Password:</label>
    <input type="password" name="pw" id="pw">
    <br>
    <button type=submit id="login">Log in</button>
    <button type=submit id="signup">sign up</button>
    <param name="islogin" value="true">
  </form>

  <script type="test/javascript">
  document.getElementById("login").onclick = fuction() {loginFunction()};
  document.getElementById("signup").onclick = function() {signupFunction()};

  function loginFunction() {{
    document.getElementById("login").innerHTML = "log in ...";
  }}

  function signupFunction() {{
    document.getElementById("signup").innerHTML = "sign up...";
    document.getElementById("islogin").innerText = "false";
  }}
  </script>
  <pre>
{}
  </pre>
</body>
</html>
'''

class IndexHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)

    self.send_header('Content-type', 'text/html; charset=utf-8')
    self.end_headers()

    msg = form.format("\n".join(memory))
    self.wfile.write(msg.encode())

  def do_POST(self):
    length = int(self.headers.get('Content-length', 0))

    data = self.rfile.read(length).decode()

    message = parse_qs(data)["username"][0]

    message = message.replace("<", "&lt;")

    if len(memory) == 0:
      memory.append("Welcome new comers:\n")

    memory.append(message)
    
    self.send_response(303)
    self.send_header('Location', '/')
    self.end_headers()

if __name__ == '__main__':
  server_addr = ('', 80)
  httpd = HTTPServer(server_addr, IndexHandler)
  httpd.serve_forever()
