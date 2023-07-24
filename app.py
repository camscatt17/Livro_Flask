# O arquivo app.py é responsável por conter a inicialização das propriedades da ferramenta Flask, banco de dados e, além disso, as rotas do projeto
# As rotas recebem as requisições e através das controllers se comunicam com as models 

# -*- coding: utf-8 -*-
from flask import Flask
from flask import request, redirect, render_template
from flask_cors import CORS

# config import
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from model.model_class import createTables

# Controllers
from controller.User import UserController

# Admin
from admin.Admin import start_views

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
    start_views(app, db)
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
        return "Aqui entrará a tela de login!"
    
    ##########################################################################################################
    @app.route('/login/', methods=['POST'])
    def loginPost():
        user = UserController()
        
        email = request.form['email']
        password = request.form['password']
        
        result = user.login(email, password)
        
        if result:
            return redirect('/admin')
        else:
            return render_template('logn.html', data={'status':401, 'msg':'Dados de usuário incorretos', 'type': None})
    
    ##########################################################################################################
    @app.route('/recuperarSenha/')
    def recuperarSenha():
        return "Aqui entrará a tela de recuperar senha"
    
    ##########################################################################################################
    @app.route('/recuperarSenha/', methods=['POST'])
    def sendRecuperarSenha():
        user = UserController()
        
        result = user.recorvery(request.form['email'])
        
        if result:
            return render_template('recovery.html', data={'status':200, 'msg':'E-mail de recuperação enviado com sucesso!'})
        else:
            return render_template('recovey.html', data={'status': 401, 'msg':'Erro ao enviar e-mail de recuperaçã'})
            
    ##########################################################################################################
    @app.route('/profile/<int:id>/action/<action>/')
    def profile(id):
       pass
            
    return app