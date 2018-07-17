from flask import Flask
from flask_restful import Api

from loginapi.src.resources.Users import UsersResource

app = Flask(__name__)
api = Api(app)

#api.add_resource(User, '/user')

api.add_resource(UsersResource, '/users')

#api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(debug=True)


