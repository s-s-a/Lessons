import pyodbc

conn = pyodbc.connect(r'''Driver={ODBC Driver 17 for SQL Server};
<<<<<<< HEAD
                      Server=.;
=======
                      Server=msk-db-1;
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
                      Database=master;
                      Trusted_Connection=yes;
                      APP=Pyton App;
                      Workstation=SSA-ASUS''')
# conn.setdecoding(pyodbc.SQL_CHAR,encoding='utf-8')
cursor = conn.cursor()
cursor.execute('select @@version')
for row in cursor:
<<<<<<< HEAD
    print(row)
=======
    print(str(row[0]).replace(r'\n', '\n').replace(r'\t', '\t'))
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841

conn.close()
