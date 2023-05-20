## Este arquivo será o responsável por dizer ao Python em que ambiente nosso projeto estará rodando, se ele estará em produção, 
#  teste ou desenvolvimento. Isso é necessário porque cada aambiente tem uma configuração diferente.

import os
import random, string

## Superclasse Config, cujas constantes são herdadas pelas subclasses
class Config(object):
    CSRF_ENABLED = True # Habilita o uso de criptografia em sessões do Flask
    SECRET = 'ysb_92=qe#djf8%ng+a*#4rt#5%3*4k5%i2bck*gn@w3@f&-&' # Será usada em alguns momentos para criar chaves e valores criptografados
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates') # Caminho do local em que os arquivos de template do projeto ficarão
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # Caminho do local em que a raiz do projeto se encontra
    APP = None # Constante que receberá a propriedade do app. Inicia com valor nulo.


## Inicialmente, tem-se três subclasses pois precisa-se rodar o projeto em três ambientes diferentes.
# Ambiente de desenvolvimento
class DevelopmentConfig(Config):
    TESTING = True # Constante que habilita o ambiente de teste no Flask
    DEBUG = True # Habilita ou não os debugs que o Python exibe no console de execução
    IP_HOST = 'localhost' # Constante que indica qual o IP da máquina em que estamos rodando o projeto
    PORT_HOST = 8000 # A porta da aplicação é algo fundamental para que a aplicação rode
    URL_MAIN = 'http://%s:%s/'	%	(IP_HOST,	PORT_HOST) # Constante que une o endereço de IP com a porta para gerar o endereço principal da sua aplicação

# Ambiente de teste
class TestingConfig(Config):
    TESTING = True 
    DEBUG = True 
    IP_HOST = 'localhost' 
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/'	%	(IP_HOST,	PORT_HOST) 

# Ambiente de Produção
class ProductionConfig(Config):
    TESTING = True 
    DEBUG = True 
    IP_HOST = 'localhost' 
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/'	%	(IP_HOST,	PORT_HOST) 

# Possui as três subclasses dentro de si e será usado para dizer ao projeto qual das três vamos usar
app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

# Receberá um dos três valores: development, testing ou production, que será atribuido através de uma variável de ambiente
app_active = os.getenv('FLASK_ENV')