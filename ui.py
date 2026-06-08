import tkinter


vinduet=tkinter.Tk()
vinduet.geometry('1000x1000')

def Vektor2DLængde(x1,y1,x2,y2):
    
    længde1 =float(x1inputfelt.get())
    længde2=float(x2inputfelt.get())



x1inputfelt=tkinter.Entry(vinduet)
x1inputfelt.place(x=200,y=300)

x2inputfelt=tkinter.Entry(vinduet)
x2inputfelt.place(x=100,y=100)

xlabel=tkinter.Label(vinduet)
xlabel.place(x=500,y=500)
xlabel.config(text=længde1)





vinduet.mainloop()
