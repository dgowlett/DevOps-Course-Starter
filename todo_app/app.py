from flask import Flask, request, redirect, render_template

from todo_app.flask_config import Config
from todo_app.data.session_items import add_item
from todo_app.data.trello_items import get_items

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items(app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])
    return render_template('index.html', items=items)
    
@app.route('/additem', methods=['POST'])
def addnewtodo():
    newtodo= request.form.get('new_item')
    if newtodo != '':
        add_item(newtodo)
        print (app.config["BOARD_ID"])
    return redirect('/')


