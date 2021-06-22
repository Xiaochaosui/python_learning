# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from excel_merge import merge_csv
from filename_group import file_group
import os
if __name__ == '__main__':
    # group_path 分组之后的你要放在的目录
    pwd = r'C:\Users\Administrator\Desktop\SweepMode_0V\SweepMode_0V'
    # 可以就在这个目录下创建 或者 你要改到新的 目录的话 我再改一下
    group_path = r'C:\Users\Administrator\Desktop\SweepMode_0V\SweepMode_0V'

    #dst = r'C:\Users\Administrator\Desktop\a\result.csv'
    result_file =  r'result.csv'
    groups = file_group(pwd,group_path)
    #print(groups)
    for key,group_dir in groups.items():
        #print(group_dir)
        merge_csv(group_dir,os.path.join(group_dir,result_file))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
