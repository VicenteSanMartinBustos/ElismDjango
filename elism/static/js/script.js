$(document).ready(function() {
    $('#contactForm').on('submit', function(event) {
        event.preventDefault(); // Evita el envío del formulario por defecto

        // Limpia mensajes de error y clases de validación
        $('.invalid-feedback').text('');
        $('.form-control').removeClass('is-invalid');

        // Obtén los valores de los campos
        var name = $('#name').val().trim();
        var email = $('#email').val().trim();
        var message = $('#message').val().trim();

        var isValid = true;

        // Validación del campo de nombre
        if (name === '') {
            $('#nameError').text('El nombre es obligatorio.');
            $('#name').addClass('is-invalid');
            isValid = false;
        }

        // Validación del campo de correo electrónico
        var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email === '') {
            $('#emailError').text('El correo electrónico es obligatorio.');
            $('#email').addClass('is-invalid');
            isValid = false;
        } else if (!emailPattern.test(email)) {
            $('#emailError').text('El formato del correo electrónico es inválido.');
            $('#email').addClass('is-invalid');
            isValid = false;
        }

        // Validación del campo de mensaje
        if (message === '') {
            $('#messageError').text('El mensaje es obligatorio.');
            $('#message').addClass('is-invalid');
            isValid = false;
        }

        // Si el formulario es válido, realiza el envío
        if (isValid) {
            var formData = $(this).serialize(); // Obtiene todos los datos del formulario en un formato URL-encoded

            $.ajax({
                url: '/guardar_contacto/', // Ruta a la vista en Django
                type: 'POST',
                data: formData,
                success: function(response) {
                    if (response.status === 'success') {
                        alert(response.message);
                        $('#contactForm')[0].reset(); // Limpia el formulario
                    } else {
                        alert('Error al enviar el formulario.');
                    }
                },
                error: function(xhr, status, error) {
                    alert('Error en la solicitud.');
                }
            });
        }
    });
});
