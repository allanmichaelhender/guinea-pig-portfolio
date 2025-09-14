import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE FTSE_data (
            date DATE PRIMARY KEY NOT NULL,
            open NUMERIC(20,2) NOT NULL,
            high NUMERIC(20,2) NOT NULL,
            low NUMERIC(20,2) NOT NULL,
            close NUMERIC(20,2) NOT NULL,
            volume BIGINT NOT NULL,
            change NUMERIC(20,2) NOT NULL,
            changePercent NUMERIC(10,8)
        )
        """,
        """
        CREATE TABLE SNP500_data (
            date DATE PRIMARY KEY NOT NULL,
            open NUMERIC(20,2) NOT NULL,
            high NUMERIC(20,2) NOT NULL,
            low NUMERIC(20,2) NOT NULL,
            close NUMERIC(20,2) NOT NULL,
            volume BIGINT NOT NULL,
            change NUMERIC(20,2) NOT NULL,
            changePercent NUMERIC(10,8)
        )
        """
)
    try:
        config = load_config()
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                # execute the CREATE TABLE statement
                for command in commands:
                    cursor.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()