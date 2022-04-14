"""conexion con postgresql para acceder a la base de datos de carro de compras"""
from flask import jsonify, request
import jwt
from conexion import con_postgres
from . import rutas
from flask_jwt_extended import jwt_required



@rutas.route("/carroCompra/<string:username>", methods=["GET"])
@jwt_required()
def get_carroCompra_username(username):
    """Obtener carro de compras por username"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from carroCompra where comprador ='{0}'".format(username))
    carroCompra = conexion.fetchall()   
    conexion.close()
    return jsonify(carroCompra)

"""POST pasando como paramentro comprador, cantidad, estado, fecha"""
@rutas.route("/carroCompra", methods=["POST"])
@jwt_required()
def post_carroCompra():
    """Crear carro de compras"""
    con = con_postgres.postgres
    conexion = con.cursor()

    comprador = request.json.get("comprador", None)
    cantidad = request.json.get("cantidad", None)
    fecha = request.json.get("fecha", None)

    try:
        conexion.execute("select * from carroCompra where comprador = '{0}' and estado = 'P'".format(comprador))
        carroCompra = conexion.fetchall()
        if len(carroCompra) == 0:
            conexion.execute("insert into carroCompra (comprador, cantidad, estado, fecha) values ('{0}', {1}, '{2}', '{3}')".format(comprador, cantidad, 'P', fecha))
            conexion.commit()
            conexion.close()
            return jsonify({"message": "Carro de compras creado"})
        else:
            return jsonify(carroCompra[0][0])
    except Exception as e:
        return jsonify({"message": "Error al crear carro de compras"})


@rutas.route("/carroCompra/<string:username>/<string:id>/abandonar", methods=["PUT"])
@jwt_required()
def put_carroCompra_username(username, id):
    """Actualizar carro de compras por username"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from carroCompra where comprador ='{0}'".format(username))
    carroCompra = conexion.fetchall()   
    comprador = carroCompra[0][0]
    cantidad = carroCompra[0][1]
    fecha = carroCompra[0][3]
    conexion.execute("update carroCompra set comprador = '{0}', cantidad = {1}, estado = '{2}', fecha = '{3}' where id_carro = {4}".format(comprador, cantidad, 'A', fecha, id))
    con.commit()
    conexion.close()
    return jsonify({"msg": "carro de compras actualizado"})

@rutas.route("/carroCompra/<string:username>/<string:id>", methods=["DELETE"])
@jwt_required()
def delete_carroCompra_username(username, id):
    """Eliminar carro de compras por username"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("delete from carroCompra where id_carroCompra = {0}".format(id))
    con.commit()
    conexion.close()
    return jsonify({"msg": "carro de compras eliminado"})


