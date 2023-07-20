# O migrate é um arquivo separado, sendo que ele não será executado com o projeto, mas apenas para realizar modificações na estrutura do banco de dados.
# Todas as vezes em que uma nova model for criada, a estrutura dela deverá ser replicada abaixo das tabelas já adicionadas ao migrate e, se uma tabela
# for modificada, a classe que representa essa tabela também deverá ser modificada e um novo migrate deverá ser rodado.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import app_active, app_config

from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text, DateTime, Boolean, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

config = app_config[app_active]
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return f'<Categoria(id={self.id}, nome={self.name}, descricao={self.description})>'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
class Product(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    description = Column(String(500), nullable=False)
    qtd = Column(Integer, nullable=True, default=0)
    image = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    date_created = Column(DateTime(6), server_default=func.current_timestamp(), nullable=False)
    last_update = Column(DateTime(6), onupdate=func.current_timestamp(), nullable=False)
    status = Column(Integer, default=1, nullable=True)
    user_created: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    category: Mapped[int] = mapped_column(ForeignKey("categoria.id"), nullable=False)

    def __repr__(self):
        return f'<Produto(id={self.id}, nome={self.name}, descricao={self.description}, quantidade={self.qtd}, image={self.image}, preco={self.price}, data_created={self.date_created}, last_update={self.last_update}, status={self.status}, user_created={self.user_created}, category={self.category})>'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(40), unique=True, nullable=False)

    def __repr__(self):
        return f'<Role(id={self.id}, nome={self.name})>'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
class User(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    date_created = Column(DateTime(6), server_default=func.current_timestamp(), nullable=False)
    last_update = Column(DateTime(6), onupdate=func.current_timestamp(), nullable=True)
    recovery_code = Column(Boolean, default=1, nullable=True)
    role: Mapped[int] = mapped_column(ForeignKey("role.id"), nullable=False)

    def __repr__(self):
        return f'<Usuario(id={self.id}, username={self.username}, email={self.email}, password={self.password}, data_created={self.date_created}, last_update={self.last_update}, recovery_code={self.recovery_code}, role={self.role})>'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
if __name__ == '__main__':
    manager.run() 

