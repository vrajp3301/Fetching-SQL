### RAW CONNECTION TO DATABASE
import mysql.connector

## ESTABLISHING THE CONNECTION
connection = mysql.connector.connect(
    user="",
    password="",
    host="",
    database="",
    ssl_disabled=True
)
cursor = connection.cursor()

## INSERTING THE QUERY
query=""""""

cursor.execute(query)

## STORING THE RESULTS
results = []
for i,data in enumerate(cursor):
    results.append(data)

## CLOSING THE CONNECTION
cursor.close()
connection.close()

df_from_sql = pd.DataFrame(results)

### USING SQLALCHEMY
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# print('sqlalchemy version',sqlalchemy.__version__)

## Connection String

connection_string = '' 
engine_create = create_engine(connection_string)

## Insert Query
query = """"""

## Using pandas to convert SQL to Dataframe
df = pd.read_sql(query,engine_create)