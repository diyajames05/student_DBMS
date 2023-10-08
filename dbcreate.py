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
        fees INT NOT NULL);'''
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
        student_id INT NOT NULL,
        FOREIGN KEY (student_id) REFERENCES student(stu_id), 
        score INT DEFAULT NULL, 
        reduced_fee INT DEFAULT NULL

    );'''
    cursor.execute(q4)








# To populate data
def populate_student_data(db):
    cursor=db.cursor()
    student_data = [
        ["Diya9","5","C","FatherA","MotherA","5000"],
        ["Diya10","1","A","FatherS","MotherB","7000"],
        ["Diya3","12","D","FatherD","MotherC","8000"],
        ["Diya4","4","F","FatherQ","MotherD","9000"],
        ["Diya5","7","B","FatherW","MotherE","5900"],
        ["Diya6","9","D","FatherE","MotherF","8000"],
        ["Diya7","11","C","FatherT","MotherG","2000"],
        ["Diya8","10","A","FatherY","MotherH","4000"]
    ]
    for student in student_data:
        q2="INSERT INTO student (name, class, section, mname, fname, fees) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(q2,student)
        
    db.commit()

## this is to initialise the student database instead of manually typing
## run this file as main to populate the database
if __name__ == "__main__":
    import mysql.connector
    db= mysql.connector.connect(host='localhost',user='diya',password='1234',database='project')
    create_table(db)