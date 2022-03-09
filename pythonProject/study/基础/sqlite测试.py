import sqlite3
conn = sqlite3.connect("test1.db")
cur = conn.cursor()
stlist = [(99, "zgq")]
# cur.execute("insert into stno values("55","测试")")
cur.execute("INSERT INTO stno values(?,?)", (9909, "zgq"))

cur.execute("select * from stno")
print(cur.fetchall())
# conn.commit()
cur.close()
conn.close()