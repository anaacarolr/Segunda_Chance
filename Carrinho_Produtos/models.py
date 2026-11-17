from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, ForeignKey, Float
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine("sqlite:///produtos.sqlite3")

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(Integer)
    imagem = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    categoria = Column(String(255), nullable=False)
    avaliacao = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)

    def save(self):
        try:
            db_session.add(self)
            db_session.commit()
        except SQLAlchemyError:
            db_session.rollback()
            raise

    def serialize(self):
        dados={
            "id": self.id,
            "nome": self.nome,
            "categoria": self.categoria,
            "avaliacao": self.avaliacao,
            "preco": self.preco,
            "estoque": self.estoque,
        }
        return dados

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_produto = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    avaliacao = Column(Integer, nullable=False)
    comentario = Column(String, nullable=False)
    data = Column(String, nullable=False)
    review_nome = Column(String, nullable=False)
    review_email = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)