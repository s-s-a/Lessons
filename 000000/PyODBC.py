import pyodbc

conn = pyodbc.connect(r'''Driver={ODBC Driver 17 for SQL Server};
                      Server=msk-db-1;
                      Database=master;
                      Trusted_Connection=yes;
                      APP=Pyton App;
                      Workstation=SSA-ASUS''')
# conn.setdecoding(pyodbc.SQL_CHAR,encoding='utf-8')
cursor = conn.cursor()
cursor.execute('select @@version')
for row in cursor:
    print(str(row[0]).replace(r'\n', '\n').replace(r'\t', '\t'))

conn.close()
