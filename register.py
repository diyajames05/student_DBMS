import mysql.connector


def register(db):
    cursor=db.cursor()
    print('Please enter the following details')
    name=input('Enter Student Name: ')
    clas=input('Enter class: ')
    section=input('Enter section: ')
    mname=input("Enter Mother's Name: ")
    fname=input("Enter Father's Name: ")
    fees= int(input('Enter total fees: '))
    q2="INSERT INTO student (name, class, section, mname, fname, fees) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(q2,[name, clas, section, mname, fname, fees])
    db.commit()
    print("User Successfully Registered!!!")
