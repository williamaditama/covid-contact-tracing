from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

userid_put_args = reqparse.RequestParser()
userid_put_args.add_argument("userID", type=str, help="User Unique ID")

user = {}


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
        return user[user_id]

    def put(self, user_id):
        args = userid_put_args.parse_args()
        abort_if_userid_duplicate(user_id)
        user[user_id] = args
        return user[user_id], 201



api.add_resource(UserId, "/userid/<string:user_id>")

if __name__ == '__main__':
    app.run(debug=True)
