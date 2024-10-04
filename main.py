from fastapi import FastAPI
from app.api.entitys.Entitys import Usuario, Base
from app.database.config import engine
from app.api.routes.Routes import routes
from starlette.responses import RedirectResponse

#Activar ORM
Base.metadata.create_all(bind = engine)

#Activar api
app=FastAPI()

@app.get("/")
def main():
    return RedirectResponse(url="/docs")
app.include_router(routes)