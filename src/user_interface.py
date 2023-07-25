```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from src import decision_making_item_selection as dm
from src import utils
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

users = []

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        for user in users:
            if user.username == username:
                if check_password_hash(user.password, password):
                    login_user(user)
                    flash('login_success')
                    return redirect(url_for('dashboard'))
                else:
                    flash('Incorrect password.')
                    return redirect(url_for('login'))
        flash('Username does not exist.')
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = generate_password_hash(request.form.get('password'))

        new_user = User(id=len(users)+1, username=username, password=password)
        users.append(new_user)

        flash('register_success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        instructions = request.form.get('instructions')
        selected_items = dm.select_items(instructions)
        flash('item_selection_success')
        return render_template('dashboard.html', selected_items=selected_items)

    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```