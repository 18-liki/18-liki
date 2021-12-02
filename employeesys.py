- 👋 Hi, I’m @18-liki
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
18-liki/18-liki is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->import tkinter 
import mysql.connector
from tkinter import messagebox
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Alpha#1418",
    database="management"
)
mycursor = mydb.cursor()
root = tkinter.Tk()
root.title("EMPLOYEE MANAGEMENT SYSTEM")
root.geometry("600x400")
# photo = PhotoImage(file='image.png')
# label12 = Label(root, image=photo).grid(row=8, column=5)
label1 = tkinter.Label(root, text="EmployeeID: ", width=20, height=2,
               bg="#88cffa").grid(row=0, column=1)
label2 = tkinter.Label(root, text="Name_of_Employee ", width=20,
               height=2, bg="#88cffa").grid(row=1, column=1)
label3 = tkinter.Label(root, text="Age", width=20,
               height=2, bg="#88cffa").grid(row=2, column=1)
label4 = tkinter.Label(root, text="Phone_Number", width=20,
               height=2, bg="#88cffa").grid(row=3, column=1)
label5 = tkinter.Label(root, text="City_Name", width=20, height=2,
               bg="#88cffa").grid(row=4, column=1)
label6 = tkinter.Label(root, text="Skill", width=20, height=2,
               bg="#88cffa").grid(row=5, column=1)
label7 = tkinter.Label(root, text="Salary", width=20, height=2,
               bg="#88cffa").grid(row=6, column=1)

e1 = tkinter.Entry(root, width=25, borderwidth=5)
e1.grid(row=0, column=2)
e2 = tkinter.Entry(root, width=25, borderwidth=5)
e2.grid(row=1, column=2)
e3 = tkinter.Entry(root, width=25, borderwidth=5)
e3.grid(row=2, column=2)
e4 = tkinter.Entry(root, width=25, borderwidth=5)
e4.grid(row=3, column=2)
e5 = tkinter.Entry(root, width=25, borderwidth=5)
e5.grid(row=4, column=2)
e6 = tkinter.Entry(root, width=25, borderwidth=5)
e6.grid(row=5, column=2)
e7 = tkinter.Entry(root, width=25, borderwidth=5)
e7.grid(row=6, column=2)


def Register():
    EmployeeId = e1.get()
    dbEmployeeId = ""
    Select = "select count(*) from emp where EmployeeId ='%s'" % (EmployeeId)
    mycursor.execute(Select)
    result = mycursor.fetchall()
    for i in result:
        dbEmployeeId = i[0]
    if(int(EmployeeId) != int(dbEmployeeId)):
        Insert = "Insert into emp(EmployeeId,Name_of_Employee,Age,Phone_Number,City_Name,Skill,Salary) values(%s,%s,%s,%s,%s,%s,%s)"
        Name_of_Employee = e2.get()
        Age = e3.get()
        Phone_Number = e4.get()
        City_Name = e5.get()
        Skill = e6.get()
        Salary = e7.get()
        
        if(Name_of_Employee != "" and Age != "" and Phone_Number != "" and City_Name != "" and Skill != "" and Salary != ""):
            Value = (EmployeeId,Name_of_Employee,Age,
                     Phone_Number,City_Name,Skill,Salary)
            mycursor.execute(Insert, Value)
            mydb.commit()
            messagebox.askokcancel("Information", "Record inserted")
            e1.delete(0, tkinter.END)
            e2.delete(0, tkinter.END)
            e3.delete(0, tkinter.END)
            e4.delete(0, tkinter.END)
            e5.delete(0, tkinter.END)
            e6.delete(0, tkinter.END)
            e7.delete(0, tkinter.END)
        else:
            if (Name_of_Employee == "" and Age == "" and Phone_Number == "" and City_Name == "" and Skill == "" and Salary == ""):
                messagebox.askokcancel(
                    "Information", "New Entery Fill All Details")
            else:
                messagebox.askokcancel("Information", "Some fields left blank")
    else:
        messagebox.askokcancel("Information", "Record Already exists")



def Delete():
    EmployeeId = e1.get()
    Delete = "delete from emp where EmployeeId='%s'" % (EmployeeId)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information", "Record Deleted")
    e1.delete(0, tkinter.END)
    e2.delete(0, tkinter.END)
    e3.delete(0, tkinter.END)
    e4.delete(0, tkinter.END)
    e5.delete(0, tkinter.END)
    e6.delete(0, tkinter.END)
    e7.delete(0, tkinter.END)


def Update():
    EmployeeId = e1.get()
    Name_of_Employee = e2.get()
    Age = e3.get()
    Phone_Number = e4.get()
    City_Name = e5.get()
    Skill = e6.get()
    Salary = e7.get()
    Update = "Update emp set Name_of_Employee ='%s', Age ='%s', Phone_Number='%s', City_Name='%s', Skill='%s', Salary='%s' where EmployeeId ='%s'" % (Name_of_Employee ,Age ,Phone_Number ,City_Name ,Skill ,Salary)
    mycursor.execute(Update) 
    mydb.commit()
    messagebox.showinfo("Info", "Record Update")




def Clear():
    e1.delete(0, tkinter.END)
    e2.delete(0, tkinter.END)
    e3.delete(0, tkinter.END)
    e4.delete(0, tkinter.END)
    e5.delete(0, tkinter.END)
    e6.delete(0, tkinter.END)
    e7.delete(0, tkinter.END)


button1 = tkinter.Button(root, text="Register", width=10, height=2,activebackground="red",
                 command=Register).grid(row=7, column=0)
button2 = tkinter.Button(root, text="Delete", width=10, height=2,activebackground="red",
                 command=Delete).grid(row=7, column=1)
button3 = tkinter.Button(root, text="Update", width=10, height=2,activebackground="red",
                 command=Update).grid(row=7, column=2)
button6 = tkinter.Button(root, text="Clear", width=10, height=2,activebackground="red",
                 command=Clear).grid(row=7, column=4)
root.mainloop()


