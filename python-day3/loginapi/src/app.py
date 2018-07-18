from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from loginapi.src.resources.Users import Users

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

#api.add_resource(User, '/user')

api.add_resource(Users, '/users')

#api.add_resource(Login, '/login')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


