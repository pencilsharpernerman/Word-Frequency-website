from __future__ import print_function

import os
from flask import Flask, request, redirect, url_for,render_template
from werkzeug import secure_filename
import main
import sys
UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    output = []
    if request.method == 'POST':
        file = request.files['file']
      
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            output = main.top25FrequentWords(filename)
            return render_template("template.html", output=output)
           
    return render_template("template.html")

# @app.route('/')
# def script_output(output):
#         return render_template("template.html", output=request.args.get('output'))

if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)