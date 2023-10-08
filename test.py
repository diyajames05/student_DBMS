import mysql.connector
from prettytable import from_db_cursor

def test(db):
    cursor=db.cursor()
    print('Each correct answer carries 2 points, there are 5 questions in all')
    score=0
    for i in range(5):
        q1='SELECT q_no FROM question ORDER BY rand() LIMIT 1;'       ##QUESTIONs get repeated, table empty :(
        cursor.execute(q1)
        no=cursor.fetchone()
        print('number',no)
        q2='SELECT answer FROM question WHERE q_no= %s' % (no)
        cursor.execute(q2)
        ans=cursor.fetchone()
        print('ans',ans)

        q3='SELECT question,A,B,C,D FROM question WHERE q_no= %s ORDER BY rand() LIMIT 1;' % (no)
        cursor.execute(q3)
        data=cursor.fetchone()
        db.commit()
        print(data)
        table=from_db_cursor(cursor)
        print(table)
        input_ans=input('Enter the correct choice (A,B,C or D)')
        if input_ans== ans[0]:
            score+=2
            print('Correct!')
            print('Next question')
    print('Your score is',score)





    # for i in range(5):
    #     q1='SELECT question,A,B,C,D FROM question ORDER BY rand() LIMIT 1;'
    #     cursor.execute(q1)
    #     data=cursor.fetchone()
    #     table=from_db_cursor(cursor)
    #     print(table)
    #     print(data)
    #     # ans=input('Enter the correct choice (A,B,C or D)')
    #     # q2='SELECT * FROM question '
    #     ##########HELPP######


if __name__ == "__main__":
    import mysql.connector
    db= mysql.connector.connect(host='localhost',user='diya',password='1234',database='project')
    test(db)