import mysql.connector
from prettytable import from_db_cursor

def display(db):
    cursor=db.cursor()
    q1='SELECT * FROM scholarship WHERE score IS NOT NULL;'
    cursor.execute(q1)
    table=from_db_cursor(cursor)
    print('The results of the scholarship tests are:')
    print(table)
    print('WELL DONE!!!')