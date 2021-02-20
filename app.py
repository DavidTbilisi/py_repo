from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
from resources.books import Item, ItemList
from resources.users import RegisterUser

app = Flask(__name__)
app.secret_key = "this_is_secret"
api = Api(app)
jwt = JWT(app, authenticate, identity)
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.sqlite"


@app.before_first_request
def create_table():
    db.create_all()



@app.route('/')
@jwt_required()
def greetings():
    return f"Hello, {current_identity}"


api.add_resource(Item, '/item/<int:item_id>')
api.add_resource(ItemList, '/list')
api.add_resource(RegisterUser, '/registration')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
