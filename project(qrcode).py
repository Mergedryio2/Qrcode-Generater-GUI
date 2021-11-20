from tkinter import *
from PIL import Image , ImageTk
from tkinter.filedialog import *
import os
i = 0
qrimg,photoqr,old_name,box,new_name,imagefile,deltxt,e,box3,button2,found,imgfind = "","","","","","","","","","","",""
#หน้าจอที่ 1
root = Tk()
root.title("Save Qrcode")
root.geometry("400x600+600+200")
image_extension = []
matching = []
#การแสดงผล
txt,txt2,downtxt = StringVar() , StringVar(),StringVar()
head = Label(text="Qrcode",fg="black",bg="sky blue",font=30).pack(fill=X)
listbox = Listbox(root)
def list_images():
    global qrimg , photoqr , imagefile,image_extension
    #เปิดไฟล์เพื่อแสดงผลภาพ
    imagefile = askopenfilename(initialdir="E:\\Desktop\\python code in VS", title="Select A File",filetypes=(("PNG Files", "*.png"),))
    #เอาที่อยู่ภาพไปเก็บไว้ในลิสต์
    if imagefile in image_extension:
        print("It has in list already!")
    else:
        image_extension.append(imagefile)
        print(image_extension)
def changename():
    #เปลี่ยนชื่อไฟล์
    box2 = Entry(root,textvariable=txt2,font=20)
    box2.pack(fill=X)
    button1 = Button(text="change",fg="black",font=15,command=changefile)
    button1.pack()
def changefile():
    #เปลี่ยนชื่อไฟล์
    global imagefile
    newmassage = txt2.get()
    old_name = str(imagefile)
    new_name = "E:/Desktop/python code in VS/"+str(newmassage)+".png"
    os.rename(old_name, new_name)
def clear():
    global qrimg
    qrimg = Label(image= None).pack()
def find():
    global box3,button2
    box3 = Entry(root,textvariable=txt,font=20)
    box3.pack(fill=X)
    button2 = Button(text="Show",fg="black",font=15,command=findfile)
    button2.pack()
def findfile():
    global   found,qrimg , photoqr ,matching
    found = txt.get()
    print(found)
    matching = [s for s in image_extension ]
    qrimg = ImageTk.PhotoImage(Image.open("E:/Desktop/python code in VS/"+found+".png"))
    photoqr = Label(image=qrimg).pack()
    
button1 = Button(text="choose file",fg="black",font=15,command=list_images).pack(side=TOP,fill=X)
button3 = Button(text="Change Name",fg="black",font=15,command=changename).pack(side=TOP,fill=X)
button4 = Button(text="Clear",fg="black",font=15,command=clear).pack(side=TOP,fill=X)
button5 = Button(text="Find",fg="black",font=15,command=find).pack(side=TOP,fill=X)
root.mainloop()