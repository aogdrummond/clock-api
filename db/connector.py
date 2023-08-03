import os
import psycopg2
import logging
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

logger = logging.getLogger()
logger.setLevel("INFO")

mydb = psycopg2.connect(host=os.environ.get("DB_HOST"),port=os.environ.get("DB_PORT"),dbname=os.environ.get("DB_NAME"),user=os.environ.get("DB_USER"),password=os.environ.get("DB_PASSWORD"))
cursor = mydb.cursor()  
class dB_Cursor:

    def __init__(self) -> None:

        self.cursor = cursor

    def persist_result(self,results,request_address):
        angle = results["angle"]
        hours = results["hours"]
        minutes = results["minutes"]
        query = self.create_query_to_insert(angle,hours,minutes,request_address)
        try:
            self.cursor.execute(query)

            logger.info("Operation persisted succesfully.")
        except:
            logger.warning("Failed on persisting the operation.")
        
    def create_query_to_insert(self,angle:int,hours:int,minutes:int,request_address:str)->str:

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO requests_archive (angle, clock, request_address, requested_at) "
        query+=f"VALUES ({angle}, ARRAY[{hours},{minutes}],'{request_address}','{current_datetime}');"
        
        return query


    def commit(self):

        mydb.commit()

    def close(self):

        mydb.close()

    def query_to_create_table(self,table_name):

        query = f"CREATE TABLE {table_name}("
        query+= "id SERIAL PRIMARY KEY,"
        query+= "angle INTEGER,"
        query+= "date_time TIMESTAMP);"
        return query


