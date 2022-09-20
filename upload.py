import os
from flask import Flask, flash, request, redirect,render_template, url_for
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
    count=0
    if request.method == 'POST':
        # check if the post request has the file part
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        for filer in files:   #added
            count=count+1
            #filename = secure_filename(filer.filename) 
            #filer.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'],filename))
            #text = request.form['id']
        #    if file.filename == '':
         #       flash('No selected file') 
          #      return redirect(request.url)
            if filer and allowed_file(filer.filename):
                filename = secure_filename(filer.filename)

               

                #filer.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
                text = request.form['id']
                processed_text = text.upper()

                folder=processed_text+"/"
                UPLOAD_FOLDER2=os.path.join(app.root_path,'uploads/', folder)
                if not os.path.isdir(UPLOAD_FOLDER2):
                    os.mkdir(UPLOAD_FOLDER2)
                
                app.config['UPLOAD_FOLDER2']=UPLOAD_FOLDER2
                filer.save(os.path.join(app.config['UPLOAD_FOLDER2'], filename))
                #textfile = open("b.txt", "w")
                textfile = open("/home/momoisgoodforhealth/Flask_upload/b.txt", "w")
                textfile.write(processed_text)
                #shutil.copy('b.txt',processed_text+".txt")
                #textfile2 = open(processed_text+".txt", "w")
                #textfile2.write(str(count))
           
                #shutil.copy('/home/momoisgoodforhealth/Flask_upload/b.txt', '/home/momoisgoodforhealth/Flask_upload/'+folder+processed_text+".txt")
                #textfile2 = open("/home/momoisgoodforhealth/Flask_upload/"+folder+processed_text+".txt", "w")
                shutil.copy('/home/momoisgoodforhealth/Flask_upload/b.txt', UPLOAD_FOLDER2+processed_text+".txt")
                textfile2 = open(UPLOAD_FOLDER2+processed_text+".txt", "w")
                textfile2.write(processed_text)
                #return redirect(url_for('download_file', name=filename))


        return processed_text

    #<input type=text name="id"><br>n
    return '''
    <!doctype html>
    <a href="/downloads">Downloads</a>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <label for="id">Ride ID: </label>
      <input type="text" list="id" name="id" />
        <datalist id="id">
        <option>901</option>
        <option>801</option>
        <option>701</option>
        <option>501</option>
        </datalist>
  
      <label for="samplerate">Sample Rate: </label>
      <input type=text name="Sample Rate"><br>
      <label for="Ginterval">G Interval: </label>
      <input type=text name="Ginterval"><br>
      <label for="lowextent">Low Extent: </label>
      <input type=text name="lowextent"><br>
      <label for="highextent">High Extent: </label>
      <input type=text name="highextent"><br>
      <label for="files[]">Please Upload CSV File </label>
      <input type=file name="files[]" multiple="true"><br>
      <input type=submit value=Upload><br>
    </form>
    </form>
    '''


from flask import send_from_directory

@app.route('/downloads/', methods = ['GET', 'POST'])
def download_file():
    #return send_from_directory(app.config["UPLOAD_FOLDER"], name)
    return '''
    <!doctype html>
    <title>Uploads Site</title>
    <h1>Download from the following</h1>
    '''
