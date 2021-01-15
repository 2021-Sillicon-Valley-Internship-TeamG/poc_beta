from app import db
from . import models
def add(img_type,imgdir):
    img = models.img_upload(img_type,imgdir)
    db.session.add(img)
    db.session.commit()

def read():
    return db.session.query(models.img_upload.imgdir).all()

def count():
    return db.session.query(models.img_upload).count()