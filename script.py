from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

import os

import csv

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload():
    if request.method == "POST":
        file = request.files["file"]

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            save_loc = os.path.join("data", filename).replace("\\","/")
            file.save(save_loc)

        with open(save_loc, newline="") as csvfile:
            return render_template("view_csv.html", csv=csvfile)
    
    return render_template("upload.html")