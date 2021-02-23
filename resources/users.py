from flask_restful import Resource, reqparse
from models.users import User as UserModel


class RegisterUser(Resource):
    u_prs = reqparse.RequestParser()
    u_prs.add_argument('username',
                       type=str,
                       required=True,
                       help="parameter should be String")

    u_prs.add_argument('password',
                       type=str,
                       required=True,
                       help="parameter should be String")

    def post(self):
        parsed = RegisterUser.u_prs.parse_args()
        u = UserModel.find_by_username(parsed.username)
        if u:
            return {"message": "Already Registered"}, 400
        else:
            UserModel(parsed.username, parsed.password).save()
            return {"message": "User was added successfully"}, 200
