from flask import Flask
from routes import login, rutas
from routes.login import api
from flask_cors import CORS 
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.register_blueprint(rutas)
app.register_blueprint(api)

app.config["JWT_SECRET_KEY"] = "dajoasdoaijasdi121312ioaajo"
jwt = JWTManager(app)

CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(port = 5000, debug = True)