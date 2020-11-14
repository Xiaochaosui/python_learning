# 一个.py文件就是一个模块

# 每一个模块都有一个__name__属性，其值等于"__main__"，表面该模块自身
# 在执行

# 当前文件为程序的入口文件，则__name__属性值为__main__
if __name__ =="__main__":
    print("这是xcs.py文件")
else:
    print(__name__)
    def sayGood():
        print("xcs is a good man!")
    def sayNice():
        print("xcs is a nice man!")
    def sayHandsome():
        print("xcs is a handsome man")