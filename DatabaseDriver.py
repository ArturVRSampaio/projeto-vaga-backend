from flask_sqlalchemy import SQLAlchemy
from app import app

db_name = 'acmevita.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

db = SQLAlchemy(app)
