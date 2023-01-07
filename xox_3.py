from tkinter import *
from time import sleep

pen=Tk(className=" XOX Oyunu")
pen.geometry("500x500")

##buton fonksiyonlarının tanımlanması
def f00():
    main(0,0)
    
def f01():
    main(0,1)

def f02():
    main(0,2)
    
def f10():
    main(1,0)
    
def f11():
    main(1,1)
    
def f12():
    main(1,2)
    
def f20():
    main(2,0)
    
def f21():
    main(2,1)
    
def f22():
    main(2,2)

########################

def fretry():
    global sıra,x_durumu,o_durumu,tahta,hamleler,oskor,xskor
    tahta = [["___", "___", "___"],
             ["___", "___", "___"],
             ["___", "___", "___"]]
    skort.config(text="O = "+str(oskor)+"\nX = "+str(xskor))
    sıra=1
    hamleler=0
    x_durumu=[]
    o_durumu=[]
    işaret="O"
    for j in range(0,3):
        for k in range(0,3):
            exec("b"+str(j)+str(k)+"['state']= NORMAL")
            exec("b"+str(j)+str(k)+".config(text='__')")
            exec("tahta["+str(j)+"]["+str(k)+"]='__'")
    l.config(text="İşaret: O")
    bretry.place_forget()

##Butonların tanımlanması
#########################
b00=Button(pen)
b00.config(text="__",font=("Arial",30),command=f00)
b00.place(y=0,x=0)

b01=Button(pen)
b01.config(text="__",font=("Arial",30),command=f01)
b01.place(y=0,x=100)

b02=Button(pen)
b02.config(text="__",font=("Arial",30),command=f02)
b02.place(y=0,x=200)

b10=Button(pen)
b10.config(text="__",font=("Arial",30),command=f10)
b10.place(y=100,x=0)

b11=Button(pen)
b11.config(text="__",font=("Arial",30),command=f11)
b11.place(y=100,x=100)

b12=Button(pen)
b12.config(text="__",font=("Arial",30),command=f12)
b12.place(y=100,x=200)

b20=Button(pen)
b20.config(text="__",font=("Arial",30),command=f20)
b20.place(y=200,x=0in())

b21=Button(pen)
b21.config(text="__",font=("Arial",30),command=f21)
b21.place(y=200,x=100)

b22=Button(pen)
b22.config(text="__",font=("Arial",30),command=f22)
b22.place(y=200,x=200)

skort=Label(pen)
skort.config(text="O = 0\nX = 0",font=("Arial",35))
skort.place(y=100,x=300)

bretry=Button(pen)
bretry.config(text="Yeniden Oyna",font=("Arial",25),command=fretry)

l=Label(pen)
l.config(text="İşaret: O",font=("Arial",25))
l.place(x=100,y=300)



xskor=0
oskor=0

tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]

kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]

x_durumu = []
o_durumu = []

sıra = 1
hamleler=0

xskor=0
yskor=0

def main(x,y):
    global işaret,sıra,x_durumu,o_durumu,tahta,hamleler,xskor,oskor
    print(tahta)
    if sıra % 2 == 0:
         işaret = "X".center(3)
    else:
      işaret = "O".center(3)

    hamleler+=1

    if işaret=="X".center(3):
        l.config(text="İşaret: O")
    else:
        l.config(text="İşaret: X")


    tahta[x][y] = işaret
    if işaret == "X".center(3):
        x_durumu += [[x, y]]
    elif işaret == "O".center(3):
        o_durumu += [[x, y]]
    sıra += 1
    exec("b"+str(x)+str(y)+".config(text=tahta[x][y])")
    exec("b"+str(x)+str(y)+"['state']= DISABLED")

    for i in kazanma_ölçütleri:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]

        if len(o) == len(i):
            l.config(text="O kazandı")
            oskor+=1
            for j in range(0,3):
                for k in range(0,3):
                    exec("b"+str(j)+str(k)+"['state']= DISABLED")
            bretry.place(x=65,y=350)
            
            
        elif len(x) == len(i):
            l.config(text="X kazandı")
            xskor+=1
            for j in range(0,3):
                for k in range(0,3):
                    exec("b"+str(j)+str(k)+"['state']= DISABLED")

            bretry.place(x=65,y=350)
    if hamleler==10:
        l.config(text="Berabere")
        bretry.place(x=65,y=350)
            
mainloop()
