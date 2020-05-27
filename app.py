from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "This is webapp for students,Deployed with {} and db_uri is {}".format(os.environ.get('APP_SETTINGS'),os.environ.get('DATABASE_URI'))

if __name__ == '__main__':
    app.run()