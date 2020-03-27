from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify

from ..services import request_processing
from ..services import report_processing

app = Flask(__name__)
api = Api(app)


class Report(Resource):

    def post(self):
        if request.form['id']:
            result = report_processing(request.form['report'])
            return jsonify(result)
        else:
            print("no feasible report id!")


class Request(Resource):

    def post(self):
        if request.form['id']:
            result = request_processing(request.form['request'])
            return jsonify(result)
        else:
            print("no feasible request id!")


api.add_resource(Report, '/report')
api.add_resource(Request, '/request')

if __name__ == '__main__':
    app.run(port='8080')
