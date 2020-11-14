import time


path = r"C:\Users\Administrator\Desktop\f"
name = r"\xcs-%s"%(time.strftime("%y-%m-%d"))
fileName = path + name+ ".txt"
f = open(fileName,"a",encoding="utf-8")
time_str = "%s"%(time.strftime("%X"))
diary_str = "阿标还是写不出来，怎么办？老师心态崩了"
con = f.write(time_str+"\n"+diary_str+"\n")
f.close()

