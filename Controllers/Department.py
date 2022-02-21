from app import Department, api, Resource


@api.route('/department/all')
class allDepartment(Resource):
    def get(self):
        allDepartment = Department.query.all()
        return allDepartment[1].name
