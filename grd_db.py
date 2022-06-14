import sqlite3


class Users:
    """Creates database with users table includes:
       create query
       insert query
       select query
    """

    def __init__(self, tablename="users", userId="userId", password="password",  email="email"):
        self.__tablename = tablename
        self.__userId = userId
        self.__password = password
        self.__email = email
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        query_str = "CREATE TABLE IF NOT EXISTS " + tablename + "(" + self.__userId + " " + \
                    " INTEGER PRIMARY KEY AUTOINCREMENT ,"
        query_str += " " + self.__password + " TEXT    NOT NULL ,"
        query_str += " " + self.__email + " TEXT UNIQUE    NOT NULL );"

        # conn.execute("Create table users")
        conn.execute(query_str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def __str__(self):
        return "table  name is ", self.__tablename

    def get_table_name(self):
        return self.__tablename

    def insert_user(self, password, email):
        conn = sqlite3.connect('test.db')
        insert_query = "INSERT INTO " + self.__tablename + " (" + self.__password + "," + self.__email + ") VALUES " \
                                                                                                            "(" + "'" + password + "'" + "," + "'" + email + "'" + ");"
        print(insert_query)
        conn.execute(insert_query)
        conn.commit()
        conn.close()
        print("Record created successfully")

    def select_user_by_id(self):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str1 = "select * from users;"

        """strsql = "SELECT userId, password, email  from " +  self.__tablename + " where " + self.__userId + "=" \
            + str(userId)
        """
        print(str1)
        cursor = conn.execute(str1)
        for row in cursor:
            print("userId = ", row[0])
            print("email = ", row[1])
            print("password =", row[2])

        print("Operation done successfully")
        conn.close()

    def delete_user(self, identity):
        conn1 = sqlite3.connect('test.db')
        sql = 'DELETE FROM users WHERE userId = ' + identity
        cur = conn1.cursor()
        cur.execute(sql)
        conn1.commit()
        cur.close()
        conn1.close()

    def update_users(self, password):
        conn1 = sqlite3.connect('test.db')
        quary = f"UPDATE users SET password = '{password}' WHERE userId = 1;"
        print(quary)
        cur = conn1.cursor()
        cur.execute(quary)
        conn1.commit()
        cur.close()
        conn1.close()

    def account_exist(self, email):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str1 = "select * from users;"

        """strsql = "SELECT userId, password, email  from " +  self.__tablename + " where " + self.__userId + "=" \
            + str(userId)
        """
        print(str1)
        cursor = conn.execute(str1)
        print("here")
        print(cursor)
        for row in cursor:
            print(row)
            if email == row[2]:
                print("exist")
                cursor.close()
                conn.close()
                return True
        cursor.close()
        conn.close()
        return False

    def is_account(self, email, password):
        print("email is - " + email)
        print("password is - " + password)
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str1 = "select * from users;"

        """strsql = "SELECT userId, password, email  from " +  self.__tablename + " where " + self.__userId + "=" \
            + str(userId)
        """
        print(str1)
        cursor = conn.execute(str1)
        for row in cursor:
            print(row)
            print("now im here")
            if row[1] == password and row[2] == email:
                print("niceeeeeeeeeeeeeeeeeeeeee")
                cursor.close()
                conn.close()
                return True
        print("not gooddddddddddd")
        cursor.close()
        conn.close()
        return False






