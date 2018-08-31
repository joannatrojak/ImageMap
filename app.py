# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 09:27:55 2018

@author: joanna
"""

from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

if __name__ == '__main__':
   app.run(debug = True)