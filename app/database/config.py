from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine


connectionToDataBase="mysql+mysqlconnector://root:""@localhost:3306/gestionbd"

engine = create_engine(connectionToDataBase)

sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)