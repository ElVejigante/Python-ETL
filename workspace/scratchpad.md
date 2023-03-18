# Extract, Transform and Load

Import libraries

def methodX():
    code here
    pass
def methodY():
    code here
    pass
def main():
    methodX()
    methodY()

# SQLAlchemy engines

-Engine:
--Starting point of SQLAlchemy applications
--Allows interaction with the database
--from sqlalchemy import create_engine--

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine([database+dialect]://[username:password]@[database_url:port]/[database_name])

create_engine("postgresql+psycopg2://dcstudent:S3cretPassw0rd@localhost:5432/campdata-prod")

session = Session(engine)

Columns and types

from sqlalchemy import Column, Integer, String

class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer)
    title = Column(String(55))
    description = Column(String(55))
    