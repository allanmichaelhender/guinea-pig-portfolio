import psycopg2
from data import FTSE_data, SNP500_data, NIKKEI225_data
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")


def insert_data(data,index):
    sql = f"INSERT INTO {index}_data(date,open,high,low,close,volume,change,changePercent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (date) DO NOTHING"
    try:
        with  psycopg2.connect(database_url) as connection:
            with  connection.cursor() as cursor:
                cursor.executemany(sql, data)
            connection.commit()
    except Exception as error:
        print(error)
        

if __name__ == '__main__':
    insert_data(FTSE_data,'FTSE')
    insert_data(SNP500_data,'SNP500')
    insert_data(NIKKEI225_data,'NIKKEI225')

