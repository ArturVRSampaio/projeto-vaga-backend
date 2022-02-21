from app import Employee, api, Resource


@api.route('/Employee/all')
class allEmployee(Resource):
    def get(self):
        allEmployee = Employee.query.all()
        return allEmployee[1].name
