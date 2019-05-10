import pymysql

def setdata(sql):
    db = pymysql.connect("localhost", "root", "root", "pythontest")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
def getdata(sql):
    db = pymysql.connect("localhost", "root", "root", "pythontest")
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    # print(res)
    db.commit()
    db.close()
    return res
