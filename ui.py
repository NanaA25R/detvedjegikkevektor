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



def beregnLængde():
    x1=float(x1inputfelt.get())     #print vitkrt
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

x37inputfelt=tkinter.Entry(vinduet)
x37inputfelt.config(width=10)
x37inputfelt.place(x=620,y=65)

x38inputfelt=tkinter.Entry(vinduet)
x38inputfelt.config(width=10)
x38inputfelt.place(x=700,y=65)



def beregn2Dog3Dminus():
    x1 =float(x3inputfelt.get())
    y1 =float(x4inputfelt.get())        #print vitkrt

    x2 =float(x5inputfelt.get())
    y2 =float(x6inputfelt.get())

    hey.Vektor2Dminus (x1,y1,x2,y2)
     

    if(x37inputfelt.get()!="" and x38inputfelt.get()!=""):  
        z1=float(x37inputfelt.get())
        z2=float(x38inputfelt.get())
        hey.Vektor3Dminus (x1,y1,x2,y2,z1,z2)

        

   
    
#knap
Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=beregn2Dog3Dminus)
Knap2.place(x=480,y=100)  

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

x111label=tkinter.Label(vinduet)
x111label.config(text="z1")
x111label.place(x=635,y=40)

x112label=tkinter.Label(vinduet)
x112label.config(text="z1")
x112label.place(x=730,y=40)

x113label=tkinter.Label(vinduet)
x113label.config(text="minusværdien af v1-v2 er")
x113label.place(x=300,y=130)

x114label=tkinter.Label(vinduet)
x114label.config(text="")
x114label.place(x=340,y=130)





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

x300inputfelt=tkinter.Entry(vinduet)
x300inputfelt.config(width=10)
x300inputfelt.place(x=300,y=210)




def BeregnVektor2DlægdeAFplus():
    x1 = float(x9inputfelt.get())   #Print virker
    y1 = float(x10inputfelt.get())
    x2 = float(x11inputfelt.get())
    y2 = float(x300inputfelt.get())

    
    længdeAfplus= hey.Vektor2DlægdeAFplus(x1,x2,y1,y2)     
    

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
x12inputfelt.place(x=1000,y=65)

x13inputfelt=tkinter.Entry(vinduet)
x13inputfelt.config(width=10)
x13inputfelt.place(x=1080,y=65)

x14inputfelt=tkinter.Entry(vinduet)
x14inputfelt.config(width=10)
x14inputfelt.place(x=860,y=65)

x15inputfelt=tkinter.Entry(vinduet)
x15inputfelt.config(width=10)
x15inputfelt.place(x=940,y=65)



def beregnSkallar2Dog3D():
    x1= float(x12inputfelt.get())                      #print printer virker
    y1= float(x13inputfelt.get())
    s = float(x15inputfelt.get())

    skallarpruduktX, skallarpruduktY=hey.skallar2D(x1,y1,s)

    x22label=tkinter.Label(vinduet)                    
    x22label.config(text = f"Resultater: ({skallarpruduktX}, {skallarpruduktY})")
    x22label.place(x=800,y=800) 


    if(x14inputfelt.get()!=""):
        z1= float(x14inputfelt.get())

        skallarpruduktX,skallarpruduktY,skallarpruduktZ=hey.skallar3D(x1,y1,z1,s)

        x23label=tkinter.Label(vinduet)                    
        x23label.config(text = f"Resultater: ({skallarpruduktX}, {skallarpruduktY},{skallarpruduktZ})")
        x23label.place(x=850,y=800) 


        
 


    

#knap
Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=beregnSkallar2Dog3D)
Knap2.place(x=765,y=100)  






def vektor3DOG2Dvinkel():
    x1=float()
    y1=float()
    x2=float()
    y2=float()                      #har ikke kigget på
    z1=float()
    z2=float()

    if(x1 and y1 and x2 and y2):
        Vinkel=hey.Vektor2Dvinkel (x1,y1,x2,y2)

        x24label=tkinter.Label(vinduet)                    
        x24label.config(text = Vinkel)
        x24label.place(x=850,y=800) 
    
    if(x1 and y1 and x2 and y2 and z1 and z2):
        Vinkel=hey.Vektor3Dvinkel (x1,y1,x2,y2,z1,z2)
        x24label=tkinter.Label(vinduet)                    
        x24label.config(text = Vinkel3D)
        x24label.place(x=850,y=800) 



    

x16inputfelt=tkinter.Entry(vinduet)
x16inputfelt.config(width=10)
x16inputfelt.place(x=540,y=360)

x17inputfelt=tkinter.Entry(vinduet)
x17inputfelt.config(width=10)
x17inputfelt.place(x=460,y=360)

x18inputfelt=tkinter.Entry(vinduet)
x18inputfelt.config(width=10)
x18inputfelt.place(x=380,y=360)

x19inputfelt=tkinter.Entry(vinduet)
x19inputfelt.config(width=10)
x19inputfelt.place(x=300,y=360)



def krydsvektor3D():
    x1=float(x16inputfelt.get())             #insæt inputfleter
    x2=float(x17inputfelt.get())
    y1=float(x18inputfelt.get())
    y2=float(x19inputfelt.get())
    z1=float()
    z2=float()

    Xverdien,Yverdien,Zverdien=hey.krydsvektor3D(x1,x2,y1,y2,z1,z2)

    x24label=tkinter.Label(vinduet)                    
    x24label.config(text = f"Resultater: ({Xverdien}, {Yverdien},{Zverdien})")
    x24label.place(x=900,y=800) 


Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=krydsvektor3D)
Knap2.place(x=400,y=400)  








x20inputfelt=tkinter.Entry(vinduet)
x20inputfelt.config(width=10)
x20inputfelt.place(x=120,y=210)

x21inputfelt=tkinter.Entry(vinduet)
x21inputfelt.config(width=10)
x21inputfelt.place(x=40,y=210)

def polærTilKartasian():
    v = float(x20inputfelt.get())
    l = float(x21inputfelt.get())         #print virker

    x1,y1=hey.polærTilKartasian(v,l)

    x25label=tkinter.Label(vinduet)                    
    x25label.config(text = f"Resultater: ({x1}, {y1})")
    x25label.place(x=900,y=800) 


Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=polærTilKartasian)
Knap2.place(x=60,y=250)  







x22inputfelt=tkinter.Entry(vinduet)
x22inputfelt.config(width=10)
x22inputfelt.place(x=120,y=360)

x23inputfelt=tkinter.Entry(vinduet)
x23inputfelt.config(width=10)
x23inputfelt.place(x=40,y=360)



def KartasianTilPolær():
    x1 = float(x22inputfelt.get())
    y1 = float(x23inputfelt.get())

    v,l=hey.KartasianTilPolær(x1,y1)      #printer virker

    x26label=tkinter.Label(vinduet)                    
    x26label.config(text = f"Resultater: ({v}, {l})")
    x26label.place(x=900,y=800) 


Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=KartasianTilPolær)      #knap er skæv
Knap2.place(x=60,y=420) 





#x24inputfelt=tkinter.Entry(vinduet)
#x24inputfelt.config(width=10)
#x24inputfelt.place(x=120,y=360)

#x25inputfelt=tkinter.Entry(vinduet)
#x25inputfelt.config(width=10)
#x25inputfelt.place(x=40,y=360)

#x26inputfelt=tkinter.Entry(vinduet)
#x26inputfelt.config(width=10)
#x26inputfelt.place(x=120,y=360)



def enhedsvektor2D ():
    x1=float()                                       #MANGLER INPUTFELTER OG PLACERING
    y1=float()
    z1=float()

    if(x1 and y1):
        længde = hey.enhedsvektor2D(x1,y1)

        x27label=tkinter.Label(vinduet)                    
        x27label.config(text = f"Resultater: ({x},{y})")
        x27label.place(x=900,y=800) 



    if(x1 and y1 and z1):
        længde = hey.enhedsvektor3D (x1,y1,z1)

        x28label=tkinter.Label(vinduet)                    
        x28label.config(text = f"Resultater: ({x},{y},{z})")
        x28label.place(x=900,y=800) 




#def projektionA(x1,y1,z1,x2,y2,z2):
    #if z1 == None:
        # z1 = 0
    #if z2 == None:
       #  z2 = 0
    #Dot = (x1*x2+y1*y2+z1*z2)
   # A = math.sqrt(x1**2+y1**2+z1**2)
   # Projektion= Dot/A
   # return(Projektion)

#def projektionB(x1,y1,z1,x2,y2,z2):
   # if z1 == None:
       #  z1 = 0
   # if z2 == None:
       #  z2 = 0
   # Dot = (x1*x2+y1*y2+z1*z2)
   # B = math.sqrt(x2**2+y2**2+z2**2)
   # Projektion= Dot/B
   # return(Projektion)






def tværvektor2d ():
    x1 = float()           #mangler inoutfleter og knap
    y1 = float()

    tvær= hey.tværvektor2d(x1,y1)

    x29label=tkinter.Label(vinduet)                    
    x29label.config(text = tvær)
    x29label.place(x=900,y=800)






x27inputfelt=tkinter.Entry(vinduet)
x27inputfelt.config(width=10)
x27inputfelt.place(x=300,y=650)

x28inputfelt=tkinter.Entry(vinduet)
x28inputfelt.config(width=10)
x28inputfelt.place(x=380,y=650)

x29inputfelt=tkinter.Entry(vinduet)
x29inputfelt.config(width=10)
x29inputfelt.place(x=460,y=650)

x30inputfelt=tkinter.Entry(vinduet)
x30inputfelt.config(width=10)
x30inputfelt.place(x=540,y=650)


def Beregnpunktvektor ():
    x1 = float(x27inputfelt.get())    #print virekr
    y1 = float(x28inputfelt.get())                   
    x2 = float(x29inputfelt.get())
    y2 = float(x30inputfelt.get())

    vektorx,vektory = hey.punktvektor (x1,y1,x2,y2)


    x30label=tkinter.Label(vinduet)                    
    x30label.config(text =f"Resultater: ({vektorx},{vektory})" )
    x30label.place(x=900,y=800)



Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=Beregnpunktvektor)     
Knap2.place(x=400,y=680) 



x31inputfelt=tkinter.Entry(vinduet)
x31inputfelt.config(width=10)
x31inputfelt.place(x=860,y=210)

x32inputfelt=tkinter.Entry(vinduet)
x32inputfelt.config(width=10)
x32inputfelt.place(x=940,y=210)

x33inputfelt=tkinter.Entry(vinduet)
x33inputfelt.config(width=10)
x33inputfelt.place(x=1020,y=210)

x34inputfelt=tkinter.Entry(vinduet)
x34inputfelt.config(width=10)
x34inputfelt.place(x=1100,y=210)

x35inputfelt=tkinter.Entry(vinduet)
x35inputfelt.config(width=10)
x35inputfelt.place(x=1180,y=210)

x36inputfelt=tkinter.Entry(vinduet)
x36inputfelt.config(width=10)
x36inputfelt.place(x=1260,y=210)




def BergenPrikprodukt():
    print("før")
    x1=float(x31inputfelt.get())           #mangler inputgleter + knap
    y1=float(x32inputfelt.get())
    x2= float(x33inputfelt.get())
    y2=float(x34inputfelt.get())
    z1=float(x35inputfelt.get())
    z2=float(x36inputfelt.get())

    print("efter")


    Dot,LængdeV1,LængdeV2,Theta = hey.Prikprodukt(x1,y1,x2,y2,z1,z2)
    print("officel efter")
    #Dot=
    #LængdeV1=
    #LængdeV2=
    #Theta= hey.

    
Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=BergenPrikprodukt)     
Knap2.place(x=1000,y=260) 






















    
    








         









    




















































vinduet.mainloop()
