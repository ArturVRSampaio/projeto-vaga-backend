import imp
from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, title="ACMEVita api", description="ACMEVita api ")

from DatabaseDriver import db
migrate = Migrate(app, db)

from Models.Department import Department
from Models.Dependent import Dependent
from Models.Employee import Employee

from Controllers.Department import *
from Controllers.Dependent import *
from Controllers.Employee import *

if __name__ == '__main__':
    app.run(debug=True)