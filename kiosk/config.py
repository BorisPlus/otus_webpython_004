from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app_base_path = os.path.dirname(os.path.abspath(__file__))
app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
app = Flask(app_name)
app.secret_key = b'012465789'
db_path = '%s.db' % os.path.join(app_base_path, 'db', app_name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_path
db = SQLAlchemy(app)
