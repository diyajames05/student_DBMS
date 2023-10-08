import mysql.connector
import dbcreate
import signup
import login
import register
import update
import search 
import questions
import random_stu





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


    







