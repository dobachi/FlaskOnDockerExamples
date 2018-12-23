from flask import Flask, url_for, request, render_template, redirect, session
                                                                                           
app = Flask(__name__)
                                                                                           
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('welcome'))
        else:
            app.logger.warning('Invalid username or password:' + request.form['username'])
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/welcome')
def welcome():
  if 'username' in session:
    return render_template('welcome.html', username=session['username'])
  else:
    return redirect(url_for('login'))

def valid_login(username, password):
  if username == 'hoge' and password == 'fuga':
    return True
  else:
    return False
