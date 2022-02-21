from app import Dependent, api, Resource


@api.route('/dependent/all')
class allDependent(Resource):
    def get(self):
        allDependent = Dependent.query.all()
        return allDependent[1].name
