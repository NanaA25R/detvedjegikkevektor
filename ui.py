import hey
import tkinter


vinduet=tkinter.Tk()
vinduet.geometry('2000x2000')

       


#Inputfelter
x1inputfelt=tkinter.Entry(vinduet)
x1inputfelt.config(width=10)
x1inputfelt.place(x=120,y=65)

x2inputfelt=tkinter.Entry(vinduet)
x2inputfelt.config(width=10)
x2inputfelt.place(x=40,y=65)



#Henter information fra input ind til knappen
def beregnLængde():
    x1=float(x1inputfelt.get())
    y1=float(x2inputfelt.get())


    if(x1!=""and y1!=""):
        længde=hey.Vektor2DLængde (x1,y1)
                                                
        x5label=tkinter.Label(vinduet)                    
        x5label.config(text = længde)
        x5label.place(x=135,y=150) 

    

#knap
Knap1=tkinter.Button(vinduet)
Knap1.config(width=12,text="Beregn",command=beregnLængde)
Knap1.place(x=70,y=100)  

#Label
x1label=tkinter.Label(vinduet)
x1label.config(text="x")
x1label.place(x=60,y=40)

x2label=tkinter.Label(vinduet)
x2label.config(text="y")
x2label.place(x=130,y=40)

x4label=tkinter.Label(vinduet)                  
x4label.config(text="længden af vektoren er")
x4label.place(x=5,y=150) 

#overskrift 
x3label=tkinter.Label(vinduet)
x3label.config(text="Finde længden på en vektor")
x3label.place(x=8,y=10)

#______________________


#man minuser to vektor og får en vektor som er differancen på de to andre vektor
x3inputfelt=tkinter.Entry(vinduet)
x3inputfelt.config(width=10)
x3inputfelt.place(x=300,y=65)

x4inputfelt=tkinter.Entry(vinduet)
x4inputfelt.config(width=10)
x4inputfelt.place(x=380,y=65)

x5inputfelt=tkinter.Entry(vinduet)
x5inputfelt.config(width=10)
x5inputfelt.place(x=460,y=65)

x6inputfelt=tkinter.Entry(vinduet)
x6inputfelt.config(width=10)
x6inputfelt.place(x=540,y=65)


#VIRKER IKKE 
def beregn2Dminus():
    x1 =float(x3inputfelt.get())
    y1 =float(x4inputfelt.get())

    x2 =float(x5inputfelt.get())
    y2 =float(x6inputfelt.get())
     

    if(x1!=""and y1!="" and x2!="" and y2!=""):     
        x1=hey.Vektor2Dminus (x1,y1,x2,y2)
        y1=hey.Vektor2Dminus(x1,y1,x2,y2)

        x2=hey.Vektor2Dminus(x1,y1,x2,y2)
        y2=hey.Vektor2Dminus(x1,y1,x2,y2)




#knap
Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=beregn2Dminus)
Knap2.place(x=400,y=100)  

#Label
x5label=tkinter.Label(vinduet)
x5label.config(text="x1")
x5label.place(x=320,y=40)

x6label=tkinter.Label(vinduet)
x6label.config(text="y1")
x6label.place(x=400,y=40)

x7label=tkinter.Label(vinduet)
x7label.config(text="x2")
x7label.place(x=480,y=40)

x8label=tkinter.Label(vinduet)
x8label.config(text="y2")
x8label.place(x=560,y=40)





#def Vektor3Dminus
#def vektor2Dplus
#def vektor3Dplus





#inputfelter
x9inputfelt=tkinter.Entry(vinduet)
x9inputfelt.config(width=10)
x9inputfelt.place(x=540,y=210)

x10inputfelt=tkinter.Entry(vinduet)
x10inputfelt.config(width=10)
x10inputfelt.place(x=460,y=210)

x11inputfelt=tkinter.Entry(vinduet)
x11inputfelt.config(width=10)
x11inputfelt.place(x=380,y=210)

x12inputfelt=tkinter.Entry(vinduet)
x12inputfelt.config(width=10)
x12inputfelt.place(x=300,y=210)








def BeregnVektor2DlægdeAFplus():
    x1 = float(x9inputfelt.get())   #inputfelt og get
    y1 = float(x10inputfelt.get())
    x2 = float(x11inputfelt.get())
    y2 = float(x12inputfelt.get())

    
    længdeAfplus=hey.Vektor2DlægdeAFplus(x1,x2,y1,y2)     
    

    x10label=tkinter.Label(vinduet)                    
    x10label.config(text = længdeAfplus)
    x10label.place(x=1000,y=1000) 

   


#Knap
Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=BeregnVektor2DlægdeAFplus)
Knap2.place(x=400,y=250)




#inputfelter
x12inputfelt=tkinter.Entry(vinduet)
x12inputfelt.config(width=10)
x12inputfelt.place(x=700,y=65)

x13inputfelt=tkinter.Entry(vinduet)
x13inputfelt.config(width=10)
x13inputfelt.place(x=780,y=65)

x14inputfelt=tkinter.Entry(vinduet)
x14inputfelt.config(width=10)
x14inputfelt.place(x=860,y=65)





def beregnSkallar2Dog3D():
    x1= float(x12inputfelt.get())
    y1= float(x13inputfelt.get())
    s = float(x14inputfelt.get())

    skallarpruduktX,skallarpruduktY=hey.skallar2D(x1,y1,s)

    x22label=tkinter.Label(vinduet)                    
    x22label.config(text = f"Resultater: ({skallarpruduktY}, {skallarpruduktX})")
    x22label.place(x=800,y=800) 
    

#knap
Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=beregnSkallar2Dog3D)
Knap2.place(x=765,y=100)  






def skallar2D (x1,y1,s):
    skallarpruduktX = (x1*s) 
    skallarpruduktY = (y1*s) 
    print(skallarpruduktY)
    print(skallarpruduktX)

    








         









    




















































vinduet.mainloop()
