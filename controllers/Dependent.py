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



@api.route('/dependent/by/employee/<int:id>')
class getDependentByEmployee(Resource):
    def get(self, id=id):
        allDependent = Dependent.query.filter_by(department_id=id)
        if allDependent:
            unwrap = list(map(unwrapFunc, allDependent))
            return repr(unwrap)
        else:
            return "nao encontrado"