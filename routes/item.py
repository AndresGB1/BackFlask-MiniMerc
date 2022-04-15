from flask import jsonify, request
from conexion import con_postgres, con_redis
from flask_jwt_extended import jwt_required
from . import rutas

@rutas.route("/items/<int:carroCompra>", methods=["GET"])
@jwt_required()
def get_items(carroCompra):
    """Obtener todos los items"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select i.id_item,i.cantidad,v.color ,pr.* from item as i, variante as v, producto as pr where (i.id_carro={0} and i.variante = v.id_variante and v.producto = pr.id_producto)".format(carroCompra))
    item = conexion.fetchall()
    conexion.close()
    return jsonify(item)

@rutas.route("/item", methods=["POST"])
@jwt_required()
def post_items():
    """Agregar un item"""
    carroCompra = request.json.get('carroCompra')
    variante = request.json.get('variante')
    cantidad = request.json.get('cantidad')
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("insert into item (variante, id_carro, cantidad) values ('{0}', '{1}', '{2}')".format(variante, carroCompra, cantidad))
    con.commit()
    conexion.close()
    return jsonify({"msg": "Item agregado"})

"""DELETE"""
@rutas.route("/item/<string:id>", methods=["DELETE"])
@jwt_required()
def delete_items(id):
    """Eliminar un item"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("delete from item where id_item = {0}".format(id))
    con.commit()
    conexion.close()
    return jsonify({"msg": "Item eliminado"})