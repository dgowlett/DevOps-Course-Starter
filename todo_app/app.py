from flask import Flask, request, redirect, render_template, url_for

from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item, delete_item, completed_item, not_started_item
from todo_app.data.view_model import ViewModel

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items = get_items()
        view_model = ViewModel(items)
        return render_template('index.html', view_model = view_model)        
    
    @app.route('/additem', methods=['POST'])
    def addnewtodo():
        newtodo= request.form.get('new_item')
        if newtodo != '':
            add_item(newtodo)
            return redirect('/')

    @app.route('/cards/<id>/completed')
    def completed(id):
        completed_item(id)
        return redirect('/')

    @app.route('/cards/<id>/not_started')
    def not_started(id):  
        not_started_item(id)   
        return redirect('/')

    @app.route('/cards/<id>/delete')
    def delete(id):
        delete_item(id)
        return redirect('/')

    redirect('/')
    return app