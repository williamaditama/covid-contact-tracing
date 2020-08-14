from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

#user id arguments
userid_put_args = reqparse.RequestParser()
userid_put_args.add_argument("userID", type=str, help="User Unique ID")

user = {}

#location arguments

location_data_put_args = reqparse.RequestParser()
location_data_put_args.add_argument("latitude", type=float, help="Hotspot location latitude")
location_data_put_args.add_argument("longitude", type=float, help="Hotspot location longitude")

location = {}

locationrisk_put_args = reqparse.RequestParser()
locationrisk_put_args.add_argument("Inherent Risk", type=float, help="Inherent Risk value for Hotspot Location")

locationrisk = "Inherent Risk"


# error handling
def abort_if_userid_null(user_id):
    if user_id not in user:
        abort(404, message="UserId invalid")


def abort_if_userid_duplicate(user_id):
    if user_id in user:
        abort(409, message="userID already exist")



# userID class with get an put function
class UserId(Resource):
    def get(self, user_id):
        abort_if_userid_null(user_id)
        return user[user_id], 200

    def put(self, user_id):
        abort_if_userid_duplicate(user_id)
        args = userid_put_args.parse_args()
        user[user_id] = args
        return user[user_id], 201

    def get(self, user_risk):
        return


class LocationData(Resource):
    def put(self,location_data):
        args = location_data_put_args.parse_args()
        location[location_data] = args
        return location[location_data]


api.add_resource(UserId, "/userid/<string:user_id>")
api.add_resource(LocationData, "/locationdata/<string:location_data>")



if __name__ == '__main__':
    app.run(debug=True)
