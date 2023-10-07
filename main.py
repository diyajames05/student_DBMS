import mysql.connector
import dbcreate
import signup


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
        choice=input('Enter your choice')
        if choice=='1':
            signup.signup(db)
        elif choice=='2':
            print("login")
        elif choice.upper()=='X':
            print('Thank you, exiting')
            break
        else:
            print('Input a valid choice')


    







