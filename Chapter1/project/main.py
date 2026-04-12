from file_define import TextFileReader,JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, InitOpts, LabelOpts

text_file_reader = TextFileReader("January2023SalesData.txt")
json_file_reader = JsonFileReader("February2023SalesData.txt")

jan_data:list[Record] = text_file_reader.read_data()
feb_data:list[Record] = json_file_reader.read_data()
all_data:list[Record] = jan_data + feb_data

#数据处理
data_dict={}
for record in all_data:
    #判断当前日期是否存在
    if record.date not in data_dict.keys():
        data_dict[record.date]=record.money
    else:
        #累加每个省份的订单金额
        data_dict[record.date]+=record.money

bar=Bar(init_opts=InitOpts())
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("sales",list(data_dict.values()))
label_opts=LabelOpts(is_show=False)
bar.set_global_opts(title_opts=TitleOpts(title="Daily sales data"))

bar.render("Daily sales bar chart.html")