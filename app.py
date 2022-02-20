from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, title="ACMEVita api", description="ACMEVita api ")

@api.route('/example/')
class hello_world(Resource):
    def get(self):
        return {'hi': 'yeah'},200
    def post(self):
        return {'hi': 'yeah'},201
    def put(self):
        return {'hi': 'yeah'},404
    def delete(self):
        return {'hi': 'yeah'},403
    def patch(self):
        return {'hi': 'yeah'},500




if __name__ == '__main__':
    app.run(debug=True)