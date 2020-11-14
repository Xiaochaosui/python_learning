import win32con
import win32gui
import time
import random

QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")

#参数1：控制的窗体
#参数2：大致方位,HWND_TOPMOST 上方
#参数3：位置x
#参数4：位置y
#参数5：长度
#参数6：宽度
while True:
    x = random.randrange(900)
    y = random.randrange(600)
    win32gui.SetWindowPos(QQWin,win32con.HWND_TOPMOST,x,y,900,600,win32con.SWP_SHOWWINDOW)
    time.sleep(0.01)