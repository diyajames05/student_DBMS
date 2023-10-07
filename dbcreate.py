def create_table(db):
    cursor=db.cursor()
    q1='''CREATE TABLE IF NOT EXISTS login (
        user_name VARCHAR(20) PRIMARY KEY, 
        password VARCHAR(20));'''
    cursor.execute(q1)
    q2='''CREATE TABLE IF NOT EXISTS student (
        stu_id INT PRIMARY KEY AUTO_INCREMENT, 
        name VARCHAR(20) NOT NULL, 
        class VARCHAR(20) NOT NULL, 
        section VARCHAR(10) NOT NULL,
        mname VARCHAR(20) NOT NULL, 
        fname VARCHAR(20) NOT NULL, 
        fees INT NOT NULL);'''
    cursor.execute(q2)