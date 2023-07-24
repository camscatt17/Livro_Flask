# O arquivo app.py é responsável por conter a inicialização das propriedades da ferramenta Flask, banco de dados e, além disso, as rotas do projeto
# As rotas recebem as requisições e através das controllers se comunicam com as models 

# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
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

    # Será dentro da def de uma rota que acionaremos a controller para realizar as ações necessárias dessa rota
    ###########################################################################################################
    @app.route('/')
    def index():
        return 'Hello World!'
    
    ##########################################################################################################
    @app.route('/criarTabelas/')
    def criarTabelas():
        createTables(engine=db.engine, session=db.session)
        return "Tabelas criadas!"
    
    ##########################################################################################################
    @app.route('/login/')
    def login():
        return "Aqui entrará a tela de login"
    
    ##########################################################################################################
    @app.route('/recuperarSenha/')
    def recuperarSenha():
        return "Aqui entrará a tela de recuperar senha"
    
    ##########################################################################################################
    @app.route('/profile/<int:id>/action/<action>/')
    def profile(id):
        if action == 'action1':
            return 'Ação action1 usuário de ID %d' %id
        elif action == 'action2':
            return 'Ação action2 usuário de ID %d' %id
        elif action == 'action3':
            return 'Ação action3 usuário de ID %d' %id
        
    ##########################################################################################################
    @app.route('/profile', methods=['POST'])
    def createProfile():
        username = request.form['username']
        password = request.form['password']
        
        return 'Essa rota possui um método POST e criará um usuário com os dados de usuários %s e senha %s' %(username, password)
    
    ##########################################################################################################
    @app.route('/profile/<int:id>', methods=['PUT'])
    def editTotalProfile(id):
        username = request.form['username']
        password = request.form['password']
        
        return 'Essa rota possui um método PUT e editará o nome do usuário para %s e a senha %s' %(username, password)
            
    return app