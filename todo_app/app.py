from flask import Flask, request, redirect, render_template, url_for

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
    return redirect('/')

@app.route('/cards/<int:id>/completed', methods=['GET','POST'])
def completed(id):
    newtodo= request.form.get('completed_item')
    if newtodo != '':
        completed_item(id,app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])

    return redirect('/')

@app.route('/cards/<int:id>/not_started', methods=['GET','POST'])
def not_started(id):
    newtodo= request.form.get('completed_item')
    if newtodo != '':
        not_started_item(id,app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])   
    
    return redirect('/')


@app.route('/cards/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    newtodo= request.form.get('completed_item')
    if newtodo != '':
        delete_item(id,app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])
    return redirect('/')


# END OF NEW




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

