# -*- coding: utf-8 -*-
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from model.model_class import Role, User, Category, Product

def start_views(app, db):    
    # Momento do código em que chamamos o método construtor do Admin, que será responsável pelas configurações básicas do sistema
    admin = Admin(app, name='Meu Estoque', template_mode='bootstrap3')
    
    admin.add_view(ModelView(Role, db.session, "Funções", category="Usuários"))
    admin.add_view(ModelView(User, db.session, "Usuários", category="Usuários"))
    admin.add_view(ModelView(Category, db.session, "Categoria", category="Produtos"))
    admin.add_view(ModelView(Product, db.session, "Produtos", category="Produtos"))
    