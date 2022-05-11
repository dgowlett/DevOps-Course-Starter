from flask import Flask, request, redirect, render_template

from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item, delete_item, completed_item, not_started_item

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
        add_item(newtodo,app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])
        print (app.config["BOARD_ID"])
    return redirect('/')

@app.route('/itemaction', methods=['POST'])
def actiontodo():

    if 'To Do List' in request.form:
        Selected_item = request.form['To Do List']
        if request.form.get('Action 1') == 'Not Started':
            not_started_item(Selected_item,app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])            
        elif request.form.get('Action 2') == 'Completed':
            completed_item(Selected_item,app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])
        elif request.form.get('Action 3') == 'delete':
            delete_item(Selected_item,app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])

    return redirect('/')

