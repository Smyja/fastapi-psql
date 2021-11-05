from typing import  Any
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://postgres:Akpobi101$@localhost/fastapi",echo=True)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

@as_declarative()
class Base:
    id:Any