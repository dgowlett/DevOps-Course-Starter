from flask import Flask, request, redirect, render_template

from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item

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
    option = request.form['To Do List']
    print("Option =["+option+"]")


    if request.form.get('Action 1') == 'Started':
        print('Started Card')
    elif request.form.get('Action 2') == 'Not Started':
        print('Not Started Card')
    elif request.form.get('Action 3') == 'Completed':
        print('Completed')
    elif request.form.get('Action 4') == 'delete':
        print('delete')
    #newtodo= request.form.get('new_item')
    #if newtodo != '':
    #    add_item(newtodo,app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])
    #    print (app.config["BOARD_ID"])
    return redirect('/')





