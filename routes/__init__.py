from flask import Blueprint

rutas = Blueprint('rutas', __name__)

from .carroCompra import *
from .producto import *
from .variante import *
from .usuario import *
from .login import *
from .categoria import *
from .item import *
from .compra import *
from .tarjeta import *