# script.py
import sys
import sqlite3

with sqlite3.connect('pyclass.db') as conn:
    c = conn.cursor()

    values = sys.argv[1:3]

    insert_statement = """
    insert into users(username, fav_color) values (?, ?);
    """
    c.execute(insert_statement, values)
