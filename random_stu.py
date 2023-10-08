import mysql.connector
import random

def random_5_student_from(db,clas):
    cursor=db.cursor()
    q1='SELECT stu_id FROM student WHERE class=%s ORDER BY rand() LIMIT 5;' % (clas)
    cursor.execute(q1)
    data=cursor.fetchall()
    return data

def select_scholarship_students_for_class(db,clas):
    cursor=db.cursor()
    students=random_5_student_from(db,clas)
    for student in students:
        q1='INSERT INTO scholarship (student_id) VALUES (%s) '% (student)
        cursor.execute(q1)
        db.commit()

def select_scholarship_students(db):
    for i in range(1,13):
        select_scholarship_students_for_class(db,i)























if __name__ == "__main__":
    import mysql.connector
    db= mysql.connector.connect(host='localhost',user='diya',password='1234',database='project')
    select_scholarship_students(db)