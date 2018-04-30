import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# db initialization
db = SQLAlchemy()
app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://ctdb1:750111@35.194.115.158/briantesting"
db.init_app(app)

# code for migrating db
migrate = Migrate(app, db)

# API routing in view.py
from views import *

if __name__ == '__main__':
    app.run(debug=True)