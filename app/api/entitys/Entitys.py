#Aqui se realizan la creación de las tablas de la base de datos
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(50))
    edad=Column(Integer)
    correo=Column(String(20))
    contraseña=Column(String(60))
    ciudad=Column(String(50))
    fechaRegistro=Column(Date)
    telefono=Column(String(20))


class Gasto(Base):
    __tablename__ = 'gasto'
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Integer)
    fecha=Column(Date)
    descripcion=Column(String(250))
    nombre=Column(String(100))

class Categoria(Base):
    __tablename__ = 'categoria'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(50))
    fotoIcono=Column(String(50))

class MetodoPago(Base):
    __tablename__ = 'MetodoPago'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(50))
    valor=Column(Integer)
    descripcion=Column(String(250))

