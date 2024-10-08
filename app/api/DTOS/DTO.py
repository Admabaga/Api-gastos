# El objetivo del DTo es responderle a un cliente con unos datos específicos

from pydantic import BaseModel, Field
from datetime import date

class UsuarioDTOPeticion(BaseModel): #En petición se piden todos losdatos
    nombre:str
    edad:int
    telefono:str
    correo:str
    contraseña:str
    fechaRegistro:date
    ciudad:str
    class Config:
        orm_mode=True

class UsuarioDTORespuesta(BaseModel): #En respuesta se muestran los necesarios
    id:int
    nombre:str
    telefono:str
    ciudad:str
    class Config:
        orm_mode=True

class GastoDTOPeticion(BaseModel):
    monto:int
    fecha:date
    descripcion:str
    nombre:str
    class Config:
        orm_mode=True

class GastoDTORespuesta(BaseModel):
    fecha:date
    monto:int
    descripcion:str
    nombre:str
    class Config:
        orm_mode=True

class CategoriaDTOPeticion(BaseModel):
    nombreCategoria:str
    fotoIcono:str
    class Config:
        orm_mode=True

class CategoriaDTORespuesta(BaseModel):
    nombreCategoria:str
    fotoIcono:str
    class Config:
        orm_mode=True

class MetodoPagoDTOPeticion(BaseModel):
    nombreMetodo:str
    valor:int
    descripcion:str
    class Config:
        orm_mode=True

class MetodoPagoDTORespuesta(BaseModel):
    nombreMetodo:str
    valor:int
    descripcion:str
    class Config:
        orm_mode=True

