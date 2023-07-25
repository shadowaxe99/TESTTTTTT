```python
from flask import Flask, render_template, request, redirect, url_for, flash
from src.data_collection_preprocessing import collect_data, preprocess_data
from src.machine_learning_models import train_model
from src.decision_making_item_selection import select_items
from src.real_time_data_integration import update_data
from src.user_interface import login, register, display_dashboard

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login(username, password):
            flash('login_success')
            return redirect(url_for('dashboard'))
        else:
            flash('login_failure')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register_route():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if register(username, password):
            flash('register_success')
            return redirect(url_for('login'))
        else:
            flash('register_failure')
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    selected_items = display_dashboard()
    return render_template('dashboard.html', items=selected_items)

@app.route('/update_data')
def update_data_route():
    update_data()
    flash('data_updated')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    data = collect_data()
    data = preprocess_data(data)
    model = train_model(data)
    selected_items = select_items(model, data)
    app.run(debug=True)
```