# Controller file : call & render html, data process
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from app.main import test_kakao
import configparser
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
config = configparser.ConfigParser()
config.read('config.ini')
app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = config['DEFAULT']['SQLALCHEMY_DATABASE_URI']
# 추가하지 않을 시 FSADeprecationWarning 주의가 떠서 추가해 줌
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import dbcon
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        img = dbcon.read()
        new_img = []
        for i in range(dbcon.count()):
            new_img.append(img[i][0])
        return render_template('home.html',img_url=new_img)

    elif request.method == 'POST':
        img_url = request.form['input_url']
        
        client_img = request.files['client_img']

        if img_url != "":
            detect_result = test_kakao.detect_adult(img_url, 0)
            dbcon.add('img_url',img_url)
            return render_template('result.html', img_url=img_url, detect_result=detect_result)
        elif client_img != "":
            img_filename = secure_filename(client_img.filename)
            client_img.save(os.path.join('./app/static/image/', img_filename))
            file_path='././app/static/image/'+img_filename
            detect_result = test_kakao.detect_adult(file_path, 1)
            dbcon.add('img_file','../static/image/'+img_filename)
            return render_template('result.html', img_url='../static/image/'+img_filename, detect_result=detect_result)
    
  
