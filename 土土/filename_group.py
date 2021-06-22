import os
import pandas as pd
import shutil
import re
# pwd 你要处理的file目录
# group_path 分组之后的你要放在的目录
pwd = r'C:\Users\Administrator\Desktop\SweepMode_0V\SweepMode_0V'
# 可以就在这个目录下创建 或者 你要改到新的 目录的话 我再改一下
group_path = r'C:\Users\Administrator\Desktop\SweepMode_0V\SweepMode_0V'

# file = "1-25.csv"
# pattern = re.compile(re_str)
# res = pattern.findall(file)[0][1:-4]
# print(res)

def file_group(pwd,group_path):
    file_list = []
    file_dict = {}
    re_str = "-.*"
    for root,dirs,files in os.walk(pwd): # 第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
      #print(files)
      for file in files:
          pattern = re.compile(re_str)
          res = pattern.findall(file)[0][1:-4]
          name_group = res
          #print(name_group)
          dir_path = os.path.join(group_path, name_group)

          if name_group not in file_dict.keys():
                file_dict[name_group] = dir_path
                try:
                    os.mkdir(dir_path)
                    print("创建" + name_group + "成功", "啊穗爱啊土")
                except:
                    print("创建"+name_group+"成功","啊穗爱啊土")
          src = os.path.join(root, file)
          try:
            shutil.copy(src,dir_path)
            #print("分组" + name_group + "成功", "啊穗爱啊土")
          except:
              print("已经分组成功")
    return file_dict
