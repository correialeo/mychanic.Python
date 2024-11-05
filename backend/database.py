from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models import Base

engine = create_engine('sqlite:///problemas_veiculares.db')
Session = sessionmaker(bind=engine)
session = Session()

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)
