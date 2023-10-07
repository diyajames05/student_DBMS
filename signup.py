
import getpass
def signup(db):
    cursor=db.cursor()
    print('Please enter the following details')
    user_name=input('enter username: ')
    password=getpass.getpass('enter password: ')
    print(user_name)
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