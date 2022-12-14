import os
from flask import Flask, flash, request, redirect,render_template, url_for, send_file
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
                ridetype= request.form['type'].upper()
                date=request.form['datadate'].upper()
                filterfreq=request.form['filter'].upper()
                rate=request.form['SampleRate'].upper()
                ginterval=request.form['Ginterval'].upper()
                lowext=request.form['lowextent'].upper()
                highext=request.form['highextent'].upper()


                folder=processed_text+"/"
                UPLOAD_FOLDER2=os.path.join(app.root_path,'uploads/', folder)
                if not os.path.isdir(UPLOAD_FOLDER2):
                    os.mkdir(UPLOAD_FOLDER2)
                
                app.config['UPLOAD_FOLDER2']=UPLOAD_FOLDER2
                filer.save(os.path.join(app.config['UPLOAD_FOLDER2'], filename))
                #textfile = open("b.txt", "w")
                textfile = open("/home/momoisgoodforhealth/Flask_upload/b.txt", "w")
                textfile.write(processed_text+"\n"+ridetype+"\n"+date+"\n"+filterfreq+"\n"+rate+"\n"+ginterval+"\n"+lowext+"\n"+highext)

                
                #shutil.copy('b.txt',processed_text+".txt")
                #textfile2 = open(processed_text+".txt", "w")
                #textfile2.write(str(count))
           
                #shutil.copy('/home/momoisgoodforhealth/Flask_upload/b.txt', '/home/momoisgoodforhealth/Flask_upload/'+folder+processed_text+".txt")
                #textfile2 = open("/home/momoisgoodforhealth/Flask_upload/"+folder+processed_text+".txt", "w")
                shutil.copy('/home/momoisgoodforhealth/Flask_upload/b.txt', UPLOAD_FOLDER2+processed_text+".txt")
                textfile2 = open(UPLOAD_FOLDER2+processed_text+".txt", "w")
                textfile2.write("RIDEID="+processed_text+"\n"+"RIDETYPE="+ridetype+"\n"+"DATE="+date+"\n"+"FILTER FREQUENCY="+filterfreq+"\n"+"RATE="+rate+"\n"+"G INTERVAL="+ginterval+"\n"+"LOW EXTENT="+lowext+"\n"+"HIGH EXTENT="+highext)
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
        </datalist><br>

      <label for="type">Type: </label>
      <input type="text" list="type" name="type" />
        <datalist id="type">
        <option>Rollercoaster</option>
        <option>Slide</option>
        </datalist><br>

      
      <label for="datadate">Data Date:</label>
      <input type="date" id="datadate" name="datadate"><br>

      <label for="filter">Filter Frequency: </label>
      <input type=text name="filter"><br>
      <label for="samplerate">Sample Rate: </label>
      <input type=text name="SampleRate"><br>
      <label for="Ginterval">G Interval: </label>
      <input type=text name="Ginterval"><br>
      <label for="lowextent">Low Extent: </label>
      <input type=text name="lowextent"><br>
      <label for="highextent">High Extent: </label>
      <input type=text name="highextent"><br>
      <br>
      <label for="files[]">Please Upload CSV File </label>
      <input type=file name="files[]" multiple="true"><br>
      <input type=submit value=Upload><br>
    </form>
    </form>
    '''


from flask import send_from_directory
dir_path = "/home/momoisgoodforhealth/Flask_upload/uploads"
rideids=[]
for path in os.listdir(dir_path):
        rideids.append(path)

@app.route('/downloads/', methods = ['GET', 'POST'])
def list_folders():
    shutil.make_archive('/home/momoisgoodforhealth/Flask_upload/assets/789zip','zip','/home/momoisgoodforhealth/Flask_upload/uploads/789')
    #return send_from_directory(app.config["UPLOAD_FOLDER"], name)
    return render_template("list.html", data=rideids)

@app.route('/static/789/', methods = ['GET', 'POST'])
def download_file():
    return send_file("/home/momoisgoodforhealth/Flask_upload/assets/789zip.zip", as_attachment=True)



