######################
# Server Side Python for File Uploader
# Runs on python3.
# Dependencies: flask (pip3 install flask/pip install flask)
######################

from flask import Flask, render_template, request, send_from_directory
from werkzeug import secure_filename
import random
import os
import string

app = Flask(__name__)
UPLOAD_PATH = "UPLOADS"

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        #code = ""
        code = create_random_code(8)
        upload_path = os.path.join(UPLOAD_PATH, code)
        while(os.path.isdir(upload_path)):
            code = create_random_code(8)
            upload_path = os.path.join(UPLOAD_PATH, code)
        os.mkdir(upload_path)
        f.save(os.path.join(upload_path, secure_filename(f.filename)))
        return 'file uploaded successfully. use the code {} to download'.format(code)
    else:
       return render_template('upload.html')

@app.route('/download', methods = ['GET', 'POST'])
def download():
    if request.method == 'POST':
        code = request.form['file_code']
        folder = os.path.join(UPLOAD_PATH, code)

        if not os.path.isdir (folder):
            return "error: code unavailable"
        files = os.listdir(folder)

        if len(files) < 1:
            return "error: file unavailable"

        return send_from_directory(directory=folder, filename=files[0], as_attachment = True)
        
    else:
        return render_template('download.html')

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0')

def create_random_code(size=8):
   return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
