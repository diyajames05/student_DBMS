import mysql.connector

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
