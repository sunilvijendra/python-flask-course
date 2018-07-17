from flask_restful import Resource, Api
from flask_restful import reqparse

from loginapi.src.models.UserModel import UserModel

parser = reqparse.RequestParser()
parser.add_argument('userName')
parser.add_argument('passWord')

userList = []

class UsersResource(Resource):

    def get(self):
        return ([user.__dict__ for user in userList])

    def post(self):
        args = parser.parse_args()
        user = UserModel(1, args['userName'], args['passWord'], 1);

        userList.append(user)

        return user.__dict__