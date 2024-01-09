import re
import filetype
from database import db

#OK
def validarNombre(nombre):
    if nombre.isspace(): return False
    regex = r'\d'
    res = re.search(regex, nombre)
    if (3 < len(nombre) < 80) and (res == None):
        return True
    else:
        return False
    
#OK
def validarEmail(mail):
    regex = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    if len(mail) == 0: return False
    if len(mail) > 30: return False
    if re.match(regex, mail): return True
    else: return False

#OK
def validarNumero(numero):
    regex = r'^\+56[1-9]\d{8}$'
    if len(numero) == 0: return True
    if re.match(regex, numero): return True
    else:
        return False

#OK
def validarDescripcion(descripcion):
    if descripcion == None: return True
    if 0 <= len(descripcion) < 30: return True
    else:
        return False

#OK
def validarFotos(fotos):
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    ALLOWED_MIMETYPES = set(['image/png', 'image/jpeg', 'image/gif'])
    if not 0 < len(fotos) <= 3:
        return False
    for foto in fotos:
        if foto is None:
            return False,
        if foto.filename == "":
            return False
        fototype = filetype.guess(foto)
        if fototype.extension not in ALLOWED_EXTENSIONS:
            return False
        if fototype.mime not in ALLOWED_MIMETYPES:
            return False
    return True

#########DEPENDIENTES DE ID###############

#OK
def validarTipos(tipos):
    if len(tipos) == 0: return False
    if len(tipos) > 3: return False
    for tipo in tipos:
        tipo_id = (db.get_tipo_id(tipo))[0]
        if tipo_id == None:
            return False
        if tipo_id < 1 or tipo_id > 9:
            return False
    return True

#OK
def validarComunaRegion(comuna, region):
    if len(comuna) == 0: return False
    if len(region) == 0: return False

    comuna_id = db.get_comuna_id(comuna)[0]
    region_id = db.get_region_id(region)[0]
    if comuna_id == None: return False
    if region_id == None: return False

    if comuna_id < 10101 or comuna_id > 130606: return False
    if region_id < 1 or region_id > 16: return False

    return True

#OK
def validarTransporte(transporte):
    if transporte == "particular" or transporte == "Locomoción Pública": return True
    else: return False

#OK
def validarDeportes(deportes):
    if len(deportes) == 0: return False
    if len(deportes) > 3: return False
    for dep in deportes:
        dep = db.get_deportes_id(dep)
        dep_id = dep[0][0]
        if dep_id == None:
            return False
        if dep_id < 1 or dep_id > 60:
            return False
    return True


##FUNCIONES VALIDADORAS##
def validarA(descripcion, nombre, email, numero, fotos, tipos, comuna, region):
    if not validarDescripcion(descripcion):
        return False, "Descripción errónea"
    if not validarNombre(nombre):
        return False, "Nombre erróneo"
    if not validarEmail(email):
        return False, "Email erróneo"
    if not validarNumero(numero):
        return False, "Numero erróneo"
    if not validarFotos(fotos):
        return False, "Fotos erróneas"
    if not validarTipos(tipos):
        return False, "Tipos erróneos"
    if not validarComunaRegion(comuna, region):
        return False, "Comuna o region errónea"
    else:
        return True, None

def validarH(nombre,email,numero,comuna,region,transporte,deportes,comentarios):
    if not validarNombre(nombre):
        return False, "Nombre erróneo"
    if not validarEmail(email):
        return False, "Email erróneo"
    if not validarNumero(numero):
        return False, "Numero erróneo"
    if not validarComunaRegion(comuna, region):
        return False, "Comuna o region errónea"
    if not validarTransporte(transporte):
        return False, "Transporte erróneo"
    if not validarDeportes(deportes):
        return False, "Deportes erróneos"
    if not validarDescripcion(comentarios):
        return False, "Descripcion errónea"
    else:
        return True, None
        