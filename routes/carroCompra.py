"""conexion con postgresql para acceder a la base de datos de carro de compras"""
from flask import jsonify, request
from conexion import con_postgres
from . import rutas

@rutas.route("/carroCompra", methods=["GET"])
def get_carroCompra():
    """Obtener todos los carros de compras"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from carroCompra")
    carroCompra = conexion.fetchall()   
    conexion.close()
    print(carroCompra)
    return jsonify(carroCompra)

@rutas.route("/carroCompra/<string:username>", methods=["GET"])
def get_carroCompra_username(username):
    """Obtener carro de compras por username"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from carroCompra where username ='{0}'".format(username))
    carroCompra = conexion.fetchall()   
    conexion.close()
    return jsonify(carroCompra)

"""POST pasando como paramentro categoria, marca, cantidad, estado, fecha"""
@rutas.route("/carroCompra", methods=["POST"])
def post_carroCompra():
    """Agregar un carro de compras"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("insert into carroCompra values(%s,%s,%s,%s,%s)",
                     (request.json["username"], request.json["categoria"], request.json["marca"], request.json["cantidad"], request.json["estado"], request.json["fecha"]))
    con.commit()
    conexion.close()
    return jsonify(request.json)
