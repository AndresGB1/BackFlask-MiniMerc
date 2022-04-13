from flask import Flask, request, jsonify, Blueprint
from conexion import con_postgres
from . import rutas
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from .usuario import auth

api = Blueprint('api', __name__)


@api.route('/token', methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if len(auth(username, password)) == 0 :
        return {"msg": "Wrong username or password"}, 401
    access_token = create_access_token(identity=username)
    response = {"access_token":access_token}
    return response


@api.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response