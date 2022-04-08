from flask import Flask
from routes import rutas
from flask_cors import CORS 

app = Flask(__name__)
app.register_blueprint(rutas)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(port = 5000, debug = True)