from flask import Flask, url_for, request, render_template, redirect, make_response
                                                                                     
app = Flask(__name__)
                                                                                     
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            username = request.form['username']
            resp = make_response(render_template('success.html'))
            resp.set_cookie('username', username)
            return resp
        else:
            error = 'Invalid username/password'
    elif request.method == 'GET':
        if 'username' in request.cookies:
            return redirect(url_for('welcome'))
        else:
            return render_template('login.html', error=error)
                                                                                     
@app.route('/logout')
def logout():
    resp = make_response(render_template('logout.html'))
    resp.delete_cookie('username')
    return resp
                                                                                     
@app.route('/welcome')
def welcome():
  if 'username' in request.cookies:
    return render_template('welcome.html', username=request.cookies.get('username'))
  else:
    return redirect(url_for('login'))
                                                                                     
def valid_login(username, password):
  if username == 'hoge' and password == 'fuga':
    return True
  else:
    return False
