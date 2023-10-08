## STUDENT DBMS
## Author Diya Sojan 12-A
## 08/10/23
import mysql.connector
import random
from prettytable import PrettyTable
from prettytable import from_db_cursor

def random_5_student_from(db,clas):
    cursor=db.cursor()
    q1='SELECT stu_id FROM student WHERE class=%s ORDER BY rand() LIMIT 5;' % (clas)
    cursor.execute(q1)
    data=cursor.fetchall()
    return data

def insert_scholarship_students_for_class(db,clas):
    cursor=db.cursor()
    students=random_5_student_from(db,clas)
    for student in students:
        q1='INSERT INTO scholarship (student_id) VALUES (%s) '% (student)
        cursor.execute(q1)
        db.commit()

def insert_scholarship_students(db):
    cursor=db.cursor()
    try:
        for i in range(1,13):
            insert_scholarship_students_for_class(db,i)

    except Exception:
        print('Error, unable to select scholarship students! (ALREADY DONE )')


def view_scholarship_students(db):
    cursor=db.cursor()
    for i in range(1,13):
        print('for class',i,'these student IDs have been selected: ')
        q2='''SELECT student_id, 
        student.name 
        FROM scholarship 
        INNER JOIN student 
        ON scholarship.student_id=student.stu_id 
        WHERE student.class=%s;''' % (i) 
        cursor.execute(q2)
        table=from_db_cursor(cursor)
        print(table)





















if __name__ == "__main__":
    import mysql.connector
    db= mysql.connector.connect(host='localhost',user='diya',password='1234',database='project')
    insert_scholarship_students(db)