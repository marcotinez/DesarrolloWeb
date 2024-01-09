// Mostrar el modal al cargar la página
document.addEventListener("DOMContentLoaded", function() {
    mostrarModal();
    
    // Ocultar el modal después de 3 segundos (3000 milisegundos)
    setTimeout(function() {
        cerrarModal();
    }, 3000);
});

// Función para mostrar el modal
function mostrarModal() {
    document.getElementById("myModal").style.display = "block";
}

// Función para cerrar el modal
function cerrarModal() {
    document.getElementById("myModal").style.display = "none";
}
