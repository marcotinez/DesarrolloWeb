from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import cross_origin
from database import db
from utils.validations import validarA, validarH
from werkzeug.utils import secure_filename
import os
import hashlib
import filetype
import math

UPLOAD_FOLDER = 'static/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template("auth/index.html")

#######################################################################################
#-------------------------------------ARTESANOS----------------------------------------
#######################################################################################
@app.route('/art-register', methods=['GET', 'POST'])
def art_register():
    if request.method == 'POST':
        comuna = request.form.getlist("comunas") #OK
        region = request.form.get("regiones") #OK
        descripcion = request.form.get("descripcion") #OK
        nombre = request.form.get("username") #OK
        email = request.form.get("email") #OK
        numero = request.form.get("number") #OK
        foticos = request.files.getlist('foto') #OK
        tipos = request.form.getlist("tipo") #OK
        msg = ""
        validacion, msg = validarA(descripcion, nombre, email, numero, foticos, tipos, comuna, region)
        
        if validacion:
            if descripcion == None: descripcion = ""
            status_artesano, msg = db.registrar_artesano(comuna, descripcion, nombre, email, numero)
            if status_artesano:
                artesano_id = db.get_artesano_id(nombre)
                for tipo in tipos:
                    tipo_id = db.get_tipo_id(tipo)
                    status_tipo = db.registrar_artesano_tipo(artesano_id, tipo_id)
                for foto in foticos:
                    _filename = hashlib.sha256(
                        secure_filename(foto.filename) # nombre del archivo
                        .encode("utf-8") # encodear a bytes
                        ).hexdigest()
                    _extension = filetype.guess(foto).extension
                    img_filename = f"{_filename}.{_extension}"

                    foto.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
                    status_foto = db.agregar_foto(app.config['UPLOAD_FOLDER'], img_filename, artesano_id)

            if status_artesano and status_tipo and status_foto:
                msg = "Artesano registrado exitosamente"
                return render_template("auth/index.html", msg=msg)
        
        return render_template("form/art_register.html", error=msg)
    
    return render_template("form/art_register.html")

@app.route('/lista-artesanos', methods=["GET"])
def ver_artesanos():
    if db.get_total_artesanos() == 0:
        return render_template("form/ver_artesano.html")
    else:
        pagina = request.args.get("pagina",1,type=int)
        tamaño_pagina = 5
        offset = (pagina - 1) * tamaño_pagina
        total_artesanos = db.get_total_artesanos()
        total_paginas = math.ceil(total_artesanos[0] / tamaño_pagina)

        data_artesanos = []
        lista_fotos = []
        for artesano in db.get_artesanos(tamaño_pagina, offset):
            id, comuna_id, _, nombre, _, celular = artesano
            comuna = db.get_comuna(comuna_id)
            
            if celular == '': celular = "No disponible"
            
            tipos = []
            tipos_str = ""
            for tipo in db.get_tipos(id):
                tipos.append(tipo[0])
            if len(tipos) == 1:
                tipos_str = "%s" % tipos[0]
            elif len(tipos) == 2:
                tipos_str = "%s, %s" % (tipos[0], tipos[1])
            elif len(tipos) == 3:
                tipos_str = "%s, %s, %s" % (tipos[0], tipos[1], tipos[2])
            
            for foto in db.get_fotos(id):
                lista_fotos.append(f"uploads/{foto[1]}")

            data_artesanos.append({
                    "nombre": nombre,
                    "telefono": celular,
                    "comuna": comuna[0],
                    "tipos": tipos_str,
                    "fotos": lista_fotos,
                    "id": id
                })
            lista_fotos = []
    return render_template("form/ver_artesano.html", data_artesanos=data_artesanos, pagina=pagina, total_paginas=total_paginas, lista_fotos=lista_fotos)

@app.route("/artesano/<int:id>")
def artesano_unico(id):
    artesano = db.get_artesano(id)

    if artesano == None:
        msg = "Artesano no encontrado"
        return render_template("auth/index.html", msg=msg)
    
    lista_fotos = []
    for foto in db.get_fotos(id):
        lista_fotos.append(f"uploads/{foto[1]}")

    telefono = ""
    if artesano[5] == '':
        telefono = "No disponible"
    else:
        telefono = artesano[5]


    descripcion = ""
    if artesano[2] == '':
        descripcion = "No disponible"
    else:
        descripcion = artesano[2]

    tipos = []
    tipos_str = ""
    for tipo in db.get_tipos(id):
        tipos.append(tipo[0])
    if len(tipos) == 1:
        tipos_str = "%s" % tipos[0]
    elif len(tipos) == 2:
        tipos_str = "%s, %s" % (tipos[0], tipos[1])
    elif len(tipos) == 3:
        tipos_str = "%s, %s, %s" % (tipos[0], tipos[1], tipos[2])

    artesano_id = {
        "nombre": artesano[3],
        "region": db.get_region(artesano[1])[0],
        "comuna": db.get_comuna(artesano[1])[0],
        "tipos": tipos_str,
        "descripcion": descripcion,
        "email": artesano[4],
        "telefono": telefono,
        "fotos": lista_fotos 
    }
    return render_template("form/artesano.html", artesano=artesano_id)

#######################################################################################
#-------------------------------------HINCHAS------------------------------------------
#######################################################################################

@app.route('/hincha-register', methods=['GET', 'POST'])
def hincha_register():
    if request.method == 'POST':
        deportes = request.form.getlist("deportes")
        nombre = request.form.get("h-username")
        comuna = request.form.get("h-comuna")
        region = request.form.get("h-region")
        transporte = request.form.get("transporte")
        email = request.form.get("h-email")
        celular = request.form.get("h-number")
        comentarios = request.form.get("h-comments")

        msg = ""
        validacion, msg = validarH(nombre, email, celular, comuna, region, transporte, deportes, comentarios)

        if validacion:
            if comentarios == None: comentarios = ""
            status_hincha, msg = db.registrar_hincha(comuna, comentarios, nombre, email, celular, transporte)  ##definir funcion
            if status_hincha:
                hincha_id = db.get_hincha_id(nombre)
                for deporte in deportes:
                    tipo_id = db.get_deportes_id(deporte)
                    status_deporte = db.registrar_deporte_hincha(hincha_id, tipo_id)
            if status_hincha and status_deporte:
                msg = "Hincha registrado exitosamente"
                return render_template("auth/index.html", msg=msg)

        return render_template("form/hincha_register.html", error=msg)
    
    return render_template("form/hincha_register.html")

@app.route('/lista-hincha', methods=['GET', 'POST'])
def ver_hinchas():
    if db.get_total_hinchas() == 0:                             
        return render_template("form/ver_hincha.html")
    else:
        pagina = request.args.get("pagina",1,type=int)
        tamaño_pagina = 5
        offset = (pagina - 1) * tamaño_pagina
        total_hinchas = db.get_total_hinchas()
        total_paginas = math.ceil(total_hinchas[0] / tamaño_pagina)

        data_hinchas = []
        for hincha in db.get_hinchas(tamaño_pagina, offset):
            id, comuna_id, transporte, nombre, _, celular, _ = hincha       ##revisar esto segun la db
            comuna = db.get_comuna(comuna_id)
            if celular == '': celular = "No disponible"
            deportes = []
            deportes_str = ""
            for dep in db.get_deportes(id):
                deportes.append(dep[0])
            if len(deportes) == 1:
                deportes_str = "%s" % deportes[0]
            elif len(deportes) == 2:
                deportes_str = "%s, %s" % (deportes[0], deportes[1])
            elif len(deportes) == 3:
                deportes_str = "%s, %s, %s" % (deportes[0], deportes[1], deportes[2])
            
            data_hinchas.append({
                    "nombre": nombre,
                    "comuna": comuna[0],
                    "deportes": deportes_str,
                    "transporte": transporte,
                    "telefono": celular,
                    "id": id
                })
    return render_template("form/ver_hincha.html", data_hinchas=data_hinchas, pagina=pagina, total_paginas=total_paginas)


@app.route("/hincha/<int:id>")
def hincha_unico(id):
    hincha = db.get_hincha(id)

    if hincha == None:
        msg = "Hincha no encontrado"
        return render_template("auth/index.html", msg=msg)

    telefono = ""
    if hincha[5] == '':
        telefono = "No disponible"
    else:
        telefono = hincha[5]

    deportes = []
    deportes_str = ""
    for dep in db.get_deportes(id):
        deportes.append(dep[0])
    if len(deportes) == 1:
        deportes_str = "%s" % deportes[0]
    elif len(deportes) == 2:
        deportes_str = "%s, %s" % (deportes[0], deportes[1])
    elif len(deportes) == 3:
        deportes_str = "%s, %s, %s" % (deportes[0], deportes[1], deportes[2])

    hincha_id = {
        "nombre": hincha[3],
        "region": db.get_region(hincha[1])[0],
        "comuna": db.get_comuna(hincha[1])[0],
        "deportes": deportes_str,
        "comentario": hincha[2],
        "email": hincha[4],
        "telefono": telefono
    }
    return render_template("form/hincha.html", hincha=hincha_id)

#######################################################################################
#-------------------------------------GRAFICOS-----------------------------------------
#######################################################################################

@app.route("/stats", methods=["GET"])
def stats():
    return render_template("stats/stats.html")

@app.route("/stats/hinchas", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def get_stats_hinchas():
    #obtener informacion (total de hinchas por deporte)
    cant_deportes = db.get_hinchas_por_deporte()
    #formatear la informacion
    data = []
    for deporte in cant_deportes:
        data.append({
            "name": deporte[0],
            "y": deporte[1]
        })
    
    return jsonify(data)

@app.route("/stats/artesanos", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def get_stats_artesanos():
    #obtener informacion (total de hinchas por deporte)
    cant_artesanos = db.get_artesanos_por_tipo()
    #formatear la informacion
    data = []
    for tipo in cant_artesanos:
        data.append({
            "name": tipo[0],
            "y": tipo[1]
        })
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)