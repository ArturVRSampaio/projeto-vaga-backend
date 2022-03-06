import imp
from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, title="ACMEVita api", description="ACMEVita api ")

from DatabaseDriver import db
migrate = Migrate(app, db)

from models.Department import Department
from models.Dependent import Dependent
from models.Employee import Employee

from controllers.Department import *
from controllers.Dependent import *
from controllers.Employee import *

if __name__ == '__main__':
    app.run(debug=True)