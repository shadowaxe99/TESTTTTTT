```python
from flask import Flask, render_template, request
import user_interface_integration as ui
import real_time_data_integration as rtdi

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/itemSelection', methods=['POST'])
def item_selection():
    user_input = request.form['itemSelectionInput']
    item_selection_result = ui.integrate_UI(user_input)
    return render_template('index.html', item_selection_result=item_selection_result)

@app.route('/updateData', methods=['GET'])
def update_data():
    rtdi.integrate_data()
    return render_template('index.html', update_message="Data updated successfully.")

if __name__ == '__main__':
    app.run(debug=True)
```
This code assumes that there is an 'index.html' file in a 'templates' directory in the same directory as this script. The 'index.html' file should contain form elements with the names 'itemSelectionInput' for user input on item selection. The 'updateData' route can be triggered to update the data used by the AI agent.