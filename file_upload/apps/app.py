from flask import Flask, request, render_template, redirect, session, url_for
from werkzeug.utils import secure_filename
                                                                              
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
                                                                              
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        session['filename'] = secure_filename(f.filename)
        f.save('/tmp/' + session['filename'])
        return redirect(url_for('done'))
    elif request.method == 'GET':
        return render_template('upload.html')
                                                                              
@app.route('/done')
def done():
    return render_template('done.html')
                                                                              
