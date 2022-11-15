import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd

conn = snowflake.connector.connect(
    user="sunilmakwana",
    password="Azl@886628",
    account="wk99799.central-india.azure",
    warehouse="DEV_WH",
    database="ACCOUNT",
    schema="DEV"
)
cur = conn.cursor()
cur.execute('USE ROLE ACCOUNTADMIN')
df = pd.read_csv('C:/Snowflake/Publibike_Fahrten.csv', sep=',')
cur.execute('USE DATABASE ACCOUNT')
cur.execute('USE SCHEMA DEV')
write_pandas(conn, df, table_name="PUBLIBIKE_FAHRTEN")
cur.close()
