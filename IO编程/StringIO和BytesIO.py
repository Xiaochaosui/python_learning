from io import StringIO
from io import BytesIO
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
f = StringIO()
f.write("Hello") # 写入str
print(f.getvalue()) # 获得str

f1 = BytesIO()
f1.write("中文".encode("utf-8"))
print(f1.getvalue())