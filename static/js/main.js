```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const dashboard = document.getElementById('dashboard');
    const itemSelection = document.getElementById('item-selection');

    loginForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const username = event.target.elements.username.value;
        const password = event.target.elements.password.value;
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.message === 'login_success') {
                window.location.href = '/dashboard';
            } else {
                alert('Login failed. Please try again.');
            }
        });
    });

    registerForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const username = event.target.elements.username.value;
        const password = event.target.elements.password.value;
        fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.message === 'register_success') {
                window.location.href = '/login';
            } else {
                alert('Registration failed. Please try again.');
            }
        });
    });

    itemSelection.addEventListener('submit', (event) => {
        event.preventDefault();
        const instructions = event.target.elements.instructions.value;
        fetch('/select_items', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ instructions }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.message === 'item_selection_success') {
                dashboard.innerHTML = '';
                data.selected_items.forEach(item => {
                    const itemElement = document.createElement('div');
                    itemElement.textContent = item;
                    dashboard.appendChild(itemElement);
                });
            } else {
                alert('Item selection failed. Please try again.');
            }
        });
    });
});
```