from xcsSql import XcsSql


x =XcsSql("localhost","root","","xiao")
sql = 'select * from bandcard '
resList = x.get_all(sql)
for res in resList:
    print("%d---%d"%(res[0],res[1]))
sql1 = 'insert into bandcard value(10,200000)'
x.insert(sql1)
resList = x.get_all(sql)
for res in resList:
    print("%d---%d"%(res[0],res[1]))