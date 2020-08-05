import pymysql.cursors


db = pymysql.connect(host='localhost', 
                    user='root', 
                    password='', 
                    db='kbank', 
                    charset='utf8mb4', 
                    cursorclass=pymysql.cursors.DictCursor)

def create_table():

    try:
        with db.cursor() as cursor:
            # create new table
            sql = "CREATE TABLE users (id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(30), account_no VARCHAR(12), age INT(3), balance INT(30));"
            
            cursor.execute(sql)
        
        db.commit()
    
    finally:
        pass
        # db.close()

    return True

def add_user(name, age, password, account_no):

    try:
        with db.cursor() as cursor:
            #read a single record
            sql = f"INSERT INTO users (name, age, password, account_no, balance) VALUES ('{name}', '{age}', '{password}', '{account_no}', 10000);"

            cursor.execute(sql)
        db.commit()
    finally:
        print("Successfully Added User...!!")
        # db.close()

def fetch_user_details(name):
    try:
        with db.cursor() as cursor:
            #read a single record
            sql = f"SELECT name, password, balance FROM users where name = '{name}';"

            cursor.execute(sql)

        data = cursor.fetchall()
        return data
    finally:
        print("Successfully Fetched...!!")
        # db.close()

def get_balance(name):

    try:
        with db.cursor() as cursor:
            #read a single record
            sql = f"SELECT balance from users where name = '{name}';"
            print(sql)

            cursor.execute(sql)

        data = cursor.fetchall()
        return data
    finally:
        print("Successfully Fetched...!!")
        


def alter_balance(name, balance):

    try:
        with db.cursor() as cursor:
            #read a single record
            sql = f"UPDATE users SET balance = {balance} WHERE name = '{name}';"

            cursor.execute(sql)

        db.commit()
    finally:
        print("Successfully Updated User Balance...!!")
        # db.close()

def get_user_details(name):

    try:
        with db.cursor() as cursor:
            #read a single record
            sql = f"SELECT name, account_no, balance FROM users WHERE name = '{name}';"

            cursor.execute(sql)

        data = cursor.fetchall()

        
        return data
    finally:
        print("Successfully gotten user data...!!")
        # db.close()
