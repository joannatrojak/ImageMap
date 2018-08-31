# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 09:27:55 2018

@author: joanna
"""

from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
import os.path
from ImageLocation import Image

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/images'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/upload')
def upload_file_template():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      image = Image(app.config['UPLOAD_FOLDER'])
      
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return image.getLocation(filename)
      #return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True)
   app.secret_key='secret123'
   