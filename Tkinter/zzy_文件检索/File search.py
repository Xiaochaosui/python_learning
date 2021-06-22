# author: "xiaochaosui"
# time: '2021/1/27 11:37'
# mail: '939103485@qq.com'

import tkinter
from PIL import Image, ImageTk
class Application(tkinter.Frame):
    def createWidgets(self):
        # 获取屏幕分辨率
        window =self.master
        winWidth = 800
        winHeight = 600
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗体
        self.master.title(self.init_window_name)
        self.master.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        # 设置窗口图标
        window.iconbitmap(r".\111.ico")
        # 设置窗口宽高固定
        #window.resizable(0, 0)
        # 搜索框
        self.searchText = tkinter.Entry(self.master,width = 60).grid(row = 2,column = 0,columnspan = 2)
        # 搜索按钮
        self.searchButton = tkinter.Button(self.master,text = '搜索',command = self.search(),width = 10).grid(row = 2,column = 5,columnspan = 10)
        # seach() 你要执行的搜索函数



        # 你爬下来的内容 放在这个列表里
        listContent = ('姓名'.ljust(20,"-")+'作者'.ljust(20,"-")+ '日期'.ljust(20," "),'论python'.ljust(20,'-')+'肖朝穗'.ljust(20,"-")+'2020/1/1'.ljust(20," "))
        varContent = tkinter.StringVar()
        varContent.set(listContent)
        listB = tkinter.Listbox(listvariable = varContent,selectmode = tkinter.MULTIPLE,width = 60,height = 20).grid(row = 3,column = 0,columnspan = 10,rowspan = 10)

        #添加你想要的图片logo
        img_open = Image.open(r'.\fiberHome.png')
        photo = ImageTk.PhotoImage(img_open)
        label = tkinter.Label(image=photo)
        label.image = photo
        label.grid(row=0, column=0, rowspan=1, columnspan=2,sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S, padx = 5, pady = 5)

        # 下载按钮
        # 你要写的 下载函数 self.download()
        self.down = tkinter.Button(self.master,text = '下载',command = self.download(),width = 10).grid(row = 11,column = 10)
        # 退出按钮
        self.Quit = tkinter.Button(window,text = '退出',command = window.quit,width = 10).grid(row = 11,column = 14)

    # 下载函数
    def download(self):
        print("正在下载")
    # 搜索函数
    def search(self):
        print("正在搜索")


    def __init__(self,name,master):
        self.init_window_name = name
        self.master = master
        tkinter.Frame.__init__(self,master)
        self.createWidgets()


root = tkinter.Tk()
app = Application('文献检索',master=root)
app.mainloop()


