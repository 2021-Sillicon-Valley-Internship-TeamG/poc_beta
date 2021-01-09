# Controller file : call & render html, data process
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from app.main import test_kakao

app = Flask(__name__)

  
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

    elif request.method == 'POST':
        img_url = request.form['input_url']
        client_img = request.files['client_img']

        if img_url != "":
            detect_result = test_kakao.detect_adult(img_url, 0)
            return render_template('result.html', img_url=img_url, detect_result=detect_result)
        elif client_img != "":
            img_filename = secure_filename(client_img.filename)
            client_img.save(os.path.join('./app/static/image/', img_filename))
            detect_result = test_kakao.detect_adult('././app/static/image/'+img_filename, 1)
            return render_template('result.html', img_url='../static/image/'+img_filename, detect_result=detect_result)
    
  
