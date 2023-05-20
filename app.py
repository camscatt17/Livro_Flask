## Responsável por conter a inicialização das propriedades da ferramenta Flask, banco de dados e além disso, as rotas do projeto.
# O arquivo app.py é o segundo arquivo que será chamado no momento do run. 
# Ele distribuirá as tarefas que cada parte do sistema deverá realizar, inicializando cada parte do projeto.

# -*- coding: utf-8 -*-
from flask import Flask

# config.py import
from config import app_config, app_active

config = app_config[app_active]


## Irá ser utilizada no arquivo run.py para iniciar a aplicação com todas as configurações que estão dentro dela
def create_app(config_name):
    # Receberá a instância do objeto Flask que faz com que todo o sistema funcione baseado nas configurações que o Flask possui.
    app = Flask(__name__, template_folder='templates') 

    # Essas próximas três linhas possuem as configurações da aplicação
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py') # Dizemos que config.py é o arquivo de configuração

    @app.route('/')
    def index():
        return 'Alo Camila!'
    # Retorna-se a variável app contendo o objeto da classe Flask instanciado lá em cima com todas as configurações realizadas e prontas
    return app