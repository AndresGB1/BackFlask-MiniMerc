from flask import Flask
from routes import rutas


app = Flask(__name__)

app.register_blueprint(rutas)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(port = 5000, debug = True)