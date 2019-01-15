from tkinter import *

from tkinter import ttk

from urllib.request import Request,urlopen

from threading import Thread

import os

def download():
    
    a=os.path.expanduser('~')
    
    downloads=os.path.join(a,"Downloads")
    
    return downloads



window=Tk()

#window.state("zoomed")

window.title("File Downloader")

window.configure(height=650,width=600)

frame=Frame(window)

frame.configure(height=450,width=550)

frame.place(relx=0.5,rely=0.4,anchor=CENTER)



def check():

    
    inp_url=url_in.get().strip()

    try:

        a=Request(inp_url, headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"})

    except:
        
        Label(frame,text="Invalid URL", width=50,bg="#c0dfd9").place(relx=0.5,y=400,anchor=CENTER)

    else:

        global b

        b=urlopen(a)

        try:
            global d

            d=round(int(b.info()["Content-Length"])/(1024*1024),2)
            
        except:
            
            d="size not available"

        Label(frame,text=str(d),width=15,bg="#c0dfd9").place(relx=0.5,y=160,anchor=CENTER)

        inp_fn=file_in.get().strip()

        Button(frame,text="Download",width=25,bg="#b3c2bf",command=onclick).place(x=280,y=300)


        


def onclick():
    
    Thread(target=dwn).start()
    

def dwn():

    '''inp_url=url_in.get().strip()

    a=Request(inp_url, headers={'User-Agent': res_in.get()})

    b=urlopen(a)
    
    txtdis="" '''

    inp_fn=file_in.get().strip()

    if inp_fn=="":
        
        inp_fn="Vinay.zip"

    with open(download()+"\\"+inp_fn, "wb") as fo:

        block_s=1024*1024

        f_s=0

        while True:

            buffer=b.read(block_s)

            if not buffer:

                txtdis="Download Completed"

                Label(frame,text=txtdis, width=50,bg="#c0dfd9").place(relx=0.5,y=400,anchor=CENTER)

                ttk.Progressbar(frame,orient="horizontal",maximum=100,length=300,mode="determinate",value=100).place(relx=0.5,y=350,anchor=CENTER)

                break

            f_s+=len(buffer)

            fo.write(buffer)

            c_s=f_s//(1024*1024)

            perc=int((c_s/d)*100)

            ttk.Progressbar(frame,orient="horizontal",maximum=100,length=300,mode="determinate",value=perc).place(relx=0.5,y=350,anchor=CENTER)




url_in=StringVar()

file_in=StringVar()

Label(frame,text="URL", width=15,bg="#c0dfd9").place(x=10,y=50)

ent1=Entry(frame,textvariable=url_in,width=48)

ent1.focus()

ent1.place(x=150,y=50)

Label(frame,text="File Name", width=15,bg="#c0dfd9").place(x=10,y=230)

Entry(frame,textvariable=file_in,width=50).place(x=150,y=230)

Label(frame,text="File Size", width=15,bg="#c0dfd9").place(relx=0.5,y=110,anchor=CENTER)

Button(frame,text="Check",width=10,bg="#b3c2bf",command=check).place(x=460,y=48)

Button(frame,text="Exit",width=40,bg="#b3c2bf",command=window.destroy).place(relx=0.5,rely=0.9,anchor=S)

window.mainloop()
