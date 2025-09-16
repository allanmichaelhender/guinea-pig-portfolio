import psycopg2
from config import load_config
from data import FTSE_data, SNP500_data, NIKKEI225_data


def insert_data(data,index):
    """ Insert multiple vendors into the vendors table  """
    sql = f"INSERT INTO {index}_data(date,open,high,low,close,volume,change,changePercent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as connection:
            with  connection.cursor() as cursor:
                # execute the INSERT statement
                cursor.executemany(sql, data)
            # commit the changes to the database
            connection.commit()
    except Exception as error:
        print(error)
        

if __name__ == '__main__':
    insert_data(FTSE_data,'FTSE')
    insert_data(SNP500_data,'SNP500')
    insert_data(NIKKEI225_data,'NIKKEI225')

