import sqlite3
location = 'test.db'
table_name = 'test_table'

def ConnectToDatabase():
    conn = sqlite3.connect(location)
    c = conn.cursor()
    return conn, c

def SetupDatabase():
    file = open('myfile.dat', 'w+')
    file.close()
    conn, c = ConnectToDatabase()

    sql = 'create table if not exists ' + table_name + ' (id integer primary key, sequence varchar(20))'
    c.execute(sql)

    sql = 'insert into ' + table_name + ' (id) values (%d)' % (1)
    c.execute(sql)
    conn.commit()

def InsertData(sequence):
    conn, c = ConnectToDatabase()

    sql = 'insert into ' + table_name + ' (sequence) values ' + sequence
    c.execute(sql)
    conn.commit()

def GetData():
    conn, c = ConnectToDatabase()

    c.execute("SELECT * FROM " + table_name)
    return c.fetchall()