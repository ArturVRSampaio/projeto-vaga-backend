from app import Employee, api, Resource
from helpers.UnwrapEntityList import unwrapFunc


@api.route('/Employee/all')
class allEmployee(Resource):
    def get(self):
        allEmployee = Employee.query.all()
        unwrap = list(map(unwrapFunc, allEmployee))
        return unwrap
