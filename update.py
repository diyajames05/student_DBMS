## STUDENT DBMS
## Author Diya Sojan 12-A
## 08/10/23
import mysql.connector

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
