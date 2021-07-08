from tkinter import *
import sys
from PIL import Image,ImageTk

root=Tk()
root.title("image viewer")
root.geometry("800x730")
label_mem=Label(root,text="MEMORIES",font=("algerian",50),fg="grey50")
label_mem.place(relx=0.5,y=50,anchor=CENTER)
#root.configure(bg="")
root.iconbitmap("C:/python/projects/bw_Tulip.jpg")

root.resizable(height=False,width=False)
list_names=["C:/manali/IMG20191018153141.jpg",
            "C:/manali/IMG20191019112631.jpg",
            "C:/manali/IMG20191019112300.jpg",
            "C:/manali/IMG20191019105217.jpg",
            "C:/manali/IMG20191019184252.jpg",
            "C:/manali/IMG-20191019-WA0057.jpg",
            "C:/manali/IMG-20191018-WA0032.jpg",
            "C:/manali/IMG20191017234912.jpg",
            "C:/manali/IMG20191020065210.jpg"]
list_images=[]
sizes=[]
count=0
for i in range(len(list_names)):
    img=Image.open(list_names[i])
    fixed_height=450
    ratio=(int(img.size[1])/int(img.size[0]))
    newwidth=int(fixed_height/ratio)
    img=img.resize((newwidth,fixed_height),Image.NEAREST)
    sizes.append([newwidth,fixed_height])
    imgtk=ImageTk.PhotoImage(img)
    list_images.append(imgtk)
    

frame1=Frame(root,bg="grey70",width=sizes[0][0]+50,height=sizes[0][1]+50)
frame1.place(relx=0.5,rely=0.5,anchor=CENTER)
label1=Label(image=list_images[0])
label1.place(relx=0.5,rely=0.5,anchor=CENTER)

def forward():
    global label1
    global count
    global button_forward
    global button_back
    global frame1
    count=count+1
    if count==(len(list_names)-1):
        button_forward.config(state=DISABLED)
        
    if count>0:
        button_back.config(state=ACTIVE)
    label1.place_forget()
    frame1.place_forget()
    frame1=Frame(root,bg="grey70",width=sizes[count][0]+50,height=sizes[count][1]+50)
    frame1.place(relx=0.5,rely=0.5,anchor=CENTER)
    label1=Label(image=list_images[count])
    label1.place(relx=0.5,rely=0.5,anchor=CENTER)
    label2.config(text="images "+str(count+1)+" of "+str(len(list_names)))
def backward():
    global label1
    global count
    global button_back
    global button_forward
    global frame1
    count=count-1
    if count<(len(list_names)-1):
        button_forward.config(state=ACTIVE)
    if count==0:
        button_back.config(state=DISABLED)
    frame1.place_forget()
    label1.place_forget()
    frame1=Frame(root,bg="grey70",width=sizes[count][0]+50,height=sizes[count][1]+50)
    frame1.place(relx=0.5,rely=0.5,anchor=CENTER)
    label1=Label(image=list_images[count])
    label1.place(relx=0.5,rely=0.5,anchor=CENTER)
    label2.config(text="images "+str(count+1)+" of "+str(len(list_names)))
    

button_back=Button(root,text="<<",state=DISABLED,padx=10,font=("arial",22),fg="black",bg="grey80",command=backward)
button_back.place(x=300,y=630)

button_forward=Button(root,text=">>",state=ACTIVE,padx=10,justify=LEFT,font=("arial",22),bg="grey80",fg="black",command=forward)
button_forward.place(x=450,y=630)

button_exit=Button(root,text="exit",font=("helvatica",22),command=root.destroy)
button_exit.place(x=380,y=630)
label2=Label(root,text="Images 1 of "+str(len(list_names)),font=("helvatica",15),bg="grey80",bd=2,relief=SUNKEN)
label2.place(relx=0.5,rely=1,bordermode=OUTSIDE,width=800,anchor=S)
root.mainloop()



    
    
