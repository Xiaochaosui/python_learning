import os
import pandas as pd


# 将文件读取出来放一个列表里面
pwd = r'C:\Users\Administrator\Desktop\SweepMode_0V\SweepMode_0V'  # 获取文件目录
dst = r'C:\Users\Administrator\Desktop\a\result.csv'
def merge_csv(pwd,dst):
  # 新建列表，存放文件名
  file_list = []
  # 新建列表存放每个文件数据(依次读取多个相同结构的Excel文件并创建DataFrame)
  dfs = []
  flag=0
  for root,dirs,files in os.walk(pwd): # 第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
    files.sort(key=lambda x: int(x[:-6]))
    #print(files)
    for file in files:
      #print(file)
      new_name = file
      #print(new_name)
      file_path = os.path.join(root, file)
      file_list.append(file_path) # 使用os.path.join(dirpath, name)得到全路径
      df = pd.read_csv(file_path) # 将excel转换成DataFrame
      #print(df)
      df = df.rename(columns={"LP(dB)":new_name})
      #print(df)
      #df.rename(index=str, columns={"LP(dB)": new_name})
      if flag==0:
        dfs.append(df["Wave(nm)"])
        dfs.append(df[new_name])
        flag = 1
        #print(dfs)
      else:
        dfs.append(df[new_name])

  #print(file_list)
  # 将多个DataFrame合并为一个
  df = pd.concat(dfs,axis=1)

  # 写入excel文件，不包含索引数据
  df.to_csv(dst, index=False)

