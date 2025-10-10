import mssql_python as pyodbc # pip install mssql-python

SERVER_NAME = "msk-db-1"
DB_NAME = "ItalikaSQL"
DB_CONNECTION_STRING = r'''Driver={ODBC Driver 17 for SQL Server};
                      Server=''' + SERVER_NAME + ''';
                      Database=''' + DB_NAME + ''';
                      Trusted_Connection=yes;
                      TrustServerCertificate=yes;
                      APP=Pyton App;
                      Workstation=SSA-ASUS'''


settings = pyodbc.get_settings()
print(f'{settings.lowercase=}')         # False
print(f'{settings.decimal_separator=}') # "."

# Enable pooling with defaults
pyodbc.pooling()

# Enable pooling with custom values
pyodbc.pooling(max_size=50, idle_timeout=300)

# Disable pooling
pyodbc.pooling(enabled=False)


conn = pyodbc.connect(DB_CONNECTION_STRING)
# conn.setdecoding(pyodbc.SQL_CHAR,encoding='utf-8')


cursor = conn.cursor()
cursor.execute('select @@version')
for row in cursor:
    print(str(row[0]).replace(r'\n', '\n').replace(r'\t', '\t'))

cursor.execute("PRINT 'Hello world!'")
print(f'{cursor.messages=}')

conn.close()
