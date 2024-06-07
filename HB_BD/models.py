from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresas'
    empresa_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    ubicacion = Column(String)
    industria = Column(String)
    codigo_postal = Column(String)
    representante = Column(String)
    numero_contacto = Column(String)

    ofertas = relationship('Oferta', back_populates='empresa')

class Oferta(Base):
    __tablename__ = 'ofertas'
    oferta_id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    tipo_empleo = Column(String)
    salario = Column(Float)
    empresa_id = Column(Integer, ForeignKey('empresas.empresa_id'))

    empresa = relationship('Empresa', back_populates='ofertas')

class Candidato(Base):
    __tablename__ = 'candidatos'
    candidato_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    correo_electronico = Column(String, nullable=False, unique=True)
    nivel_experiencia = Column(String)

class Aplicacion(Base):
    __tablename__ = 'aplicaciones'
    aplicacion_id = Column(Integer, primary_key=True, autoincrement=True)
    candidato_id = Column(Integer, ForeignKey('candidatos.candidato_id'))
    oferta_id = Column(Integer, ForeignKey('ofertas.oferta_id'))
    fecha_aplicacion = Column(Date)

    candidato = relationship('Candidato')
    oferta = relationship('Oferta')

# Configuración de la base de datos (SQLite en este caso)
engine = create_engine('sqlite:///empleos_ciencia_datos.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
