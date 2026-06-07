from data_define import Record
from file_define import TextFileReader,JsonFileReader
from pymysql import Connection

text_file_reader = TextFileReader("January2023SalesData.txt")
json_file_reader = JsonFileReader("February2023SalesData.txt")

jan_data:list[Record] = text_file_reader.read_data()
feb_data:list[Record] = json_file_reader.read_data()
all_data:list[Record] = jan_data + feb_data
#on peut pas print directement all_data car def__init__ ne peut que print les elements du type Record
#comme all_data est un type list donc non Record donc on peut pas utiliser --String--
#donc on peut que print les ele ds la liste ( car list[Record] )
"""
for i in all_data:
    print(i)
"""
conn=Connection(
    host="localhost",
    port=3306,
    user='root',
    password="root",  # 密码
    database="py_sql",
    autocommit=True,  # 自动提交
)
print(conn.get_server_info())
#创建游标
cursor=conn.cursor()

#插入数据
"""
for record in all_data:
    sql=f"insert into orders (order_date,order_id,money,province) values {record.date,record.order_id,record.money,record.province};"
    cursor.execute(sql)
"""

sql="select * from orders;"
cursor.execute(sql)
results=cursor.fetchall()
for result in results:
    print(result)

conn.close()