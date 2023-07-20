# O arquivo app.py é responsável por conter a inicialização das propriedades da ferramenta Flask, banco de dados e, além disso, as rotas do projeto

# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS

# config import
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from model.model_class import createTables

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    CORS(app)

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(config.APP, engine_options={"echo":True})
    db.init_app(app)

    ########################################################################
    @app.route('/')
    def index():
        return 'Hello World!'
    
    ########################################################################
    @app.route('/createTables/')
    def createTables():
        createTables(engine=db.engine, session=db.session)
        return "Tabelas criadas!"
    
    return app