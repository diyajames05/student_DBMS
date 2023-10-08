## STUDENT DBMS
## Author Diya Sojan 12-A
## 08/10/23

import mysql.connector
import dbcreate
import signup
import login
import register
import update
import search 
import questions
import random_stu
from prettytable import from_db_cursor
import test 
import display_results

def conduct_test(db):
    cursor=db.cursor()
    print('Welcome, please enter the grade of the student who wants to take the test')
    clas=int(input('enter the class the student is in'))
    q1='''SELECT scholarship_id, student_id, 
        student.name 
        FROM scholarship 
        INNER JOIN student 
        ON scholarship.student_id=student.stu_id 
        WHERE student.class=%s;''' % (clas)
    cursor.execute(q1)
    print('The following students are eligible for scholarship from class',clas)
    table=from_db_cursor(cursor)
    print(table)
    student=input('enter the scholarship id of the student who needs to take the test')
    q2='SELECT scholarship_id FROM scholarship WHERE scholarship_id=%s' % (student)
    cursor.execute(q2)
    x=cursor.fetchone()
    if x==None:
        print('Invalid id')
    else:
        test.test_for_scholarshipid(db,student)




def loggedin(db):
    while True:
        print('-------------------------')
        print('what would you like to do? ')
        print('1-Register a Student')
        print('2-Update student data')
        print('3-Search student data')
        print('4- Add Question to the scholarship test')
        print('5- Randomly generate scholarship list')
        print('6- View the students selected for scholarship')
        print('7- Take scholarship Test')
        print('8- View scholarship results')
        print('X- Exit')
        choice=input('Enter your choice: ')
        if choice=='1':
            register.register(db)

        elif choice=='2':
            update.update(db)
        
        elif choice=='3':
            search.search(db)

        elif choice=='4':
            questions.questionanswer(db)
        
        elif choice=='5':
            random_stu.insert_scholarship_students(db)
        
        elif choice=='6':
            random_stu.view_scholarship_students(db)
        
        elif choice=='7':
            conduct_test(db)
        
        elif choice=='8':
            display_results.display(db)

        
        elif choice.upper()=='X':
            print('Thank you, exiting')
            break

    



#program
if __name__ == "__main__":
    db= mysql.connector.connect(host='localhost',user='diya',password='1234',database='project')
    dbcreate.create_table(db)
    print('WELCOME!!!')
    print('What do you want to do?')
    while True:
        print('1-Signup')
        print('2-Login')
        print('X-Exit')
        print('-------------------------')
        choice=input('Enter your choice: ')
        if choice=='1':
            signup.signup(db)
        elif choice=='2':
            if login.login(db) is True:
                loggedin(db)
                
            else:
                continue

        elif choice.upper()=='X':
            print('Thank you, exiting')
            break
        else:
            print('Input a valid choice')


    







