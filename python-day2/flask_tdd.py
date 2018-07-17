from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import pytest

app = Flask(__name__)
api = Api(app)

class SampleApi(Resource):
    def get(self):
        return {'test' : 123 }

api.add_resource(SampleApi, '/')

if __name__ == '__main__':
    app.run(debug=True)

@pytest.fixture
def client():
    app.Testing = True
    client = app.test_client()

    yield client

def test_SampleApi_get(client):
    rv = client.get('/')

    print(rv.json)
    assert rv.json['test'] == 123
