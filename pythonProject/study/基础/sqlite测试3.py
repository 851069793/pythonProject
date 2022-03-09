import sqlite3
conn = sqlite3.connect("test1.db")
cur = conn.cursor()
# cur.execute("create table no_name2(id int primary key,id2 int )")
list1 = [(99,"余贞鹏")]
cur.execute("insert into no_name1 values(?,?)",list1[0])
# conn.commit()
cur.close()
conn.close()