import mysql.connector

def questionanswer(db):
        cursor=db.cursor()
        while True:
            print("Welcome to Question Portal")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            question = input("Enter the question :")
            A = input("Enter the option A :")
            B = input("Enter the option B :")
            C = input("Enter the option C :")
            D = input("Enter the option D :")
            answer = 'X'
            while answer == 'X':
                op = input("Which option is correct answer? (A,B,C OR D) ")
                if op.upper() == 'A':
                    answer = A
                elif op.upper() == 'B':
                    answer = B
                elif op.upper() == 'C':
                    answer = C
                elif op.upper() == 'D':
                    answer = D
              
                else:
                    print("Please choose a valid option as your answer")
                
            print('you have entered the question', question)
            print('with the options:', A, B, C, D)
            print('and the correct anser given is', answer)
            con=input('Type C to confirm any other key to cancel')
            if con.upper()=='C':
                q1= "INSERT INTO question(question,A,B,C,D,answer) VALUES (%s,%s,%s,%s,%s,%s);"
                cursor.execute(q1,[question, A, B, C, D, answer])
                db.commit()
                ch=input('Question added successfully! Do you want to add more questions? y or n?')
                if ch.upper()=='N':
                    break 
            else:
                print('cancelled')