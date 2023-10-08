import mysql.connector
from prettytable import from_db_cursor

def test(db):
    cursor=db.cursor()
    print('Each correct answer carries 2 points, there are 5 questions in all')
    score=0
    for i in range(5):
        q1='SELECT question,A,B,C,D FROM question ORDER BY rand() LIMIT 1;'
        cursor.execute(q1)
        table=from_db_cursor(cursor)
        print(table)
        ans=input('Enter the correct choice (A,B,C or D)')
        q2='SELECT * FROM question '
        ##########HELPP######


if __name__ == "__main__":
    import mysql.connector
    db= mysql.connector.connect(host='localhost',user='diya',password='1234',database='project')
    test(db)