# file-transfer
A Basic File Transfer Server using Flask.

Dependencies:
  - Python3
  - Flask

Initialization:
  - Install Flask: (pip install Flask)
  - Either: run init.sh (linux) or (Make a directory called "UPLOADS" if it doesn't exist and set the env var "FLASK_APP" = "app.py")

How to run:
  - Server Side: In the file-transfer directory, type "python3 app.py" to run.
  - Client Side: Go to the appropriate localhost depending on the command line output of the flask server. Click "Upload" and upload the file. You will get a code that you can use to download. To Download, click "Download" on the landing page.
