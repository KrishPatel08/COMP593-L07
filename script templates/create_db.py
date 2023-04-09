"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import inspect
from faker import Faker
from datetime import datetime
import sqlite3
import random



def main():

    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():

    """Creates the people table in the database"""
    
    con = sqlite3.connect(db_path)

    cur = con.cursor()

    create_people_table_query = """
    CREATE TABLE IF NOT EXISTS people
    (
    id         INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    email      TEXT NOT NULL,
    address    TEXT NOT NULL,
    city       TEXT NOT NULL,
    province   TEXT NOT NULL,
    bio        TEXT,
    age        INTEGER,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
    );
    """
    cur.execute(create_people_table_query)
   
    con.commit()
   
    con.close()
           
    

def populate_people_table():

    """Populates the people table with 200 fake people"""
    
    con = sqlite3.connect(db_path)

    cur = con.cursor()

    fake = Faker()
    
    add_people_query = """
    INSERT INTO people
    (
    name,
    email,
    address,
    city,
    province,
    bio,
    age,
    created_at,
    updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    for _ in range(200):

        new_people = (fake.name(),
                    fake.ascii_company_email(),
                    fake.street_address(),
                    fake.city(),
                    fake.country(),
                    fake.text(),
                    random.randint(1, 100),
                    datetime.now(),
                    datetime.now())
   
        cur.execute(add_people_query, new_people)

    con.commit()
    
    con.close()
    
def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()