from flask_restful import Resource, Api
from flask_restful import reqparse

from loginapi.app.models.UserModel import User
from loginapi.app import db

parser = reqparse.RequestParser()
parser.add_argument('userName')
parser.add_argument('passWord')

userList = []


class Users(Resource):

    def get(self):
        return ([user.__dict__ for user in userList])

    def post(self):
        args = parser.parse_args()
        user = User(username=args['userName'], password=args['passWord']);

        db.session.add(user)
        db.commit()

        return user.__dict__
