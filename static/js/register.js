document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('signup-form');

    form.addEventListener('submit', function(event) {
        const username = form.querySelector('input[name="username"]');
        const email = form.querySelector('input[name="email"]');
        const password1 = form.querySelector('input[name="password1"]');
        const password2 = form.querySelector('input[name="password2"]');
        let valid = true;

        
        form.querySelectorAll('.error-message').forEach(el => el.remove());

        if (username.value.length < 4) {
            showError(username, "Username must be at least 4 characters long");
            valid = false;
        }

        if (!validateEmail(email.value)) {
            showError(email, "Enter a valid email address");
            valid = false;
        }

        if (password1.value.length < 8) {
            showError(password1, "Password must be at least 8 characters long");
            valid = false;
        }

        if (password1.value !== password2.value) {
            showError(password2, "Passwords do not match");
            valid = false;
        }

        if (!valid) {
            event.preventDefault(); 
        }
    });

    function showError(input, message) {
        const error = document.createElement('div');
        error.classList.add('error-message');
        error.style.color = 'red';
        error.innerText = message;
        input.parentNode.insertBefore(error, input.nextSibling);
    }

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    
    const showPasswordCheckbox = document.getElementById('show-password-checkbox');
    showPasswordCheckbox.addEventListener('change', function() {
        const password1 = document.getElementById('id_password1');
        const password2 = document.getElementById('id_password2');
        if (showPasswordCheckbox.checked) {
            password1.type = "text";
            password2.type = "text";
        } else {
            password1.type = "password";
            password2.type = "password";
        }
    });
});
