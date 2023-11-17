import sys
import pypyodbc as odbc

records = [
    ['10000', 'W', 'Commercial', '18', '6.2'],
    ['10001', 'A', 'Science', '16', '6.1']
]

DRIVER = 'SQL Server'
SERVER_NAME = 'Safe\SQLEXPRESS'
DATABASE_NAME = 'DBA'

conn_string = f"""
          Driver={{{DRIVER}}};
          Server={SQLEXPRESS};
          Database={DBO};
          Trust_Connection=yes;
"""

try:
    conn = odbc.connect(conn_string)
    except Exception as e:
        print(e)
        print('Task is terminated')
        sys.exit()
    else:
        cursor = conn.cursor()

insert_statement = """
INSERT INTO STUDENTS
VALUES (?, ?, ?, ?, ?)
"""

try:
  for record in records:
    print(record)
    cursor.execute(insert_statement, record)

    except Exception as e:
        cursor.rollback()
        print(e.value)
        print('Error')

    else:
        print('Successful')
        cursor.commit()
        
    finally:
        if conn.connected = 1:
            print('connection closed')
            conn.close()