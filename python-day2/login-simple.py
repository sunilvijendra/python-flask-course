from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('userName')
parser.add_argument('passWord')
parser.add_argument('userArg', location='args')

class User(object):
    def __init__(self, userId, userName, passWord, roleId):
        self.userId = userId
        self.userName = userName
        self.passWord = passWord
        self.roleId = roleId


userList = []

class UserResource(Resource):

    def get(self):
        return ([user.__dict__ for user in userList])

    def post(self):
        args = parser.parse_args()
        user = User(1, args['userName'], args['passWord'], 1);

        userList.append(user)

        #return {'userName' : user.userName }
        return user.__dict__

    def delete(self):
        args = parser.parse_args()
        userName = args['userArg']

        for user in userList:
            if (user.userName == userName):
                del userList[userList.index(user)]
                break

class Login(Resource):

    def post(self):
        return {'success' : True}

api.add_resource(Login, '/login')
api.add_resource(UserResource, '/users')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
