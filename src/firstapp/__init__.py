from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api


app = Flask(__name__, instance_relative_config=True)
app.config.from_envvar('APP_CONFIG_FILE')
db = SQLAlchemy(app)
api = Api(app)


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/hi')


@app.route("/")
def hello():
    return "Hello World! prueba"
