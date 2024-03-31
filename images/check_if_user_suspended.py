from tkinter import Tk, Frame, Label, Button, BOTTOM, FLAT,Entry,Canvas
from dbConnection import *

def check_if_user_is_suspended(user_id,user_type):
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    if user_type == "S":
        query = "select suspended from student where uid=%s"
        cursor.execute(query,(user_id,))
        result = cursor.fetchone()
        if result[0]:
            print("he/she is suspended")
            return True
        else:
            print("he/she is not suspended")
            return False
    else :
        query = "select suspended,verified from institute where uid=%s"
        cursor.execute(query,(user_id,))
        result = cursor.fetchone()
        if result[0] or result[1]:
            print("institute is suspended or not verified")
            return True
        else:
            print("institute is not suspended and verified")
            return False

def check():
    result = check_if_user_is_suspended("S568111462779","S") 
    print(result)

check()