import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import shutil

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

rel_directory=os.path.realpath('.')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file') 
            return redirect(request.url)
        if file and allowed_file(file.filename):
            text = request.form['name']
            processed_text = text.upper()

            textfile = open("/home/momoisgoodforhealth/Flask_upload/b.txt", "w")
            textfile.write(processed_text)

            shutil.copy2('/home/momoisgoodforhealth/Flask_upload/b.txt', '/home/momoisgoodforhealth/Flask_upload/newname.txt')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('download_file', name=filename))
            return processed_text
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=text name="name">
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>

    </form>
    '''


from flask import send_from_directory

@app.route('/uploads/')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)