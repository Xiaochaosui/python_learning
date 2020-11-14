import pymysql

'''
fetchone()
功能：获取下一个查询结果集，结果集是一个对象

fetchall()
功能：接收全部的返回行

rowcount:是一个只读属性，返回execute()的方法影响的行数
'''
db = pymysql.connect("localhost","root","","xiao")
cursor = db.cursor()

#查询数据
sql='select * from bandcard where money > 400'
try:
    cursor.execute(sql)
    dataList = cursor.fetchall()
    for data in dataList:
        print("%d----%d"%(data[0],data[1]))

    db.commit()
except:
    #如果提交失败，回滚到上一次的数据
    db.rollback()



#print(data)
cursor.close()
db.close()