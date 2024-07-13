// popover-script.js
document.addEventListener('DOMContentLoaded', function () {
    // Event listener para el botón "Inscripciones mensuales"
    document.getElementById('queryMonthBtn').addEventListener('click', async function (event) {
        event.preventDefault(); // Evitar el redireccionamiento

        try {
            const url = this.getAttribute('data-url');
            const response = await fetch(url);
            const data = await response.json(); // Parsear la respuesta como JSON

            // Mostrar el popover con el contenido obtenido
            $(this).popover({
                content: JSON.stringify(data), // Ajusta la lógica según el formato de tus datos
                html: true,
            });
            $(this).popover('show'); // Mostrar el popover
        } catch (error) {
            console.error('Error al obtener los datos:', error);
            // Manejar errores o mostrar un mensaje de error en el popover
        }
    });

    // Event listener para el botón "Total Deuda"
    document.getElementById('queryTotalDueBtn').addEventListener('click', async function (event) {
        event.preventDefault(); // Evitar el redireccionamiento

        try {
            const url = this.getAttribute('data-url');
            const response = await fetch(url);
            const data = await response.json(); // Parsear la respuesta como JSON

            // Mostrar el popover con el contenido obtenido
            $(this).popover({
                content: JSON.stringify(data), // Ajusta la lógica según el formato de tus datos
                html: true,
            });
            $(this).popover('show'); // Mostrar el popover
        } catch (error) {
            console.error('Error al obtener los datos:', error);
            // Manejar errores o mostrar un mensaje de error en el popover
        }
    });
});
