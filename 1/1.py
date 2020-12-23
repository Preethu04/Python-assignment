import mysql.connector

def database_connect():

    try:
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql123",
        database="employees"
        )


        if conn.is_connected():
            print('Connected to MySQL database')

            
        cursor = conn.cursor()
        
        cursor.execute('Select * from employees')

        for result in cursor.fetchall():
            yield result
  

    except:
        print('Not connected to database') 

if __name__ == '__main__':

    print(database_connect().__next__())
