from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

databaseName = "gestionbd"

userName = "root"

userPassword = ""
port = "3306"
serverConnection = "localhost"

connectionToDataBase = f'mysql+mysqlconnector://{userName}:{userPassword}@{serverConnection}:{port}/{databaseName}'

# connectionToDataBase = 'jdbc:sqlserver://adrian-123456.database.windows.net:1433;database=ControlGastos;user=adrian-admin@adrian-123456;password=Duhast2379497;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;'

engine = create_engine(connectionToDataBase)

sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)