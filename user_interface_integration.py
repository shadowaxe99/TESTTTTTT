```python
from flask import Flask, render_template, request
import decision_making_item_selection as dm
import natural_language_understanding as nlu

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/item_selection', methods=['POST'])
def item_selection():
    user_input = request.form['itemSelectionInput']
    interpreted_input = nlu.understand_language(user_input)
    selected_items = dm.make_decision(interpreted_input)
    return render_template('item_selection.html', selected_items=selected_items)

@app.route('/action_monitor')
def action_monitor():
    actions = dm.get_actions()
    return render_template('action_monitor.html', actions=actions)

@app.route('/update_display')
def update_display():
    updates = dm.get_updates()
    return render_template('update_display.html', updates=updates)

if __name__ == '__main__':
    app.run(debug=True)
```