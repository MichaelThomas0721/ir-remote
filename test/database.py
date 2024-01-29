import sqlite3
location = 'test.db'
table_names = ['sequences', 'pending']

def ConnectToDatabase():
    conn = sqlite3.connect(location)
    c = conn.cursor()
    return conn, c

def SetupDatabase():
    file = open('myfile.dat', 'w+')
    file.close()
    conn, c = ConnectToDatabase()

    for name in table_names:
        sql = 'create table if not exists ' + name + ' (id integer primary key, sequence varchar(20), date datetime default current_timestamp)'
        c.execute(sql)

def InsertData(table, data):
    conn, c = ConnectToDatabase()

    sql = 'insert into ' + table + ' (sequence) values("' + data + '");'
    c.execute(sql)
    conn.commit()

def GetData(table):
    conn, c = ConnectToDatabase()

    c.execute("SELECT * FROM " + table)
    return c.fetchall()