from flask import Blueprint

rutas = Blueprint('rutas', __name__)

from .carroCompra import *
from .producto import *
from .usuario import *
