fail_form = '''<!DOCTYPE html>
<html lang='en'>
<head>
 <meta charset='UTF-8'>
 <meta name='viewport' content='width=device-width, initial-scale=1.0'>
 <title>Login Fail</title>
</head>

<body>
 <h2>Sorry</h2>
 <br>
 <button onclick="window.location.href='http://voidcypherplay.com:8000/login'">Return</button>
 <button onclick="window.location.href='http://voidcypherplay.com:80'">Home</button>
</body>

<pre>
{}
</pre>
</html>
'''

login_form = '''<!DOCTYPE html>
<html lang='en'>
<head>
 <meta charset='UTF-8'>
 <meta name='viewport' content='width=device-width, initial-scale=1.0'>
 <title>Welcome</title>
</head>

<body>
 <h2>Welcome Back</h2>
 <br>
 <button onclick="window.location.href='http://voidcypherplay.com:80'">Home</button>
</body>
<pre>
{}
</pre>
</html>
'''

signup_form = '''<!DOCTYPE html>
<html lang='en'>
<head>
 <meta charset='UTF-8'>
 <meta name='viewport' content='width=device-width, initial-scale=1.0'>
 <title>Welcome</title>
</head>

<body>
 <h2>Welcome, New Player</h2>
 <form method='GET'>
  <button type='submit'>Return</button>
 </form>
</body>
<pre>
{}
</pre>
</html>
'''
