//Funcionamiento de los selectores de regiones y comunas.alle San Esteban

//Diccionario de comunas sacado de esta pagina https://codepen.io/emingo/pen/aEwRNb
const comunasPorRegion = {
    None: ["---"],
    "Región Arica y Parinacota": ["---","Arica", "Camarones", "Putre", "General Lagos"],
    "Región de Tarapacá": ["---","Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"],
    "Región de Antofagasta": ["---","Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollague", "San Pedro Atacama", "Tocopilla", "Maria Elena"],
    "Región de Atacama": ["---","Copiapo", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"],
    "Región de Coquimbo": ["---","La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paihuano", "Vicuña", "Illapel", "Los Vilos", "Salamanca", "Ovalle", "Combarbala", "Monte Patria", "Punitaqui", "Rio Hurtado"],
    "Región de Valparaíso": ["---","Valparaiso", "Casablanca", "Concon", "Juan Fernandez", "Puchuncavi", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "La Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llay Llay", "Panquehue", "Putaendo", "Santa Maria", "Quilpue", "Limache", "Olmue", "Villa Alemana"],
    "Región Metropolitana de Santiago": ["---","Cerrillos", "Cerro Navia", "Conchali", "El Bosque", "Estacion Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipu", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolen", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "Santiago", "San Joaquin", "San Miguel", "San Ramon", "Vitacura", "Puente Alto", "Pirque", "San Jose de Maipo", "Colina", "Lampa", "Tiltil", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhue", "Curacavi", "Maria Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"],
    "Región del Libertador Bernardo Ohiggins": ["---","Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machali", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta Tilcoco", "Rengo", "Requinoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchigue", "Navidad", "Paredones", "San Fernando", "Chepica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"],
    "Región del Maule": ["---","Talca", "Constitucion", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Rio Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curico", "Hualañe", "Licanten", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquen", "Linares", "Colbun", "Longavi", "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas"],
    "Región de Ñuble": ["---","Cobquecura", "Coelemu", "Ninhue", "Portezuelo", "Quirihue", "Ranquil", "Trehuaco", "Bulnes", "Chillan Viejo", "Chillan", "El Carmen", "Pemuco", "Pinto", "Quillon", "San Ignacio", "Yungay", "Coihueco", "Ñiquen", "San Carlos", "San Fabian", "San Nicolas"],
    "Región del Biobío": ["---","Concepcion", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tome", "Hualpen", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Alamos", "Tirua", "Los Angeles", "Antuco", "Cabrero", "Laja", "Mulchen", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Barbara", "Tucapel", "Yumbel", "Alto Bio Bio"],
    "Región de la Araucanía": ["---","Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquen", "Pucon", "Puerto Saavedra", "Teodoro Schmidt", "Tolten", "Vilcun", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautin", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Puren", "Renaico", "Traiguen", "Victoria"],
    "Región de Los Ríos": ["---","Valdivia", "Corral", "Lanco", "Los Lagos", "Mafil", "Mariquina", "Paillaco", "Panguipulli", "La Union", "Futrono", "Lago Ranco", "Rio Bueno"],
    "Región de Los Lagos": ["---","Puerto Montt", "Calbuco", "Cochamo", "Fresia", "Frutillar", "Los Muermos", "Llanquihue", "Maullin", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Velez", "Dalcahue", "Puqueldon", "Queilen", "Quellon", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Rio Negro", "San Juan", "San Pablo", "Chaiten", "Futaleufu", "Hualaihue", "Palena"],
    "Región Aisén del General Carlos Ibáñez del Campo": ["---","Coyhaique", "Lago Verde", "Aysen", "Cisnes", "Guaitecas", "Cochrane", "O'Higins", "Tortel", "Chile Chico", "Rio Ibañez"],
    "Región de Magallanes y la Antártica Chilena": ["---","Punta Arenas", "Laguna Blanca", "Rio Verde", "San Gregorio", "Antartica", "Porvenir", "Primavera", "Timaukel", "Puerto Natales", "Torres del Paine"]
};

document.getElementById("regiones").addEventListener('change', function() {
    var regionSeleccionada = this.value;
    var comunas = comunasPorRegion[regionSeleccionada];
  
    // Limpia las opciones existentes
    var selectComunas = document.getElementById('comunas');
    selectComunas.innerHTML = '';
  
    // Añade las nuevas opciones
    for (var i = 0; i < comunas.length; i++) {
      var nuevaOpcion = document.createElement('option');
      nuevaOpcion.text = comunas[i];
      nuevaOpcion.value = comunas[i];
      selectComunas.add(nuevaOpcion);
    }
  });
  
//validación del formulario de hinchas

//verificador comentarios generales y descripcion artesanias.
const validadorGeneral = (input) => {
    let valido = false;
    //en caso de mensaje vacio.
    if (input.length == 0) {
        valido = true;
    }
    //en caso de mensaje con contenido.
    if (input && input.length >= 3 && input.length < 80) {
        valido = true;
    }
    return valido;
}

//validador de mail, que cumpla el formato.
const validadorMail = (mail) => {
    let valido = false;
    let re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/; //Expresión regular.
    if (mail && mail.length > 10 && re.test(mail)) {
        valido = true;
    }
    return valido;
}

//validador de nombres, aseguramos que no hayan numeros.
const validadorNombre = (input) => {
    let valido = false;
    const regexNumbers = /\d/;
    const soloEspacios = /^\s*$/.test(input);
    if (input && input.length > 3 && input.length < 80 && !regexNumbers.test(input) && !soloEspacios) {
        valido = true;
    }
    return valido;
}

//validador de numero de telefono.
const validadorTelefono = (number) => {
    let valido = false;
    const re = /^\+56[1-9]\d{8}$/; //Expresión regular.
    if (number.length == 0)  {
        valido = true;
    }
    if (number && re.test(number)) {
        valido = true;
    }
    return valido;
}
//valida la seleccion de tipos de artesania
const validarTipo = (lista) => {
    let valido = false;
    if (lista.length > 0 && lista.length < 4) {
        valido = true;
    }
    return valido;
}

//validador cantidad de fotos.
const validarFotos = (lista) => {
    let valido = false;
    if (lista.files.length > 0 && lista.files.length < 4) {
        valido = true;
    }
    return valido;
}

const validarFormArtesanos = () => {
    console.log("Enviando..."); // imprimir en consola

    // obtener elementos del DOM por el ID
    let email_artesano = document.getElementById("email");
    let nombre_artesano = document.getElementById("username");
    let numero_artesano = document.getElementById("number");
    let descripcion_artesano = document.getElementById("descripcion");
    let tipos_artesano = document.getElementById("tipo");
    let region_artesano = document.getElementById("regiones");
    let comuna_artesano = document.getElementById("comunas");
    let fotos_artesano = document.getElementById("fotos");

    let msg = "";

    //validador de nombre
    if (!validadorNombre(nombre_artesano.value)) {
        msg += "Nombre invalido.\n";
        nombre_artesano.style.borderColor = "red";
    } else {
        nombre_artesano.style.borderColor = "";
    }

    //validador de region.
    if (region_artesano.value === '') {
        msg += "Debe seleccionar una región.\n";
        region_artesano.style.borderColor = "red";
    } else {
        region_artesano.style.borderColor = "";
    }

    //validador de comuna.
    if (comuna_artesano.value === '' || comuna_artesano.value === '---') {
        msg += "Debe seleccionar una comuna.\n";
        comuna_artesano.style.borderColor = "red";
    } else {
        comuna_artesano.style.borderColor = "";
    }

    //validador de tipos.
    if (!validarTipo(tipos_artesano.selectedOptions)) {
        msg += "Debe seleccionar entre 1 y 3 tipos de artesania.\n";
        tipos_artesano.style.borderColor = "red";
    } else {
        tipos_artesano.style.borderColor = "";
    }
    
    //validador de fotos
    if (!validarFotos(fotos_artesano)) {
        msg += "Debe seleccionar entre 1 y 3 fotos.\n";
        fotos_artesano.style.borderColor = "red";
    } else {
        fotos_artesano.style.borderColor = "";
    }

    //validador de mail
    if (!validadorMail(email_artesano.value)) {
        msg += "Email invalido.\n";
        email_artesano.style.borderColor = "red"; // cambiar estilo con JS!!
    } else {
        email_artesano.style.borderColor = "";
    }
    
    //validador de numero
    if (!validadorTelefono(numero_artesano.value)) {
        msg += "Número Celular invalido.\n";
        numero_artesano.style.borderColor = "red";
    } else {
        numero_artesano.style.borderColor = "";
    }

    //validador de comentarios
    if (!validadorGeneral(descripcion_artesano.value)) {
        msg += "Comentario invalido.\n";
        descripcion_artesano.style.borderColor = "red";
    } else {
        descripcion_artesano.style.borderColor = "";
    }

    if (msg === "") {
        var modal1 = document.getElementById("myModal");
        var modal2 = document.getElementById("myModal2");
        var home = document.getElementById("home");
        var home2 = document.getElementById("home-msg");
        var yes_btn = document.getElementById("confirmar-hincha");
        var no_btn = document.getElementById("cancelar-hincha");

        modal1.style.display = "block";
        
        no_btn.onclick = function() {
            modal1.style.display = "none";
        }
        
        home.onclick = function() {
            window.location.href = "/";
        }

        home2.onclick = function() {
            window.location.href = "/";
        }

        yes_btn.onclick = function() {
            modal1.style.display = "none";
            modal2.style.display = "block";
        }

        window.onclick = function(event) {
            if (event.target == modal1) {
              modal1.style.display = "none";
            }
          }
    }
    else if (msg !== ""){
        alert(msg); // alertas JS
    }
};

document.getElementById("artesano-form").addEventListener("keydown", function(event) {
    if (event.key == "Enter") {
      event.preventDefault();
    }
  });
  
let artesanosBtn = document.getElementById("registro-artesano");
artesanosBtn.addEventListener("click", validarFormArtesanos); // registrar evento 