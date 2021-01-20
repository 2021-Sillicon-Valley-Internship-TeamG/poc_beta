# Controller file : call & render html, data process
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from app.main import test_kakao
from flask_cors import CORS
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

CORS(app)

from app import dbcon
@app.route('/detect', methods=['POST'])
def detect():
    print("hihi")
    if request.form['image_type'] == "0":
        img_url = request.form['image_url']
        detect_result = test_kakao.detect_adult(img_url, 0)
        dbcon.add('img_url',img_url)
        return {"result" : detect_result}
    elif request.form['image_type'] == "1" :
        input_img = request.files['file']
        input_img_filename = secure_filename(input_img.filename)
        print(input_img)
        input_img.save(os.path.join('./data/', input_img_filename))
        detect_result = kakao_api.detect_adult('./data/'+input_img_filename, 1)
        dbcon.add('img_file','./data/'+img_filename)
        return {'result' : detect_result}
    
  
