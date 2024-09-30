from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine



connectionToDataBase = 'jdbc:sqlserver://adrian-123456.database.windows.net:1433;database=ControlGastos;user=adrian-admin@adrian-123456;password=Duhast2379497;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;'

engine = create_engine(connectionToDataBase)

sessionLocal = sessionmaker(autocommit = false, autoflush = false, bind = engine)