from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__, instance_relative_config=True)
app.config.from_envvar('APP_CONFIG_FILE')
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello World! prueba"
