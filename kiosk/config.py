from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app_base_path = os.path.dirname(os.path.abspath(__file__))
app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
app = Flask(app_name)
app.secret_key = b'012465789'
db_folder = os.path.join(app_base_path, 'db')
if not db_folder:
    os.mkdir(db_folder)
db_file = '%s.db' % os.path.join(db_folder, app_name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_file
db = SQLAlchemy(app)
