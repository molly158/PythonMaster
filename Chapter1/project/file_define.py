from data_define import Record
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
if __name__ == '__main__':
    text_file_reader=TextFileReader("January2023SalesData.txt")
    data=text_file_reader.read_data()
    for i in data:
        print(i)


