# Controller file : call & render html, data process
import os
from flask import Flask, render_template, request

app = Flask(__name__)

  
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        print("hi")
        return render_template('result.html')
  
