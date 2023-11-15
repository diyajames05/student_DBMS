# STUDENT DBMS PROJECT 
# DIYA, SANJANA, SRUJANA 

import mysql.connector
import getpass
import random 
from prettytable import from_db_cursor
from prettytable import from_db_cursor

## TO CREATE TABLES
def create_table(db):
    cursor=db.cursor()
    #LOGIN TABLE
    q1='''CREATE TABLE IF NOT EXISTS login (
        user_name VARCHAR(20) PRIMARY KEY, 
        password VARCHAR(20));'''
    cursor.execute(q1)
    #STUDENT DATA TABLE
    q2='''CREATE TABLE IF NOT EXISTS student (
        stu_id INT PRIMARY KEY AUTO_INCREMENT, 
        name VARCHAR(20) NOT NULL, 
        class VARCHAR(20) NOT NULL, 
        section VARCHAR(10) NOT NULL,
        mname VARCHAR(20) NOT NULL, 
        fname VARCHAR(20) NOT NULL, 
        fees INT NOT NULL,
        is_parent_a_teacher VARCHAR(20),
        parent_experience INT
        );'''
    cursor.execute(q2)
    #SCHOLARSHIP QUESTION TABLE
    q3='''CREATE TABLE IF NOT EXISTS question (
        q_no INT PRIMARY KEY AUTO_INCREMENT, 
        question VARCHAR(200), 
        A VARCHAR(20),
        B VARCHAR(20),
        C VARCHAR(20),
        D VARCHAR(20),
        answer VARCHAR(20)
        );'''
    cursor.execute(q3)

    #SCHOLARSHIP STUDENTS
    ##FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
    q4='''CREATE TABLE IF NOT EXISTS scholarship(
        scholarship_id INT PRIMARY KEY AUTO_INCREMENT,
        student_id INT NOT NULL UNIQUE,
        FOREIGN KEY (student_id) REFERENCES student(stu_id), 
        score INT DEFAULT NULL, 
        reduced_fee INT DEFAULT NULL

    );'''
    cursor.execute(q4)

# TO POPULATE DATA ( NOT PART OF MAIN PROJECT )
def populate_student_data(db):
    cursor=db.cursor()
    student_data = [
        ["A","5","C","FatherA","MotherA","5000"],
        ["B","1","A","FatherS","MotherB","7000"],
        ["C","12","D","FatherD","MotherC","8000"],
        ["D","4","F","FatherQ","MotherD","9000"],
        ["E","7","B","FatherW","MotherE","5900"],
        ["F","9","D","FatherE","MotherF","8000"],
        ["G","11","C","FatherT","MotherG","2000"],
        ["H","10","A","FatherY","MotherH","4000"]
    ]
    for student in student_data:
        q2="INSERT INTO student (name, class, section, mname, fname, fees) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(q2,student)
        
    db.commit()

## TO SIGN UP
def signup(db):
    cursor=db.cursor()
    print('Please enter the following details')
    user_name=input('enter username: ')
    password=getpass.getpass('enter password: ')
    #check if username is not empty
    if user_name!='':
        # check if this username exists
        q3='SELECT user_name FROM login WHERE user_name = %s ;'
        cursor.execute(q3,[user_name])
        res=cursor.fetchall()
        if len(res)!=0:
            print('user_name already exists, try again!')
            return
        q2='INSERT INTO login (user_name, password) VALUES (%s,%s);'
        cursor.execute(q2, [user_name,password])
        print('SUCCESSFULLY SIGNED UP')
        db.commit()
    else:
        print('Invalid username!!!')

## TO LOGIN 
def login(db):
    cursor=db.cursor()
    attemps=3
    while attemps>0:
        user_name=input('Enter username: ')
        q='SELECT user_name FROM login where user_name=%s;'
        cursor.execute(q,[user_name])
        rep=cursor.fetchone()
        if rep==None:
            print('This username does not exist, try to sign up first')
            return False

        else:
            password=getpass.getpass('Enter password: ')
       
        q1='SELECT user_name FROM login WHERE user_name= %s and password= %s ;'
        cursor.execute(q1,[user_name,password])
        res=cursor.fetchone()
        if res!= None:
            print('LOGIN SUCCESSFUL')
            return True
            
            
        else:
            print('INVALID USERNAME OR PASSWORD!!')
            attemps-=1

            if attemps == 0:
                print("You have exceeded the maximum number of login attempts.")
                return False
                  

## TO REGISTER
def register(db):
    cursor=db.cursor()
    print('Please enter the following details')
    name=input('Enter Student Name: ')
    clas=input('Enter class (1 to 12): ')
    section=input('Enter section: ')
    mname=input("Enter Mother's Name: ")
    fname=input("Enter Father's Name: ")
    fees= int(input('Enter total fees: '))
    is_parent_a_teacher= input('Is the parent a teacher? yes or no?')
    
    if is_parent_a_teacher =='yes':
        parent_experience=int(input('Enter the number of years of experience of parent as a teacher'))

    
   

    if is_parent_a_teacher == 'yes':
        print('Since the parent is a teacher, you have a fee reducion of Rs', end= ' ')
        if parent_experience<5:
            print(10/100*fees)
            print('The new fees is', fees-(10/100*fees))
            fees=fees-(10/100*fees)
        elif parent_experience>5 and parent_experience<=10:
            print(20/100*fees)
            print('The new fees is', fees-(20/100*fees))
            fees=fees-(20/100*fees)

        elif parent_experience>10:
            print(30/100*fees)
            print('The new fees is', fees-(30/100*fees))
            fees=fees-(30/100*fees)

        q2="INSERT INTO student (name, class, section, mname, fname, fees, is_parent_a_teacher,parent_experience) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(q2,[name, clas, section, mname, fname, fees,is_parent_a_teacher,parent_experience])
        db.commit()
        print("Student Data entered Successfully!!!")
    else:
        q2="INSERT INTO student (name, class, section, mname, fname, fees, is_parent_a_teacher) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(q2,[name, clas, section, mname, fname, fees,is_parent_a_teacher])
        db.commit()

## TO UPDATE STUDENT DATA
def update(db):
    cursor=db.cursor()
    print('Enter the student id of the student you wish to update the data of')
    stu_id=int(input('Enter stu_id provided on ID card'))
    q1= 'SELECT * FROM student WHERE stu_id = %s;' 
    cursor.execute(q1,[stu_id])
    data=cursor.fetchone()
    print('Original data: ',data)
    print("What do you need to modify?")
    print('1. Name')
    print('2. Father name')
    print('3. Mother name')
    print('4. Class')
    print('5- Section')

    x=int(input('Enter your choice'))
    if x==1:
        name=input("Enter updated name")
        q2="UPDATE student SET name= %s WHERE stu_id=%s;"
        cursor.execute(q2,[name,stu_id])
        db.commit()
        print('UPDATED SUCCESSFULLY')

    elif x==2:
        fname=input("Enter updated father name")
        q3="UPDATE student SET fname= %s WHERE stu_id=%s;"
        cursor.execute(q3,[fname,stu_id])
        db.commit()
        print('UPDATED SUCCESSFULLY')

    elif x==3:
        mname=input("Enter updated Mother name")
        q4="UPDATE student SET mname=%s WHERE stu_id=%s;"
        cursor.execute(q4,[mname,stu_id])
        db.commit()
        print('UPDATED SUCCESSFULLY')

    elif x==4:
        clas=input("Enter updated class")
        q5="UPDATE student SET class= %s WHERE stu_id=%s;"
        cursor.execute(q5,[clas,stu_id])
        db.commit()
        print('UPDATED SUCCESSFULLY')

    elif x==5:
        section=input("Enter updated section")
        q6="UPDATE student SET section= %s WHERE stu_id=%s;"
        cursor.execute(q6,[section,stu_id])
        db.commit()
        print('UPDATED SUCCESSFULLY')
    else:
        print("Nothing to update!")


## TO SEARCH STUDENT DATA
def search(db):
    cursor=db.cursor()
    print("Search student by name, class and section")
    name=input("enter name: ")
    clas=input("enter class: ")
    section=input('enter section: ')
    q1="SELECT * FROM student WHERE name=%s AND class=%s AND section=%s;"
    cursor.execute(q1,[name,clas,section])
    op=cursor.fetchall()
    if len(op) != 0:
        for i in op:
            print(i)
        print('data found successfully')
    else:
        print('No student found, please check the case of the data')

## TO ADD QUESTIONS TO THE TEST
def questionanswer(db):
        cursor=db.cursor()
        while True:
            print("Welcome to Question Portal")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            question = input("Enter the question :")
            A = input("Enter the option A :")
            B = input("Enter the option B :")
            C = input("Enter the option C :")
            D = input("Enter the option D :")
            answer = 'X'
            while answer == 'X':
                op = input("Which option is correct answer? (A,B,C OR D) ")
                if op.upper() == 'A':
                    answer = 'A'
                elif op.upper() == 'B':
                    answer = 'B'
                elif op.upper() == 'C':
                    answer = 'C'
                elif op.upper() == 'D':
                    answer = 'D'
              
                else:
                    print("Please choose a valid option as your answer")
                
            print('you have entered the question', question)
            print('with the options:', A, B, C, D)
            print('and the correct anser given is', answer)
            con=input('Type C to confirm any other key to cancel')
            if con.upper()=='C':
                q1= "INSERT INTO question(question,A,B,C,D,answer) VALUES (%s,%s,%s,%s,%s,%s);"
                cursor.execute(q1,[question, A, B, C, D, answer])
                db.commit()
                ch=input('Question added successfully! Do you want to add more questions? y or n?')
                if ch.upper()=='N':
                    break 
            else:
                print('cancelled')


## TO RANDOMLY GENERATE SCHOLARSHIP LIST ( CAN ONLY BE DONE ONCE! )
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


## TO VIEW SCHOLARSHIP STUDENTS
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


## TO CONDUCT THE TEST

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
    q7='UPDATE scholarship SET reduced_fee=%s WHERE scholarship_id=%s '%(new_fee, scholarship_id)
    cursor.execute(q7)
    db.commit()


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
    
    q0= """ SELECT student.is_parent_a_teacher
            FROM student
            JOIN scholarship ON student.stu_id = scholarship.student_id
            WHERE scholarship.scholarship_id = %s;""" % (student)
    cursor.execute(q0)
    res=cursor.fetchone()
    if res[0]=='yes':
        print('Since the parent is already a teacher, there is already a fee ruduction. Depending on how much you score, you will be granted a concessionThe fee reduction after the scholarship test will be added to this')

    else:
        print('The is no prior fee redcution, depending on how much you score, you will be granted a concession')
    q2='SELECT scholarship_id FROM scholarship WHERE scholarship_id=%s' % (student)
    cursor.execute(q2)
    x=cursor.fetchone()
    if x==None:
        print('Invalid id')
    else:
        test_for_scholarshipid(db,student)

## TO VIEW SCHOLARSHIP RESULTS
def display(db):
    cursor=db.cursor()
    q1='SELECT * FROM scholarship WHERE score IS NOT NULL;'
    cursor.execute(q1)
    table=from_db_cursor(cursor)
    print('The results of the scholarship tests are:')
    print(table)
    print('WELL DONE!!!')

## TO VIEW ALL STUDENT DATA
def viewdata(db):
    q= 'SELECT * FROM student;'
    cursor=db.cursor()
    cursor.execute(q)
    table=from_db_cursor(cursor)
    print(table)





    ## MAIN 
def loggedin(db):
    print('-------------------------')
    print('Please select your role:')
    print('A- Admin')
    print('B- Student')
    role=input('Enter your option: ')

    if role.lower()=='a': 
        
        while True:

            print('-------------------------')
            print('what would you like to do? ')
            print('1-Register a Student')
            print('2-Update student data')
            print('3-Search student data')
            print('4- Add Question to the scholarship test')
            print('5- Randomly generate scholarship list')
            print('9- View all the student data' )
            print('X- Exit')
            choice=input('Enter your choice: ')
            if choice=='1':
                register(db)

            elif choice=='2':
                update(db)
                
            elif choice=='3':
                search(db)

            elif choice=='4':
                questionanswer(db)
                
            elif choice=='5':
                insert_scholarship_students(db)
            elif choice=='9':
                viewdata(db)
            elif choice.upper()=='X':
                print('Thank you, exiting')
                break

    elif role.lower()=='b':
        
        while True:

            print('6- View the students selected for scholarship')
            print('7- Take scholarship Test')
            print('8- View scholarship results')
            print('X- Exit')
            choice=input('Enter your choice: ')

            if choice=='6':
                view_scholarship_students(db)
                    
            elif choice=='7':
                conduct_test(db)
                    
            elif choice=='8':
                display(db)
            elif choice.upper()=='X':
                print('Thank you, exiting')
                break
                
    else:
        print('Please enter a valid role!!')





   
            

        

            

        
db= mysql.connector.connect(host='localhost',user='diya',password='1234',database='project')
create_table(db)
print('WELCOME!!!')
print('What do you want to do?')
while True:
    print('1-Signup')
    print('2-Login')
    print('X-Exit')
    print('-------------------------')
    choice=input('Enter your choice: ')
    if choice=='1':
        signup(db)
    elif choice=='2':
        if login(db) is True:
            loggedin(db)
                
        else:
            continue

    elif choice.upper()=='X':
        print('Thank you, exiting')
        break
    else:
        print('Input a valid choice')