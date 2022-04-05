from flask import Flask, request, redirect, render_template

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    #print(items)
    return render_template('index.html', items=items)
    
@app.route('/additem', methods=['POST'])
def addnewtodo():
    newtodo= request.form.get('nitem')
    if newtodo != 'Enter ToDo':
        add_item(newtodo)
    return redirect('/')


