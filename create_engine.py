#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import  create_engine

# Connecting to MySQL server at localhost using PyMySQL DBAPI
engine = create_engine("mysql+mysqldb://root:pass@23.92.23.113/mydb")
engine.connect()

print(engine)
