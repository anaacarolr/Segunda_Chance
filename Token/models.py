from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, func
from sqlalchemy.orm import sessionmaker, declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()
engine = create_engine('sqlite:///database.db')
SessionLocalExemplo = sessionmaker(bind=engine)


class UsuarioExemplo(Base):
    __tablename__ = 'usuarios_exemplo'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha_hash = Column(String, nullable=False)
    papel = Column(String, default="usuario")

    def set_senha_hash(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_passoword_hash(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def serializar(self):
        dados={
            "id":self.id,
            "nome":self.nome,
            "email":self.email,
            "papel":self.papel,
        }
        return dados

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(DateTime, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    cargo = Column(String, nullable=False)
    salario = Column(Float, nullable=False)
    criado_em = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f'<Funcionario {self.nome}>'

    def set_password(self, password):
        self.senha = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha, password)

class NotasExemplo(Base):
    __tablename__ = 'notas_exemplo'
    id = Column(Integer, primary_key=True)
    conteudo = Column(String, nullable=False)
    # user_id = Column(Integer, ForeignKey('usuarios_exemplo.id')) # Poderia ter para associar

Base.metadata.create_all(engine)  # Cria as tabelas