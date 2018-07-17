from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import pytest

app = Flask(__name__)
api = Api(app)

class SampleApi(Resource):
    def get(self):
        return {'test' : 1234 }

class Employee(Resource):
    def get(self):
        return {'id' : 25045, 'name': "Ironman" }

api.add_resource(SampleApi, '/')
api.add_resource(Employee, '/avengers')

if __name__ == '__main__':
    app.run(debug=True)

# TEST CODE

@pytest.fixture
def client():
    app.Testing = True
    client = app.test_client()

    yield client

def test_SampleApi_get(client):
    rv = client.get('/')

    print(rv.json)
    assert rv.json['test'] == 1234

def test_Employee_test1(client):
    rv = client.get('/avengers')

    print (rv.json)
    assert rv.json['id'] == 25045
    assert rv.json['name'] == 'Ironman'
