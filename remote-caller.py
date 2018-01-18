from flask import Flask, request
from flask_restful import Resource, Api
import requests
import sys
import time

app = Flask(__name__)
api = Api(app)


class TodoSimple(Resource):
    def get(self):
        r = requests.get('https://httpbin.org/uuid')
        return r.text

api.add_resource(TodoSimple, '/test')


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        run_port = sys.argv[1]
    else:
        run_port = 10002
    app.run(host='0.0.0.0',port=int(run_port), debug=True)
