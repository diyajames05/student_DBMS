import mysql.connector
import getpass



def login(db):
    cursor=db.cursor()
    attemps=3
    while attemps>0:
        user_name=input('Enter username: ')
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
        




    
