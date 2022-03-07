from app import Employee, api, Resource
from helpers.UnwrapEntityList import unwrapFunc


@api.route('/employee/all')
class allEmployee(Resource):
    def get(self):
        allEmployee = Employee.query.all()
        unwrap = list(map(unwrapFunc, allEmployee))
        return unwrap


@api.route('/employee/<int:id>')
class getEmployee(Resource):
    def get(self, id=id):
        employee = Employee.query.get(id)
        if employee:
            return repr(employee)
        else:
            return "nao encontrado"


@api.route('/employee/by/dept/<int:id>')
class getEmployeeByDept(Resource):
    def get(self, id=id):
        allEmployee = Employee.query.filter_by(department_id=id)
        if allEmployee:
            unwrap = list(map(unwrapFunc, allEmployee))
            return repr(unwrap)
        else:
            return "nao encontrado"