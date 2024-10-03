document.addEventListener("DOMContentLoaded", function() {
    const showPasswordCheckbox = document.getElementById('show-password-checkbox');
    const passwordField = document.getElementById('id_password');

    showPasswordCheckbox.addEventListener('change', function() {
        if (showPasswordCheckbox.checked) {
            passwordField.type = "text";
        } else {
            passwordField.type = "password";
        }
    });
});
