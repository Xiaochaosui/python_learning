import os, sys

cur_path = 'D:\DataSet\camvid\labels'  # 你的数据集路径

labels = os.listdir(cur_path)

for label in labels:
    old_label = str(label)
    new_label = label.replace('_P.png', '.png')
    print(old_label, new_label)
    os.rename(os.path.join(cur_path, old_label), os.path.join(cur_path, new_label))

