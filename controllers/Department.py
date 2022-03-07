from app import Department, api, Resource
from helpers.UnwrapEntityList import unwrapFunc

@api.route('/department/all')
class allDepartment(Resource):
    def get(self):
        allDepartment = Department.query.all()
        unwrap = list(map(unwrapFunc, allDepartment))
        return unwrap

@api.route('/department/<int:id>')
class getDepartment(Resource):
    def get(self, id=id):
        department = Department.query.get(id)
        if department:
            return repr(department)
        else:
            return "nao encontrado"