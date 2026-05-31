from pymysql import Connection

conn=Connection(host="localhost",#ip地址 （nom d hote ou adressen IP)
                port=3306, #port 端口
                user="root",#登陆用户
                password="root",#密码
                database="class",
                autocommit=True,#自动提交
                )
#获取登陆信息
print(conn.get_server_info())

#获取游标对象cursor
cursor=conn.cursor()
#创建student2表
#cursor.execute("create table student2(id int, name varchar(20),age int,gender varchar(10));")
#只有增删改需要commit()
#conn.commit()
#插入数据
cursor.execute("insert into student2 values (10001,'Leo',18,'male'),(10002,'Kevin',21,'male'),(10003,'Lucas',17,'male'),(10004,'Laurent',36,'female'),(10005,'Alex',40,'female');")

#查询数据
#execute() 用来执行sql语句
cursor.execute("select * from student2;")
#fetchall 获取一次查询的所有结果 返回值的类型是tuple
results : tuple=cursor.fetchall()
for r in results:
    print(r)

#关闭连接
conn.close()

