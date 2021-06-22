
import zipfile
import os
import unrar
def unzip_file(path):
    '''
    基本格式：zipfile.ZipFile(filename[,mode[,compression[,allowZip64]]])
    mode：可选 r,w,a 代表不同的打开文件的方式；r 只读；w 重写；a 添加
    compression：指出这个 zipfile 用什么压缩方法，默认是 ZIP_STORED，另一种选择是 ZIP_DEFLATED；
    allowZip64：bool型变量，当设置为True时可以创建大于 2G 的 zip 文件，默认值 True；

    '''
    zip_file = zipfile.ZipFile(path)
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件

    for f in zip_list:
        zip_file.extract(f, os.getcwd())  # 循环解压文件到指定目录
    zip_file.close()  # 关闭文件，必须有，释放内存

import rarfile
def unrar_file(file,filepath):
    rf = rarfile.RarFile(file, mode='r')  # mode的值只能为'r'
    rf_list = rf.namelist()  # 得到压缩包里所有的文件
    print('rar文件内容', rf_list)
    for f in rf_list:
        rf.extract(f, filepath)  # 循环解压，将文件解压到指定路径

    # 一次性解压所有文件到指定目录
    # rf.extractall(path) # 不传path，默认为当前目录


file = r'C:\Users\Administrator\Desktop\人员管理列表-模板.rar'
print(os.getcwd())