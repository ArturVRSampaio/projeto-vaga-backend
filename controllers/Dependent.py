from app import Dependent, api, Resource
from helpers.UnwrapEntityList import unwrapFunc


@api.route('/dependent/all')
class allDependent(Resource):
    def get(self):
        allDependent = Dependent.query.all()
        unwrap = list(map(unwrapFunc, allDependent))
        return unwrap

@api.route('/dependent/<int:id>')
class getDependent(Resource):
    def get(self, id=id):
        dependent = Dependent.query.get(id)
        if dependent:
            return repr(dependent)
        else:
            return "nao encontrado"
