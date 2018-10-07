from pytube import YouTube

from tkinter import *

from urllib.request import Request,urlopen

from winreg import *

import _thread

global Downloads

with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

window=Tk()

screen_width = window.winfo_screenwidth()

screen_height = window.winfo_screenheight()

window.state("zoomed")

window.title("Downloader")

frame=Frame(window)

frame.configure(height=450,width=550)

frame.place(relx=0.5,rely=0.4,anchor=CENTER)



def check():

    
    inp_url=url_in.get().strip()

    try:

        a=Request(inp_url, headers={'User-Agent': res_in.get()})

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

        Label(frame,text=str(d), width=15,bg="#c0dfd9").place(x=150,y=110)


        inp_fn=file_in.get().strip()

        


def onclick():
    _thread.start_new_thread(dwn,())
    

def dwn():

    '''inp_url=url_in.get().strip()

    a=Request(inp_url, headers={'User-Agent': res_in.get()})

    b=urlopen(a)
    
    txtdis="" '''

    inp_fn=file_in.get().strip()

    if inp_fn=="":
        
        inp_fn="Vinay.zip"

    with open(Downloads+"\\"+inp_fn, "wb") as fo:

        block_s=1024*1024

        f_s=0

        while True:

            buffer=b.read(block_s)

            if not buffer:

                txtdis="Download Completed"

                Label(frame,text=txtdis, width=50,bg="#c0dfd9").place(relx=0.5,y=400,anchor=CENTER)

                break

            f_s+=len(buffer)

            fo.write(buffer)

            c_s=f_s//(1024*1024)

            perc=int((c_s/d)*100)

            txtdis="Downloading...."+str(c_s)+"MB  "+str(perc)+"%"

            Label(frame,text=txtdis, width=50,bg="#c0dfd9").place(relx=0.5,y=400,anchor=CENTER)

            #Label(frame,text=str(perc), width=perc//2,bg="#c0dfd9").place(relx=0.5,y=430,anchor=CENTER)

    



url_in=StringVar()

file_in=StringVar()

res_in=StringVar()

Label(frame,text="URL", width=15,bg="#c0dfd9").place(x=10,y=50)

ent1=Entry(frame,textvariable=url_in,width=48)

ent1.focus()

ent1.place(x=150,y=50)

Label(frame,text="User Agent", width=15,bg="#c0dfd9").place(x=10,y=170)

rad=Radiobutton(frame,text="Mozilla",variable=res_in,value="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",width=10,bg="#c0dfd9")

rad.select()

rad.place(x=150,y=170)

Radiobutton(frame,text="Android",variable=res_in,value="Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",width=10,bg="#c0dfd9").place(x=280,y=170)


Radiobutton(frame,text="IOS",variable=res_in,value="Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",width=10,bg="#c0dfd9").place(x=410,y=170)


Label(frame,text="File Name", width=15,bg="#c0dfd9").place(x=10,y=230)

Entry(frame,textvariable=file_in,width=50).place(x=150,y=230)

Label(frame,text="File Size", width=15,bg="#c0dfd9").place(x=10,y=110)

Button(frame,text="Check",width=10,bg="#b3c2bf",command=check).place(x=460,y=48)

Button(frame,text="Download",width=25,bg="#b3c2bf",command=onclick).place(x=280,y=300)

Button(frame,text="Exit",width=25,bg="#b3c2bf",command=window.destroy).place(x=50,y=300)


window.mainloop()
