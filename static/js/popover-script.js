document.addEventListener('DOMContentLoaded', function () {
    var popovers = document.querySelectorAll('[data-bs-toggle="popover"]');
    
    popovers.forEach(function (popover) {
        popover.addEventListener('click', function () {
            var url = popover.getAttribute('data-url');
            
            fetch(url)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.text();
                })
                .then(data => {
                    if (data.trim() === '') {
                        data = 'No se encontró contenido';
                    }
                    
                    // Actualizamos el contenido del popover
                    popover.setAttribute('data-bs-content', data);
                    
                    // Creamos una instancia de Popover de Bootstrap
                    var popoverInstance = new bootstrap.Popover(popover);
                    
                    // Mostramos el popover
                    popoverInstance.show();
                    
                    // Cerramos el popover cuando se hace clic fuera de él
                    document.addEventListener('click', function closePopover(event) {
                        if (!popover.contains(event.target)) {
                            popoverInstance.hide();
                            document.removeEventListener('click', closePopover);
                        }
                    });
                })
                .catch(error => {
                    console.error('Error fetching or displaying data:', error);
                });
        });
    });
});
