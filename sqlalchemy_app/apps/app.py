from flask import Flask, url_for, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

@app.route('/regist', methods=['POST', 'GET'])
def regist():
    if request.method == 'POST':
        user = User(username=request.form['username'], email=request.form['email'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('list'))
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('regist.html')

@app.route('/list')
def list():
    users = User.query.order_by(User.username).all()
    return render_template('list.html', users=users)
