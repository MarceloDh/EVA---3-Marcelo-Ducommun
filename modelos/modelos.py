from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False) 

    def __str__(self):
        return f"Usuario: {self.username}"  
    

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True) 
    userId = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    
    comentarios = relationship("Comentario", back_populates="post", cascade="all, delete-orphan")

class Comentario(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True) 
    postId = Column(Integer, ForeignKey('posts.id'), nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)

    post = relationship("Post", back_populates="comentarios")