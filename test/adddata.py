import pymysql

def setdata(sql):
    db = pymysql.connect("localhost", "root", "root", "pythontest")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()