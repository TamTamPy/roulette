#!/usr/bin/python
import psycopg2
from config import config

try:
    conn = psycopg2.connect("dbname='roulette' user='tamtam' host='localhost' password='p@ssw0rd'")
except:
    print("I am unable to connect to the database")

def create_table(table_name):
    with conn.cursor() as curs:

        print(f'Creating table {table_name}')
        curs.execute(f"""
                CREATE TABLE {table_name} (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """)

def insert_info(table_name, person):
    with conn.cursor() as curs:

        print(f'inserting {person} into {table_name}')
        curs.execute(f"""
                INSERT INTO {table_name} ( name ) VALUES ( '{person}')
                
                """)


#INSERT INTO postgresqldotorg ( page_name ) VALUES ( 'psycopg2_tutorial' )"

def show_everything():
    with conn.cursor() as curs:
        print('Showing Everything')
        curs.execute(f"""
                    SELECT * FROM test
                """)
        everything = curs.fetchall()
        print(f"{everything}")




if __name__ == '__main__':
    create_table('test')
    insert_info('test', 'Christian' )
    show_everything()
