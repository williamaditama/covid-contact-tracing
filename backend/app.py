from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

from calculations import Simulation
import json
from db_interface import connect, add_user, add_loc

app = Flask(__name__)
api = Api(app)

# userID class with get an put function
class NewUser(Resource):
    def post(self):
        json_request = request.get_json()
        add_user(json_request['userID'])
        return {'message': 'Success'}, 200


class GetRiskLevel(Resource):
    def post(self):
        json_request = request.get_json()
        lat, lng = json_request['lat'], json_request['lng']

        sim = Simulation()
        risk = sim.risk_field((lat, lng))

        return {'risk': risk}, 200


class AddLocationData(Resource):
    def post(self):
        json_request = request.get_json()
        add_loc(json_request['userID'], json_request['lat'], json_request['lng'], json_request['timestamp'])
        return {'message': 'Success'}, 200



api.add_resource(NewUser, "/new_user")
api.add_resource(AddLocationData, "/new_location")
api.add_resource(GetRiskLevel, "/risk_level")



if __name__ == '__main__':
    app.run(debug=True)
