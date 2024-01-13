from tkinter import *

def click_button(number):
    curernt_text = a.get("1.0","end-1c")
    a.delete("1.0",END)
    a.insert(END,curernt_text+str(number))

def clear_text():
    a.delete("1.0",END)

def add():
    first_number = a.get("1.0","end-1c")
    global operation
    global f_number
    operation = "addition"
    f_number = float(first_number)
    a.delete("1.0",END)
def multi():
    first_number = a.get("1.0","end-1c")

    global operation
    global f_number
    operation = "multi"
    f_number = float(first_number)
    a.delete("1.0",END)
def divi():
    first_number = a.get("1.0","end-1c")
    global operation
    global f_number
    operation = "division"
    f_number = float(first_number)
    a.delete("1.0",END)
def sub():
    first_number = a.get("1.0",END)
    global operation
    global f_number
    operation = "sub"
    f_number = float(first_number)
    a.delete("1.0",END)
def per():
    first_number = a.get("1.0",END)
    global operation
    global f_number
    operation = "per"
    f_number = float(first_number)
    a.delete("1.0",END)
def equal():
    second_number = a.get("1.0","end-1c")
    a.delete("1.0",END)
    if operation == "addition":
        result = f_number + float(second_number)
        a.insert(END,str(result))
    elif operation == "multi":
        result = f_number * float(second_number)
        a.insert(END,str(result))
    elif operation == "division":
        result = f_number / float(second_number)
        a.insert(END,str(result))
    elif operation == "sub":
        result = f_number - float(second_number)
        a.insert(END,str(result))
    elif operation == "per":
        result = (f_number/100)
        a.insert(END,str(result))



root=Tk()
root.title("NIRU_Calculator")
root.geometry("400x550")
root.maxsize(400, 550)
root.minsize(400, 550)
e = Frame(root,bd=10,relief=RIDGE)
e.place(x=0,y=0,width=400,height=75)

a = Text(e,font=("times new roman",34,"bold"))
a.place(x=0,y=0,width=400,height=75)

Buttonframe = Frame(root,bd=10,relief=RIDGE)
Buttonframe.place(x=0,y=75,width=400,height=475)

button_9 = Button(Buttonframe,text="9",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=lambda: click_button(9))
button_8 = Button(Buttonframe,text="8",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=lambda: click_button(8))
button_7 = Button(Buttonframe,text="7",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=lambda: click_button(7))
button_6 = Button(Buttonframe,text="6",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=lambda: click_button(6))
button_5 = Button(Buttonframe,text="5",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=lambda: click_button(5))
button_4 = Button(Buttonframe,text="4",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=lambda: click_button(4))
button_3 = Button(Buttonframe,text="3",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=lambda: click_button(3))
button_2 = Button(Buttonframe,text="2",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=lambda: click_button(2))
button_1 = Button(Buttonframe,text="1",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=lambda: click_button(1))
button_0 = Button(Buttonframe,text="0",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=lambda: click_button(0))

button_multi = Button(Buttonframe,text="X",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=multi)
button_sub = Button(Buttonframe,text="-",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=sub)
button_add = Button(Buttonframe,text="+",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=add)
button_divide = Button(Buttonframe,text="/",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=divi)
button_clear = Button(Buttonframe,text="AC",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=clear_text)
button_decimal = Button(Buttonframe,text=".",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=lambda: click_button("."))
button_double = Button(Buttonframe,text="00",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=lambda: click_button("00"))
button_result = Button(Buttonframe,text="=",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=equal)
button_per = Button(Buttonframe,text="%",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=per)
button_back = Button(Buttonframe,text="Back",padx=10,pady=25,font=("times new romen",20,"bold"),bd=10,command=clear_text)


button_9.place(x=0, y=0, width=100, height=95)
button_8.place(x=100, y=0, width=100, height=95)
button_7.place(x=200, y=0, width=100, height=95)
button_6.place(x=0, y=95, width=100, height=95)
button_5.place(x=100, y=95, width=100, height=95)
button_4.place(x=200, y=95, width=100, height=95)
button_3.place(x=0, y=190, width=100, height=95)
button_2.place(x=100, y=190, width=100, height=95)
button_1.place(x=200, y=190, width=100, height=95)
button_0.place(x=100, y=285, width=100, height=95)
button_multi.place(x=300, y=0, width=100, height=95)
button_sub.place(x=300, y=95, width=100, height=95)
button_add.place(x=300, y=190, width=100, height=95)
button_divide.place(x=300, y=285, width=100, height=95)
button_clear.place(x=0, y=285, width=100, height=95)
button_decimal.place(x=200, y=285, width=100, height=95)
button_double.place(x=0, y=380, width=100, height=95)
button_result.place(x=300, y=380, width=100, height=95)
button_per.place(x=100, y=380, width=100, height=95)
button_back.place(x=200, y=380, width=100, height=95)




root.mainloop()