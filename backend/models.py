from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProblemaVeicular(Base):
    __tablename__ = 'problemas_veiculares'

    id = Column(Integer, primary_key=True, autoincrement=True)
    problema = Column(String, nullable=False)
    sintoma = Column(String, nullable=False)
    causa = Column(String, nullable=False)
    solucao = Column(String, nullable=False)

    def __repr__(self):
        return f"<ProblemaVeicular(id={self.id}, problema='{self.problema}')>"
