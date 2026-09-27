#目标：给一个文件夹，把这个文件夹以及所有子文件夹里的文件全部找出来
import os
def get_files_recursion_from_dir(path):
    print("le dossier actuel est: "+path)
    #保存我们找到的所有的文件
    fill_list=[]
    #判断文件是否存在
    if os.path.exists(path):
        #找到文件里的内容
        for f in os.listdir(path):
            #new_path=path+"/"+f# ==> 拼接路径
            new_path=os.path.join(path,f)
            #判断是否是文件夹
            if os.path.isdir(new_path):
                fill_list+=get_files_recursion_from_dir(new_path)
            else:
                fill_list.append(new_path)
    else:
        print(f"le repertoire specifie {path} non existe")
        return []
    return fill_list
if __name__=="__main__":
    files=get_files_recursion_from_dir("/Users/yixueliang/PycharmProjects/PythonMaster/Chapter3")
    print(files)