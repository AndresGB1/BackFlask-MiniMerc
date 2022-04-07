"""conexion con postgresql para acceder a la base de datos de carro de compras"""
from flask import jsonify
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
