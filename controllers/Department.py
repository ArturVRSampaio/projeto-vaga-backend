from app import Department, api, Resource
from helpers.UnwrapEntityList import unwrapFunc

@api.route('/department/all')
class allDepartment(Resource):
    def get(self):
        allDepartment = Department.query.all()
        unwrap = list(map(unwrapFunc, allDepartment))
        return unwrap