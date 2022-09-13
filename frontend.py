from tkinter import *
import backend
import datetime

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]#this [0] means we are taking just first item in tuple, like we just get number not tuple
    selected_tuple=list1.get(index) #this let take us all of the elements form tuple. Sooo ISBN, author or title
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0, END)
    e5.insert(END, selected_tuple[5])
    e6.delete(0, END)
    e6.insert(END, selected_tuple[6])
    e7.delete(0, END)
    e7.insert(END, selected_tuple[7])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(), title_author.get(), title_year.get(), title_ISBN.get(), title_borrow.get(), title_return.get(), title_name.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title_text.get(), title_author.get(), title_year.get(), title_ISBN.get(), title_name.get())
    list1.delete(0, END)
    list1.insert(END,( title_text.get(), title_author.get(), title_year.get(), title_ISBN.get(), title_name.get()))


    
def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0],title_text.get(), title_author.get(), title_year.get(), title_ISBN.get(), title_borrow.get(), title_return.get(), title_name.get())
    view_command()

window= Tk()

window.wm_title('Bookstore')

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

l5=Label(window,text="Borrow date")
l5.grid(row=0,column=4)

l6=Label(window,text="Return date")
l6.grid(row=1,column=4)

l6=Label(window,text="Mate name")
l6.grid(row=2,column=4)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

title_author=StringVar()
e2=Entry(window,textvariable=title_author)
e2.grid(row=0,column=3)

title_year=StringVar()
e3=Entry(window,textvariable=title_year)
e3.grid(row=1,column=1)

title_ISBN=StringVar()
e4=Entry(window,textvariable=title_ISBN)
e4.grid(row=1,column=3)

title_borrow=StringVar()
e5=Entry(window,textvariable=title_borrow)
e5.grid(row=0,column=5)

title_return=StringVar()
e6=Entry(window,textvariable=title_return)
e6.grid(row=1,column=5)

title_name=StringVar()
e7=Entry(window,textvariable=title_name)
e7.grid(row=2,column=5)

list1=Listbox(window,height=10, width=60)
list1.grid(row=2,column=0,rowspan=7,columnspan=4)

sb1=Scrollbar(window)
#sb1.grid(row=2,column=2,rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview())

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all",width=12, command=view_command)
b1.grid(row=3, column=5)
b2=Button(window,text="Search",width=12, command=search_command)
b2.grid(row=4, column=5)
b3=Button(window,text="Add",width=12, command=add_command)
b3.grid(row=5, column=5)
b4=Button(window,text="Update",width=12, command=update_command)
b4.grid(row=6, column=5)
b5=Button(window,text="Delete",width=12, command=delete_command)
b5.grid(row=7, column=5)
b6=Button(window,text="Close",width=12, command=window.destroy)
b6.grid(row=8, column=5)

window.mainloop()
print(type(datetime.date.today()))