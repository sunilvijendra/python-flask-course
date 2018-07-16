from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('userName')
parser.add_argument('passWord')

class User:
    def __init__(self, userId, userName, passWord, roleId):
        self.userId = userId
        self.userName = userName
        self.passWord = passWord
        self.roleId = roleId

class Login(Resource):

    def post(self):
        args = parser.parse_args()
        user = User(1, args['userName'], args['passWord'], 1);

        return {'userName' : user.userName }
        
api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(debug=True)
