import pyodbc

# Connection parameters
server = 'SQLEXPRESS'
database = 'DBO'

# Create a connection string
conn_str = f'DRIVER={{SQL Server}};SERVER={SQLEXPRESS};DATABASE={Students}'

# Connect to the database
conn = pyodbc.connect(conn_str)

# Create a cursor from the connection
cursor = conn.cursor()

# Example: Execute a simple query
cursor.execute('SELECT * FROM Students')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Example: Insert data into a table
insert_query = 'INSERT INTO Students (Student ID, Student Name, Class, Age, Height) VALUES (?, ?, ?, ?, ?)'
values = ('ID', 'Name', 'Class', 'Age', 'Height')
cursor.execute(insert_query, values)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()