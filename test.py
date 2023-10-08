## STUDENT DBMS
## Author Diya Sojan 12-A
## 08/10/23
import mysql.connector
from prettytable import from_db_cursor

def list_questions(db):
    cursor=db.cursor()
    q1='SELECT q_no FROM question ORDER BY rand() LIMIT 5;'       
    cursor.execute(q1)
    q_no=cursor.fetchall()
    return q_no

def test_for_scholarshipid(db,scholarship_id):
    cursor=db.cursor()
    print('Each correct answer carries 2 points, there are 5 questions in all')
    score=0
    q_no= list_questions(db)
    for i in q_no:
        q2='SELECT answer FROM question WHERE q_no= %s' % (i)
        cursor.execute(q2)
        ans=cursor.fetchone()
        q3='SELECT question,A,B,C,D FROM question WHERE q_no= %s ;' % (i)
        cursor.execute(q3)
        table=from_db_cursor(cursor)
        print(table)
        input_ans=input('Enter the correct choice (A,B,C or D)')
        if input_ans.upper()== ans[0]:
            score+=2
            print('Correct!', 'Your current score is', score,'/10')
    print('Your final score is',score)
    q4='UPDATE scholarship SET score=%s WHERE scholarship_id=%s' % (score,scholarship_id)
    cursor.execute(q4)
    db.commit()
    q5='SELECT student_id from scholarship WHERE scholarship_id=%s ' % (scholarship_id)
    cursor.execute(q5)
    id=cursor.fetchone()
    q6='SELECT fees FROM student WHERE stu_id=%s'% (id[0])
    cursor.execute(q6)
    d=cursor.fetchone()
    og_fee=d[0]
    new_fee=0
    if score==2:
        new_fee=og_fee-(2/100*og_fee)
    elif score==4:
        new_fee=og_fee-(4/100*og_fee)
    elif score==6:
        new_fee=og_fee-(6/100*og_fee)
    elif score==8:
        new_fee=og_fee-(8/100*og_fee)
    elif score==10:
        new_fee=og_fee-(10/100*og_fee)
    elif score==0:
        new_fee=og_fee-(1/100*og_fee)
    q7='UPDATE scholarship SET reduced_fee=%s'%(new_fee)
    cursor.execute(q7)
    db.commit()


    


























if __name__ == "__main__":
    import mysql.connector
    db= mysql.connector.connect(host='localhost',user='diya',password='1234',database='project')
    conduct_test(db)