from app import Dependent, api, Resource
from helpers.UnwrapEntityList import unwrapFunc


@api.route('/dependent/all')
class allDependent(Resource):
    def get(self):
        allDependent = Dependent.query.all()
        unwrap = list(map(unwrapFunc, allDependent))
        return unwrap
