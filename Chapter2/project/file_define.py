from data_define import Record
import json
#文件类
class FileReader:
    def read_data(self):
        pass

class TextFileReader(FileReader):

    def __init__(self, path):
        #文件的路径
        self.path=path

    def read_data(self):
        f=open(self.path,'r',encoding='utf-8')
        record_list:list[Record]=[]
        for line in f.readlines():
            line=line.strip()
            data_list=line.split(',')
            record=Record(data_list[0],data_list[1],data_list[2],data_list[3])
            record_list.append(record)
        f.close()
        return record_list

class JsonFileReader(FileReader):

    def __init__(self, path):
        # 文件的路径
        self.path = path

    def read_data(self):
        f = open(self.path, 'r', encoding='utf-8')
        record_list: list[Record] = [] #list 里面都是record类型（class record）
        for line in f.readlines():
            data2=dict(json.loads(line))
            record = Record(data2["date"], data2["order_id"], data2["money"], data2["province"])
            record_list.append(record)
        f.close()
        return record_list

if __name__ == '__main__':
    text_file_reader=JsonFileReader("February2023SalesData.txt")
    text_file_reader1 = TextFileReader("January2023SalesData.txt")
    data=text_file_reader.read_data()
    data1 =text_file_reader1.read_data()
    for i in data:
        print(i)
    for i in data1:
        print(i)


