import sqlite3
conn = sqlite3.connect("test1.db")
cur = conn.cursor()
# cur.execute("create table if not exists NO(no int primary key)")
cur.execute("insert into NO values(1);")
# conn.commit()
cur.close()
conn.close()