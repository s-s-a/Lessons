import pyodbc

conn = pyodbc.connect(r'''Driver={ODBC Driver 17 for SQL Server};
                      Server=.;
                      Database=master;
                      Trusted_Connection=yes;
                      APP=Pyton App;
                      Workstation=SSA-ASUS''')
# conn.setdecoding(pyodbc.SQL_CHAR,encoding='utf-8')
cursor = conn.cursor()
cursor.execute('select @@version')
for row in cursor:
    print(row)

conn.close()
