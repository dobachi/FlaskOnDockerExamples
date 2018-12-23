from flask import Flask, url_for, request, render_template
                                                            
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'
                                                            
@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

@app.route('/post/<int:post_id>')
def post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
                                                            
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
                                                            
def do_the_login():
  return 'Do log in'
                                                            
def show_the_login_form():
  return 'This is a login form'
                                                            
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
                                                            
# Test for URLs
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
