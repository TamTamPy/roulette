#!/usr/bin/python
import psycopg2
from config import config

try:
    conn = psycopg2.connect("dbname='roulette' user='tamtam' host='localhost' password='p@ssw0rd'")
except:
    print("I am unable to connect to the database")

def create_table(table_name):
    with conn.cursor() as curs:
        try:
            curs = conn.cursor()
            print(f'Creating table {table_name}')
            curs.execute(f"""
                    CREATE TABLE {table_name} (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                    """)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

def show_everything():
    try:
        print('Showing Everything')
        cur.execute(f"""
                    SHOW * FROM roulette
                """)
        everything = cur.fetchall()
        print(f"{everything}")
    except:
        print("Some error")
        cur.close()

def disconnect():
    cur = conn.cursor()
    cur.close()

if __name__ == '__main__':

    create_table('test')
    #show_everything()
    #disconnect()