# El archivo de rutas nos ayuda a articular la información, a donde va a ir dirigido

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from typing import List
from fastapi.params import Depends
from app.api.DTOS.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta, GastoDTOPeticion, GastoDTORespuesta, CategoriaDTOPeticion, CategoriaDTORespuesta, MetodoPagoDTOPeticion, MetodoPagoDTORespuesta
from app.api.entitys.Entitys import Usuario, Gasto, Categoria, MetodoPago
from app.database.config import sessionLocal, engine

# para que una api funcione debe tener un archivo enrutador
routes = APIRouter()  # Estoe s conocido como ENDPOINTS


# Crear una funcion para establecer cuando yo quiera y necesite conexion hacia la base de datos

def getDataBase():
    basedatos = sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()


# programación de cada uno de los seficios que ofrecerá nuestra api

# y que son los servicio web?, son operaciones en la base de datos, y por lo general se programan basados en un modelo

# registrando o guardando un usuario en la base de datos

@routes.post("/usuarios", response_model=UsuarioDTORespuesta)
def guardarUsuario(datosPeticion: UsuarioDTOPeticion,
                   db: Session = Depends(getDataBase)):  # los : en python establece el tipo de dato
    try:
        usuario = Usuario(
            nombre=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad
        )
        db.add(usuario)  # Agrego la información a la base de datos
        db.commit()  # Guarda y verifica
        db.refresh(usuario)  # y se actualiza
        return usuario  # Me muestra usuario
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail= f"Error al registrar el usuario {error}")


@routes.post("/gastos", response_model=GastoDTORespuesta)
def guardarGasto(datosPeticion: GastoDTOPeticion,
                 db: Session = Depends(getDataBase)):  # los : en python establece el tipo de dato
    try:
        gasto = Gasto(
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            nombre=datosPeticion.nombre,
            usuario_id = datosPeticion.usuarioId
        )
        db.add(gasto)
        db.commit()
        db.refresh(gasto)
        return gasto
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail= f"Error al registrar el gasto {error}")


@routes.post("/categorias", response_model=CategoriaDTORespuesta)
def guardarCategoria(datosPeticion: CategoriaDTOPeticion,
                     db: Session = Depends(getDataBase)):  # los : en python establece el tipo de dato
    try:
        categoria = Categoria(
            nombre=datosPeticion.nombre,
            fotoIcono=datosPeticion.fotoIcono,
        )
        db.add(categoria)  # Agrego la información a la base de datos
        db.commit()  # Guarda y verifica
        db.refresh(categoria)  # y se actualiza
        return categoria  # Me muestra usuario
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail= f"Error al registrar el usuario {error}")


@routes.post("/metodoPagos", response_model=MetodoPagoDTORespuesta)
def guardarCategoria(datosPeticion: MetodoPagoDTOPeticion,
                     db: Session = Depends(getDataBase)):  # los : en python establece el tipo de dato
    try:
        metodoPago = MetodoPago(
            nombreMetodo=datosPeticion.nombreMetodo,
            valor=datosPeticion.valor,
            descripcion = datosPeticion.descripcion
        )
        db.add(metodoPago)  # Agrego la información a la base de datos
        db.commit()  # Guarda y verifica
        db.refresh(metodoPago)  # y se actualiza
        return metodoPago  # Me muestra usuario
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail= f"Error al registrar el metodo de pago {error}")


@routes.get("/usuarios", response_model=List[UsuarioDTORespuesta])
def buscarUsuario(db: Session = Depends(getDataBase)):
    try:
        listadoUsuarios = db.query(Usuario).order_by(asc(Usuario.nombre)).all()
        return listadoUsuarios
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail= f"Error al registrar el usuario {error}")


@routes.get("/gastos", response_model=List[GastoDTORespuesta])
def buscarGasto(db: Session = Depends(getDataBase)):
    try:
        listadoGastos = db.query(Gasto).order_by(desc(Gasto.fecha)).all()
        return listadoGastos
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail= f"Error al registrar el usuario {error}")

@routes.get("/gastos/usuarios/{usuarioId}", response_model=List[GastoDTORespuesta])
def buscarGastosPorUsuario(usuarioId: int, db: Session = Depends(getDataBase)):
    try:
        listadoGastos = db.query(Gasto).filter(Gasto.usuario_id == usuarioId).order_by(desc(Gasto.fecha)).all()
            # if not listadoGastos:
            #     raise HTTPException(status_code=404, detail="No se encontraron gastos para el usuario especificado")
        return listadoGastos
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al buscar los gastos: {error}")


@routes.get("/categorias", response_model=List[CategoriaDTORespuesta])
def buscarCategoria(db: Session = Depends(getDataBase)):
    try:
        listadoCategoria = db.query(Categoria).all()
        return listadoCategoria
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail= f"Error al registrar el usuario {error}")


@routes.get("/metodoPagos", response_model=List[MetodoPagoDTORespuesta])
def buscarMetodoPago(db: Session = Depends(getDataBase)):
    try:
        listadoMetodoPago = db.query(MetodoPago).all()
        return listadoMetodoPago
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail= f"Error al registrar el usuario {error}")







