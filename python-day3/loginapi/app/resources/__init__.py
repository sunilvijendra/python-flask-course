from loginapi.app import api
from . import Users

#api.add_resource(User, '/user')
api.add_resource(Users, '/users')
#api.add_resource(Login, '/login')