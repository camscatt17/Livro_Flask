from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text, DateTime, Boolean, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from passlib.hash import pbkdf2_sha256 

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
    funcao=relationship(Role)

    def __repr__(self):
        return f'<Usuario(id={self.id}, username={self.username}, email={self.email}, password={self.password}, data_created={self.date_created}, last_update={self.last_update}, recovery_code={self.recovery_code}, role={self.role})>'
    
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
    usuario=relationship(User)
    categoria=relationship(Category)

    def __repr__(self):
        return f'<Produto(id={self.id}, nome={self.name}, descricao={self.description}, quantidade={self.qtd}, image={self.image}, preco={self.price}, data_created={self.date_created}, last_update={self.last_update}, status={self.status}, user_created={self.user_created}, category={self.category})>'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns} 

class QueriesUser():
    @staticmethod
    def get_user_by_mail(self):
        """_summary_
        """
        return ''
    
    @staticmethod
    def get_user_by_id(self):
        """_summary_
        """
        return ''
    
    @staticmethod
    def hash_password(self, password):
        try:
            return pbkdf2_sha256.hash(password)
        except Exception as e:
            print("Erro ao criptografar senha %s" %e)
            
    @staticmethod
    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)
        
    @staticmethod
    def verify_password(self, password_no_hash, password_database):
        try:
            return pbkdf2_sha256.verify(password_no_hash, password_database)
        except ValueError:
            return False

def createTables(engine, session=None):
    Base.metadata.create_all(engine, checkfirst=True)
    return True   
