from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

dataBaseName = "gestionbd"
userName = "root"   
userPassword = " "
server = "localhost"
conexionPort = "3306"

connectionToDataBase = f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{conexionPort}/{dataBaseName}"

engine = create_engine(connectionToDataBase)

sessionLocal = sessionmaker(autocommit = false, autoflush = false, bind = engine)