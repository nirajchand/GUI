from tkinter import *
from tkinter import messagebox
import mysql.connector

def add_to_database():
    name = name_entry.get()
    age = age_entry.get()

    if not name or not age:
        messagebox.showerror("error","please enter both name and age")
        return

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "#Nbchand07",
            database = "test"
        )
        cursor = connection.cursor()

        query = "INSERT INTO info(name,age) values(%s,%s)"
        data = (name,age)
        cursor.execute(query,data)

        connection.commit()
        messagebox.showinfo("success","data added to the database successfully")

    except Exception as e:
        messagebox.showerror("error",f"error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()



root = Tk()
root.geometry("650x300")
Label(root,text="Name:").grid(row=0,column=0,padx=10,pady=10)
name_entry = Entry(root)
name_entry.grid(row=0,column=1,padx=10,pady=10)
Label(root,text="Age:").grid(row=1,column=0,padx=10,pady=10)
age_entry=Entry(root)
age_entry.grid(row=1,column=1,padx=10,pady=10)

Button(root,text="create",command=add_to_database).grid(row=3,column=4,columnspan=10,pady=10)

root.mainloop()



