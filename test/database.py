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

    sql = 'create table if not exists sequences (id integer primary key, sequence varchar(20), name varchar(20), date datetime default current_timestamp)'
    c.execute(sql)

    sql = 'create table if not exists pending (id integer primary key, sequence varchar(20), date datetime default current_timestamp)'
    c.execute(sql)

def InsertSequenceData(table, data):
    conn, c = ConnectToDatabase()

    sql = 'insert into ' + table + ' (sequence) values("' + data + '");'
    c.execute(sql)
    conn.commit()

def SaveSequence(sequence, name):
    conn, c = ConnectToDatabase()

    sql = 'insert into ' + table + ' (sequence, name) values ("' + squence + ', ' + name + '");'
    c.execute(sql)
    conn.commit()

def RunSql(sql):
    conn, c = ConnectToDatabase()
    c.execute(sql)
    conn.commit()

def GetData(table):
    conn, c = ConnectToDatabase()

    c.execute("SELECT * FROM " + table)
    return c.fetchall()

def GetSequence(sequence_id):
    conn, c = ConnectToDatabase()
    sql = 'SELECT * FROM sequences WHERE id=' + sequence_id + ';'
    c.execute(sql)
    return c.fetchall()