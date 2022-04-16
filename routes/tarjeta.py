from flask import jsonify, request
from conexion import con_postgres
from flask_jwt_extended  import jwt_required
from . import rutas


@rutas.route("/tarjeta", methods=["POST"])
@jwt_required()
def post_tarjeta():
    con = con_postgres.postgres
    conexion = con.cursor()
    numero = request.json.get("numero", None)
    tipo = request.json.get("tipo", None)
    nombre = request.json.get("nombre", None)
    fecha = request.json.get("fecha", None)
    cvv = request.json.get("cvv", None)
    conexion.execute("insert into tarjeta (id_numero,tipo, nombre, expiración, cvv) values ('{0}', '{1}', '{2}', '{3}', '{4}')".format(numero, tipo, nombre, fecha, cvv))
    con.commit()
    conexion.close()
    return jsonify({"status": "ok"})
