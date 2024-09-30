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

class UsuarioDTORespuesta(): #En respuesta se muestran los necesarios
    id:int
    nombre:str
    telefono:str
    ciudad:str
    class Config:
        orm_mode=True

class GastoDTOPeticion():
    monto:int
    fecha:date
    descripcion:str
    nombre:str
    class Config:
        orm_mode=True

class GastoDTORespuesta():
    fecha:date
    descripcion:str
    nombre:str
    class Config:
        orm_mode=True

class CategoriaDTOPeticion():
    nombreCategoria:str
    fotoIcono:str
    class Config:
        orm_mode=True

class CategoriaDTORespuesta():
    nombreCategoria:str
    fotoIcono:str
    class Config:
        orm_mode=True

class MetodoPagoDTOPeticion():
    nombre:str
    valor:int
    descripcion:str
    class Config:
        orm_mode=True

class MetodoPagoDTORespuesta():
    nombre:str
    valor:int
    descripcion:str
    class Config:
        orm_mode=True

class facturadeoDTOPeticion():
    numeroTransaccion:int
    valor:int
    descripcion:str
    class Config:
        orm_mode=True

class facturadeoDTORespuesta():
    valor:int
    descripcion:str
    class Config:
        orm_mode=True