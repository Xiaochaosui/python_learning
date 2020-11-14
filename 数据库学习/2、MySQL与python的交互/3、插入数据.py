import pymysql


db = pymysql.connect("localhost","root","","xiao")
cursor = db.cursor()

#插入数据
sql='insert into bandcard values(0,500)'
try:
    cursor.execute(sql)
    db.commit()
except:
    #如果提交失败，回滚到上一次的数据
    db.rollback()


#data = cursor.fetchone()
#print(data)
cursor.close()
db.close()