from flask import jsonify, request
from conexion import con_postgres, con_mongo
from flask_jwt_extended  import jwt_required
from . import rutas

@rutas.route("/compra", methods=["POST"])
@jwt_required()
def post_compra():

    """Guardar en mongo la info de la compra con_mongo. y en postgres """
    record = request.json
    con = con_mongo.mongo
    db = con["mercado"]
    col = db["compra"]
    col.insert_one(record)
    con = con_postgres.postgres
    conexion = con.cursor()
    id_compra = request.json.get("id_compra", None)
    direccion = request.json.get("direccion", None)
    tipo = request.json.get("tipo", None)
    tarjeta = request.json.get("tarjeta", None)
    estado = request.json.get("estado", None)
    ciudad = request.json.get("ciudad", None)
    pais = request.json.get("pais", None)
    conexion.execute("insert into compra (id_compra,direccion,tipo,tarjeta,ciudad,pais,estado) values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(id_compra, direccion, tipo, tarjeta, ciudad, pais, estado))
    con.commit()
    conexion.close()    
    return jsonify({"status": "ok"})
    
 
    

  