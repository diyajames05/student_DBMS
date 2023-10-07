def create_table(db):
    cursor=db.cursor()
    q1='CREATE TABLE IF NOT EXISTS login (user_name VARCHAR(20) PRIMARY KEY, password VARCHAR(20));'
    cursor.execute(q1)
