from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify

from ..services.patient_request_processing import process_patient_request
from ..services.report_processing import process_report, get_hospital_status

app = Flask(__name__)
api = Api(app)


class Report(Resource):

    def post(self):
        if request.form['id']:
            result = process_report(request.form['report'])
            return jsonify(result)
        else:
            print("no feasible report id!")

    def get(self):
        if request.form['id']:
            result = get_hospital_status(request.form['hospital_id'])
            return jsonify(result)
        else:
            print("no feasible hospital id!")

class Request(Resource):

    def post(self):
        if request.form['id']:
            result = process_patient_request(request.form['request'])
            return jsonify(result)
        else:
            print("no feasible request id!")


api.add_resource(Report, '/report')
api.add_resource(Request, '/request')

if __name__ == '__main__':
    app.run(port='8080')
