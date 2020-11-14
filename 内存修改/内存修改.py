# 进程模块
import win32process
# 系统
import win32con
import win32gui
import win32api
import ctypes
# 最高权限
PROCESS_ALL_ACCESS = (0x000F000|0x00100000|0xFF)

# 找窗体
win = win32gui.FindWindow("MainWindow","植物大战僵尸中文版")

# 根据窗体找到进程号
hid,pid = win32process.GetWindowThreadProcessId(win)
print("pid =" ,pid)
# 根据最高权限打开进程
p = win32api.OpenProcess(PROCESS_ALL_ACCESS,False,pid)

data = ctypes.c_long()
# 加载内核模块
md = ctypes.windll.LoadLibrary(r"C:\Windows\System32\kernel32.dll")

# 读取内存
address = "13FA63E8"
md.ReadProcessMemory(int(p),int(address,16),ctypes.byref(data),4,None)
# print("data =",data)

# 新值
newData = ctypes.c_long(2020)

# 修改
md.WriteProcessMemory(int(p),int(address,16),ctypes.byref(newData),4,None)
