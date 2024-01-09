import pymysql

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

# -- conn ---
def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn	

# -- querys --
def anadir_artesano(comuna_id, descripcion, nombre, email, celular):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO artesano (comuna_id, descripcion_artesania, nombre, email, celular) VALUES (%s,%s,%s,%s,%s);", (comuna_id, descripcion, nombre, email, celular))
	conn.commit()

def anadir_tipo_artesano(artesano_id, tipo_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO artesano_tipo (artesano_id, tipo_artesania_id) VALUES (%s,%s);", (artesano_id, tipo_id))
	conn.commit()

def insertar_foto(ruta_archivo, nombre_archivo, artesano_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO foto (ruta_archivo, nombre_archivo, artesano_id) VALUES (%s,%s,%s);", (ruta_archivo, nombre_archivo, artesano_id))
	conn.commit()

def get_comuna_id(nombre_comuna):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id FROM comuna WHERE nombre = %s;", (nombre_comuna))
	comuna_id = cursor.fetchone()
	return comuna_id

def get_artesano_id(nombre_artesano):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id FROM artesano WHERE nombre = %s;", (nombre_artesano))
	artesano_id = cursor.fetchone()
	return artesano_id

def get_tipo_id(nombre_tipo):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id FROM tipo_artesania WHERE nombre = %s;", (nombre_tipo))
	tipo_id = cursor.fetchone()
	return tipo_id

def get_tipos(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT tipo_artesania.nombre FROM artesano_tipo JOIN tipo_artesania ON artesano_tipo.tipo_artesania_id = tipo_artesania.id WHERE artesano_tipo.artesano_id = %s;", (id,))
	tipos = cursor.fetchall()
	return tipos

def get_comuna(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT nombre FROM comuna WHERE id = %s;", (id,))
	comuna = cursor.fetchone()
	return comuna

def get_artesanos(page_size, offset):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM artesano ORDER BY nombre DESC LIMIT %s OFFSET %s;", (page_size, offset))
	artesanos = cursor.fetchall()
	return artesanos

def get_artesano(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM artesano WHERE id = %s;", (id,))
	artesano = cursor.fetchone()
	return artesano

def get_region(comuna_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT r.nombre FROM comuna c, region r WHERE c.id = %s and r.id = c.region_id;", (comuna_id,))
	region_id = cursor.fetchone()
	return region_id

def get_total_artesanos():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT COUNT(*) FROM artesano;")
	total_artesanos = cursor.fetchone()
	return total_artesanos

def get_fotos(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT ruta_archivo, nombre_archivo FROM foto WHERE artesano_id=%s;", (id,))
	fotos = cursor.fetchall()
	return fotos

def get_region_id(nombre_region):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id FROM region WHERE nombre = %s;", (nombre_region,))
	region_id = cursor.fetchone()
	return region_id
####################FUNCIONES NUEVAS##############
def get_hinchas(page_size, offset):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM hincha ORDER BY nombre DESC LIMIT %s OFFSET %s;", (page_size, offset))
	hincha = cursor.fetchall()
	return hincha

def anadir_hincha(comuna_id, comentarios, nombre, email, numero, transporte):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO hincha (comuna_id, modo_transporte, nombre, email, celular, comentarios) VALUES (%s,%s,%s,%s,%s,%s);", (comuna_id, transporte, nombre, email, numero, comentarios))
	conn.commit()

def anadir_deporte_hincha(hincha_id, deporte_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO hincha_deporte (hincha_id, deporte_id) VALUES (%s,%s);", (hincha_id, deporte_id))
	conn.commit()

def get_deportes_id(nombre_deporte):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id FROM deporte WHERE nombre = %s;", (nombre_deporte,))
	deportes = cursor.fetchall()
	return deportes

def get_deportes(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT deporte.nombre FROM hincha_deporte JOIN deporte ON hincha_deporte.deporte_id = deporte.id WHERE hincha_deporte.hincha_id = %s;", (id,))
	deportes = cursor.fetchall()
	return deportes

def get_hincha_id(nombre_hincha):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id FROM hincha WHERE nombre = %s;", (nombre_hincha,))
	hincha_id = cursor.fetchone()
	return hincha_id

def get_hincha(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM hincha WHERE id = %s;", (id,))
	hincha = cursor.fetchone()
	return hincha

def get_total_hinchas():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT COUNT(*) FROM hincha;")
	total_hinchas = cursor.fetchone()
	return total_hinchas


####################REGISTRO######################
# tabla artesano
def registrar_artesano(comuna, descripcion, nombre, email, celular):
	comuna_id = get_comuna_id(comuna)
	if get_artesano_id(nombre) != None:
		return False, "El artesano ya existe."
	else:
		anadir_artesano(comuna_id, descripcion, nombre, email, celular)
		return True, None

#tabla artesano_tipo
def registrar_artesano_tipo(artesano_id, tipo_id):
	anadir_tipo_artesano(artesano_id, tipo_id)
	return True

# tabla foto
def agregar_foto (ruta_archivo, nombre_archivo, artesano_id):
	insertar_foto(ruta_archivo, nombre_archivo, artesano_id)
	return True

def registrar_deporte_hincha(hincha_id, deporte_id):
	anadir_deporte_hincha(hincha_id, deporte_id)
	return True

def registrar_hincha(comuna, comentarios, nombre, email, numero, transporte):
	comuna_id = get_comuna_id(comuna)
	if get_hincha_id(nombre) != None:
		return False, "El hincha ya existe."
	else:
		anadir_hincha(comuna_id, comentarios, nombre, email, numero, transporte)
		return True, None
######################STATS##########################

def get_hinchas_por_deporte():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT deporte.nombre, COUNT(*) FROM hincha_deporte JOIN deporte ON hincha_deporte.deporte_id = deporte.id GROUP BY deporte.nombre;")
	hinchas_por_deporte = cursor.fetchall()
	return hinchas_por_deporte

def get_artesanos_por_tipo():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT tipo_artesania.nombre, COUNT(*) FROM artesano_tipo JOIN tipo_artesania ON artesano_tipo.tipo_artesania_id = tipo_artesania.id GROUP BY tipo_artesania.nombre;")
	artesanos_por_tipo = cursor.fetchall()
	return artesanos_por_tipo
