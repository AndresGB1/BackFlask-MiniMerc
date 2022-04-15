from flask import jsonify, request
from conexion import con_postgres, con_mongo
from . import rutas

@rutas.route("/compra", methods=["POST"])
def post_compra():
    """direccion,tipo,tarjeta,ciudad,pais,estado"""
    con = con_postgres.postgres
    conexion = con.cursor()
    direccion = request.json.get("direccion", None)
    tipo = request.json.get("tipo", None)
    tarjeta = request.json.get("tarjeta", None)
    estado = request.json.get("estado", None)
    ciudad = request.json.get("ciudad", None)
    pais = request.json.get("pais", None)
    conexion.execute("insert into compra (direccion,tipo,tarjeta,ciudad,pais,estado) values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(direccion, tipo, tarjeta, ciudad, pais, estado))   
    con.commit()
    conexion.close()
    return jsonify({"status": "ok"})