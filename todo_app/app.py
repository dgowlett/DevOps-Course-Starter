from flask import Flask, request, redirect, render_template, url_for

from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item, delete_item, completed_item, not_started_item
from todo_app.data.view_model import ViewModel

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config())


    @app.route('/')
    def index():
        items = get_items(app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])
        view_model = ViewModel(items)
        return render_template('index.html', view_model = view_model)

        #return render_template('index.html', items = items)

        
    
    @app.route('/additem', methods=['GET','POST'])
    def addnewtodo():
        newtodo= request.form.get('new_item')
        if newtodo != '':
            add_item(newtodo,app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])
            return redirect('/')

    @app.route('/cards/<id>/completed', methods=['GET','POST'])
    def completed(id):
        #newtodo= request.form.get('completed_item')
        #if newtodo != '':
        completed_item(id,app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])

        return redirect('/')

    @app.route('/cards/<id>/not_started', methods=['GET','POST'])
    def not_started(id):
        #newtodo= request.form.get('completed_item')
        #if newtodo != '':
        not_started_item(id,app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])   
    
        return redirect('/')

    @app.route('/cards/<id>/delete', methods=['GET','POST'])
    def delete(id):
        #newtodo= request.form.get('completed_item')
        #if newtodo != '':
        #    print("id equels ",id)
        delete_item(id,app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])
        return redirect('/')

    redirect('/')
    return app