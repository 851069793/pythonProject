import pymysql
conn =  pymysql.connect(host="localhost",user="root",password="root",db="test")
cursor = conn.cursor()
# cursor.execute("INSERT INTO test1 values(?,?)", (9909, 'zgq'))
# cursor.commit()
cursor.execute("select * from test1")
db_version = cursor.fetchall()
print(db_version)

# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL primary key,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
# cursor.execute(sql)


cursor.close()
conn.close()