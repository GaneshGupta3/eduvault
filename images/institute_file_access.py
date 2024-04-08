from tkinter import Tk, Frame, Label, Button, BOTTOM, FLAT,Entry,Canvas
from dbConnection import *
from fetch_documents_list import *

def instituteHasAccessTo(Institute_id,student_id, user_type):
    dbobj = db()
    mydb, cursor = dbobj.dbconnect("documents")
    
    if user_type == "I":
        query = "SELECT file_id FROM file_access WHERE iuid=%s and suid=%s"
        cursor.execute(query, (Institute_id,student_id))
        file_ids = cursor.fetchall()
        
        result = []
        for row in file_ids:
            file_id = row[0]  # Extracting the file_id from the tuple
            result.append(fetch_documents_for_institute_view(file_id))
        print(result)
        return result
    else:
        raise ValueError("Invalid user type: user_type must be 'I'")

# def check():
#     result2 = instituteHasAccessTo("I138615553989","S353356847444", "I")
#     print(result2)

# check()
