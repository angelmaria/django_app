// popover-script.js

document.addEventListener('DOMContentLoaded', function () {
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl, {
            content: function () {
                var url = popoverTriggerEl.getAttribute('data-url');
                return fetch(url)
                    .then(response => response.text())
                    .then(html => {
                        var parser = new DOMParser();
                        var doc = parser.parseFromString(html, 'text/html');
                        return doc.body.innerHTML;
                    });
            },
            html: true,
            placement: 'bottom'
        });
    });
});
