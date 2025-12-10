from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos.modelos import Base


url_db = "sqlite:///sistema.db" 

motor_db = create_engine(url_db, echo=False)
Base.metadata.create_all(motor_db)

Session = sessionmaker(bind=motor_db)
sesion = Session()