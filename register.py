## STUDENT DBMS
## Author Diya Sojan 12-A
## 08/10/23
import mysql.connector


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
        print('Since the parent is a teacher, you have a fee reducion of Rs.')
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
    print("User Successfully Registered!!!")
        

