import hey
import tkinter
import matplotlib.pyplot as plt


vinduet=tkinter.Tk()
vinduet.geometry('2000x2000')

#visuell
def tegn(x1, y1 ):

    plt.arrow(0,0,x1,y1,color="blue",
    head_width=0.2,
    length_includes_head=True)

    plt.grid()
    plt.axis("equal")
    plt.show()



def tegn2D(x1, y1, x2,y2,plusX,plusY,plusZ,s):

    plt.arrow(0,0,x1,y1,color="blue",
    head_width=0.2,
    length_includes_head=True)

    plt.arrow(0,0,x2,y2,color="red",
    head_width=0.2,
    length_includes_head=True)

    plt.arrow(0,0,plusX,plusY,color="green",
    head_width=0.2,
    length_includes_head=True)

    plt.arrow(0,0,plusX,plusY,plusZ,color="black",
    head_width=0.2,
    length_includes_head=True)

    plt.arrow(0,0,x1,y1,s,color="pink",
    head_width=0.2,
    length_includes_head=True)

    


    plt.grid()
    plt.axis("equal")
    plt.show()



def tegn3D(x1, y1, x2,y2,z1,z2):
    
    plt.arrow(0,0,x1,y1,color="blue",
    head_width=0.2,
    length_includes_head=True)

    plt.arrow(0,0,x2,y2,color="red",
    head_width=0.2,
    length_includes_head=True)

    
    plt.arrow(0,0,z1,z2,color="green",
    head_width=0.2,
    length_includes_head=True)

    plt.grid()
    plt.axis("equal")
    plt.show()

    
def tegn3D3(x1, y1, z1):
    
    plt.arrow(0,0,x1,y1,z1,color="blue",
    head_width=0.2,
    length_includes_head=True)


    plt.grid()
    plt.axis("equal")
    plt.show()


    
def tegn22(x1, y1 ,x2,y2):

    plt.arrow(0,0,x1,y1,color="blue",
    head_width=0.2,
    length_includes_head=True)
    
    plt.arrow(0,0,x2,y2,color="blue",
    head_width=0.2,
    length_includes_head=True)

    plt.grid()
    plt.axis("equal")
    plt.show()



       


#Inputfelter
x1inputfelt=tkinter.Entry(vinduet)
x1inputfelt.config(width=10)
x1inputfelt.place(x=120,y=65)

x2inputfelt=tkinter.Entry(vinduet)
x2inputfelt.config(width=10)
x2inputfelt.place(x=40,y=65)



def beregnLængde():
    x1=float(x1inputfelt.get())     
    y1=float(x2inputfelt.get())                 


    if(x1!=""and y1!=""):
        længde=hey.Vektor2DLængde (x1,y1)

        tegn (x1,y1)
        
                                                
        x5label=tkinter.Label(vinduet)                    
        x5label.config(text = længde)
        x5label.place(x=150,y=150) 

    

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
x4label.place(x=40,y=150) 

#overskrift 
x3label=tkinter.Label(vinduet)
x3label.config(text="længden af vektor")
x3label.place(x=8,y=10)

#______________________


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
    
    x1 = float(x3inputfelt.get())
    y1 = float(x4inputfelt.get())

    x2 = float(x5inputfelt.get())
    y2 = float(x6inputfelt.get())

    if (x37inputfelt.get() != "" and x38inputfelt.get() != ""):

        z1 = float(x37inputfelt.get())
        z2 = float(x38inputfelt.get())

        minus1X2, minus1Y2, minus1Z2, minus2X1, minus2Y1, minus2Z1 = hey.Vektor3Dminus(x1, y1, x2, y2, z1, z2)

        tegn3D(x1, y1, x2, y2, z1, z2)

        x114label = tkinter.Label(vinduet)
        x114label.config(text=f"{minus1X2} , {minus1Y2}, {minus1Z2}")
        x114label.place(x=450, y=130)

        x115label=tkinter.Label(vinduet)
        x115label.config(text=f"{minus2X1} , {minus2Y1} , {minus2Z1}")
        x115label.place(x=450,y=150) 

        
        x113label=tkinter.Label(vinduet)
        x113label.config(text="minusværdien af v1-v2 er")
        x113label.place(x=300,y=130)

        x222label=tkinter.Label(vinduet)
        x222label.config(text="minusværdien af v2-v1 er")
        x222label.place(x=300,y=150)



    if(x37inputfelt.get() == "" and x38inputfelt.get() == ""):

        minus1X2, minus1Y2, minus2X1, minus2Y1 = hey.Vektor2Dminus(x1, y1, x2, y2)
        tegn22(x1, y1, x2, y2)

        x114label = tkinter.Label(vinduet)
        x114label.config(text=f"{minus1X2} , {minus1Y2}")
        x114label.place(x=450, y=130)
        minus1X2, minus1Y2, minus2X1, minus2Y1 = hey.Vektor2Dminus (x1,y1,x2,y2)

        x114label=tkinter.Label(vinduet)
        x114label.config(text=f"{minus1X2} , {minus1Y2}")
        x114label.place(x=300,y=150)    


        x212label=tkinter.Label(vinduet)
        x212label.config(text=f"{minus2X1}, {minus2Y1}")
        x212label.place(x=450,y=150)    


        x113label=tkinter.Label(vinduet)
        x113label.config(text="minusværdien af v1-v2 er")
        x113label.place(x=300,y=130)

        x222label=tkinter.Label(vinduet)
        x222label.config(text="minusværdien af v2-v1 er")
        x222label.place(x=300,y=150)







        

   
    
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

x115label=tkinter.Label(vinduet)
x115label.config(text="Minus")
x115label.place(x=300,y=8)


#__________________________________


x06inputfelt=tkinter.Entry(vinduet)
x06inputfelt.config(width=10)
x06inputfelt.place(x=850,y=700)

x07inputfelt=tkinter.Entry(vinduet)
x07inputfelt.config(width=10)
x07inputfelt.place(x=930,y=700)

x08inputfelt=tkinter.Entry(vinduet)
x08inputfelt.config(width=10)
x08inputfelt.place(x=1010,y=700)

x09inputfelt=tkinter.Entry(vinduet)
x09inputfelt.config(width=10)
x09inputfelt.place(x=1090,y=700)

x010inputfelt=tkinter.Entry(vinduet)
x010inputfelt.config(width=10)
x010inputfelt.place(x=1170,y=700)

x011inputfelt=tkinter.Entry(vinduet)
x011inputfelt.config(width=10)
x011inputfelt.place(x=1250,y=700)



def Beregnplus2Dg3D():

    x1 = float(x06inputfelt.get())
    y1 = float(x07inputfelt.get())

    x2 = float(x08inputfelt.get())
    y2 = float(x09inputfelt.get())



    if (x010inputfelt.get() != "" and x011inputfelt.get() != ""):
        #3D
        z1 = float(x010inputfelt.get())
        z2 = float(x011inputfelt.get())
        plusX,plusY,plusZ= hey.vektor3Dplus (x1,y1,x2,y2,z1,z2)


        

        x2label=tkinter.Label(vinduet)                    
        x2label.config(text = "Summen af vektorne er")
        x2label.place(x=850,y=730) 

        
        x23label=tkinter.Label(vinduet)                    
        x23label.config(text = f"{plusX} , {plusY} , {plusZ}")
        x23label.place(x=980,y=730) 




    if (x010inputfelt.get() == "" and x011inputfelt.get() == ""):
        #2D
        plusX,plusY= hey.vektor2Dplus (x1,y1,x2,y2)


        x2label=tkinter.Label(vinduet)                    
        x2label.config(text = "Summen af vektorne er")
        x2label.place(x=850,y=730) 

        x23label=tkinter.Label(vinduet)                    
        x23label.config(text = f"{plusX} , {plusY}")
        x23label.place(x=980,y=730) 



#knap
Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=Beregnplus2Dg3D)
Knap2.place(x=1000,y=750)  

#Labels
x2label=tkinter.Label(vinduet)                    
x2label.config(text = "x1")
x2label.place(x=870,y=670) 

x3label=tkinter.Label(vinduet)                    
x3label.config(text = "y1")
x3label.place(x=950,y=670) 

x4label=tkinter.Label(vinduet)                    
x4label.config(text = "x2")
x4label.place(x=1030,y=670)

x2label=tkinter.Label(vinduet)                    
x2label.config(text = "y2")
x2label.place(x=1110,y=670) 

x2label=tkinter.Label(vinduet)                    
x2label.config(text = "z1")
x2label.place(x=1190,y=670) 

x2label=tkinter.Label(vinduet)                    
x2label.config(text = "z2")
x2label.place(x=1270,y=670) 


x2label=tkinter.Label(vinduet)                    
x2label.config(text = "Plus")
x2label.place(x=850,y=650) 







    




#_____________________





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
    x1 = float(x300inputfelt.get())  
    y1 = float(x11inputfelt.get())
    x2 = float(x10inputfelt.get())
    y2 = float(x9inputfelt.get())

    
    længdeAfplus= hey.Vektor2DlægdeAFplus(x1,x2,y1,y2)   
    

    x10label=tkinter.Label(vinduet)                    
    x10label.config(text = længdeAfplus)
    x10label.place(x=490,y=295) 

    x115label=tkinter.Label(vinduet)
    x115label.config(text="Længden af to vektor pluss sammen:")
    x115label.place(x=280,y=295)

x116label=tkinter.Label(vinduet)
x116label.config(text="Længden af vektor plus sammen")
x116label.place(x=280,y=280)

x117label=tkinter.Label(vinduet)
x117label.config(text="x1")
x117label.place(x=300,y=180)

x118label=tkinter.Label(vinduet)
x118label.config(text="y1")
x118label.place(x=380,y=180)

x118label=tkinter.Label(vinduet)
x118label.config(text="x2")
x118label.place(x=460,y=180)

x119label=tkinter.Label(vinduet)
x119label.config(text="y2")
x119label.place(x=540,y=180)

   


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
x14inputfelt.place(x=1160,y=65)

x15inputfelt=tkinter.Entry(vinduet)
x15inputfelt.config(width=10)
x15inputfelt.place(x=1240,y=65)



def beregnSkallar2Dog3D():
    x1= float(x12inputfelt.get())                  
    y1= float(x13inputfelt.get())
    s = float(x15inputfelt.get())

    if(x14inputfelt.get()==""):
        skallarpruduktX, skallarpruduktY=hey.skallar2D(x1,y1,s)


        x22label=tkinter.Label(vinduet)                    
        x22label.config(text = f"{skallarpruduktX} , {skallarpruduktY}")
        x22label.place(x=1100,y=140) 

        x223abel=tkinter.Label(vinduet)                    
        x223abel.config(text = "Skallarprodukt er")
        x223abel.place(x=1000,y=140) 


    if(x14inputfelt.get()!=""):
        z1= float(x14inputfelt.get())

        skallarpruduktX,skallarpruduktY,skallarpruduktZ=hey.skallar3D(x1,y1,z1,s)

        x23label=tkinter.Label(vinduet)                    
        x23label.config(text = f"{skallarpruduktX} , {skallarpruduktY} , {skallarpruduktZ}")
        x23label.place(x=1100,y=140) 

        x223abel=tkinter.Label(vinduet)                    
        x223abel.config(text = "Skallarprodukt er")
        x223abel.place(x=1000,y=140) 

x22label=tkinter.Label(vinduet)                    
x22label.config(text = "s")
x22label.place(x=1260,y=40) 

x222abel=tkinter.Label(vinduet)                    
x222abel.config(text = "z1")
x222abel.place(x=1180,y=40) 

x223abel=tkinter.Label(vinduet)                    
x223abel.config(text = "y1")
x223abel.place(x=1100,y=40) 

x223abel=tkinter.Label(vinduet)                    
x223abel.config(text = "x1")
x223abel.place(x=1030,y=40) 


x224abel=tkinter.Label(vinduet)                    
x224abel.config(text = "Skallar")
x224abel.place(x=1000,y=10) 


    

#knap
Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=beregnSkallar2Dog3D)
Knap2.place(x=1100,y=100)  








x1111inputfelt=tkinter.Entry(vinduet)
x1111inputfelt.config(width=10)
x1111inputfelt.place(x=1000,y=400)

x2222inputfelt=tkinter.Entry(vinduet)
x2222inputfelt.config(width=10)
x2222inputfelt.place(x=1080,y=400)

x3333inputfelt=tkinter.Entry(vinduet)
x3333inputfelt.config(width=10)
x3333inputfelt.place(x=1160,y=400)

x4444inputfelt=tkinter.Entry(vinduet)
x4444inputfelt.config(width=10)
x4444inputfelt.place(x=1240,y=400)

x5555inputfelt=tkinter.Entry(vinduet)
x5555inputfelt.config(width=10)
x5555inputfelt.place(x=920,y=400)

x6666inputfelt=tkinter.Entry(vinduet)
x6666inputfelt.config(width=10)
x6666inputfelt.place(x=840,y=400)


def vektor3DOG2Dvinkel():
    x1=float(x6666inputfelt.get())
    y1=float(x5555inputfelt.get())
    x2=float(x1111inputfelt.get())
    y2=float(x2222inputfelt.get())                      
   

    if(x3333inputfelt.get()=="" and x4444inputfelt.get()==""):
        Vinkel=hey.Vektor2Dvinkel (x1,y1,x2,y2)

        x24label=tkinter.Label(vinduet)                    
        x24label.config(text = Vinkel)
        x24label.place(x=950,y=450) 

        x24label=tkinter.Label(vinduet)                    
        x24label.config(text = "Vektors vinkel")
        x24label.place(x=840,y=450) 
    
    if(x3333inputfelt.get()!="" and x4444inputfelt.get()!=""):
        z1=float(x3333inputfelt.get())
        z2=float(x4444inputfelt.get())

        Vinkel3D=hey.Vektor3Dvinkel (x1,y1,x2,y2,z1,z2)

        x24label=tkinter.Label(vinduet)                    
        x24label.config(text = Vinkel3D)
        x24label.place(x=950,y=450) 

        x24label=tkinter.Label(vinduet)                    
        x24label.config(text = "Vektors vinkel")
        x24label.place(x=840,y=450) 


Knap111=tkinter.Button(vinduet)
Knap111.config(width=12,text="Beregn",command=vektor3DOG2Dvinkel)
Knap111.place(x=1000,y=430)  

x24label=tkinter.Label(vinduet)                    
x24label.config(text = "x1")
x24label.place(x=850,y=370) 

x1212label=tkinter.Label(vinduet)                    
x1212label.config(text = "y1")
x1212label.place(x=940,y=370) 

x1212label=tkinter.Label(vinduet)                    
x1212label.config(text = "x2")
x1212label.place(x=1030,y=370) 

x1212label=tkinter.Label(vinduet)                    
x1212label.config(text = "y2")
x1212label.place(x=1100,y=370) 

x1212label=tkinter.Label(vinduet)                    
x1212label.config(text = "z1")
x1212label.place(x=1200,y=370) 

x1212label=tkinter.Label(vinduet)                    
x1212label.config(text = "z2")
x1212label.place(x=1270,y=370) 

x222label=tkinter.Label(vinduet)                    
x222label.config(text = "Find vinkel")
x222label.place(x=840,y=330) 





    

x16inputfelt=tkinter.Entry(vinduet)
x16inputfelt.config(width=10)
x16inputfelt.place(x=300,y=360)

x17inputfelt=tkinter.Entry(vinduet)
x17inputfelt.config(width=10)
x17inputfelt.place(x=380,y=360)

x18inputfelt=tkinter.Entry(vinduet)
x18inputfelt.config(width=10)
x18inputfelt.place(x=460,y=360)

x19inputfelt=tkinter.Entry(vinduet)
x19inputfelt.config(width=10)
x19inputfelt.place(x=540,y=360)

x0111inputfelt=tkinter.Entry(vinduet)
x0111inputfelt.config(width=10)
x0111inputfelt.place(x=620,y=360)

x0112inputfelt=tkinter.Entry(vinduet)
x0112inputfelt.config(width=10)
x0112inputfelt.place(x=700,y=360)



def krydsvektor3D():
    x1=float(x16inputfelt.get())            
    x2=float(x17inputfelt.get())
    y1=float(x18inputfelt.get())
    y2=float(x19inputfelt.get())
    z1=float(x0111inputfelt.get())
    z2=float(x0112inputfelt.get())

    Xverdien,Yverdien,Zverdien=hey.krydsvektor3D(x1,x2,y1,y2,z1,z2)

    x24label=tkinter.Label(vinduet)                    
    x24label.config(text = f"{Xverdien}, {Yverdien},{Zverdien}")
    x24label.place(x=400,y=430) 

    x25label=tkinter.Label(vinduet)                    
    x25label.config(text = "Krydsvetoren er")
    x25label.place(x=300,y=430)


Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=krydsvektor3D)
Knap2.place(x=400,y=400)  

x24label=tkinter.Label(vinduet)                    
x24label.config(text = "Krydsvektor")
x24label.place(x=250,y=310) 

x25label=tkinter.Label(vinduet)                    
x25label.config(text = "x1")
x25label.place(x=330,y=330) 

x25label=tkinter.Label(vinduet)                    
x25label.config(text = "x2")
x25label.place(x=400,y=330) 

x25label=tkinter.Label(vinduet)                    
x25label.config(text = "y1")
x25label.place(x=480,y=330) 

x25label=tkinter.Label(vinduet)                    
x25label.config(text = "y2")
x25label.place(x=560,y=330)

x25label=tkinter.Label(vinduet)                    
x25label.config(text = "z1")
x25label.place(x=640,y=330)

x25label=tkinter.Label(vinduet)                    
x25label.config(text = "z2")
x25label.place(x=720,y=330)



#_____________________________________




x20inputfelt=tkinter.Entry(vinduet)
x20inputfelt.config(width=10)
x20inputfelt.place(x=120,y=210)

x21inputfelt=tkinter.Entry(vinduet)
x21inputfelt.config(width=10)
x21inputfelt.place(x=40,y=210)

def polærTilKartasian():
    v = float(x21inputfelt.get())
    l = float(x20inputfelt.get())        

    x1,y1=hey.polærTilKartasian(v,l)
    tegn(x1,y1)

    x25label=tkinter.Label(vinduet)                    
    x25label.config(text = f"{x1}, {y1}")
    x25label.place(x=50,y=280) 

    x223abel=tkinter.Label(vinduet)                    
    x223abel.config(text = "polær til kartasian")
    x223abel.place(x=35,y=280) 

x224abel=tkinter.Label(vinduet)                    
x224abel.config(text = "vinkel")
x224abel.place(x=45,y=187)

x228abel=tkinter.Label(vinduet)                    
x228abel.config(text = "længde")
x228abel.place(x=120,y=187)

Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=polærTilKartasian)
Knap2.place(x=60,y=240)  

x24label=tkinter.Label(vinduet)                    
x24label.config(text = "Polær til kartasian")
x24label.place(x=8,y=170) 




#_____________________________________


x22inputfelt=tkinter.Entry(vinduet)
x22inputfelt.config(width=10)
x22inputfelt.place(x=120,y=360)

x23inputfelt=tkinter.Entry(vinduet)
x23inputfelt.config(width=10)
x23inputfelt.place(x=40,y=360)



def KartasianTilPolær():
    x1 = float(x23inputfelt.get())
    y1 = float(x22inputfelt.get())

    v,l=hey.KartasianTilPolær(x1,y1)     

    x26label=tkinter.Label(vinduet)                    
    x26label.config(text = f"{v}  , {l}")
    x26label.place(x=155,y=420) 

    x227label=tkinter.Label(vinduet)                    
    x227label.config(text = "Kartasian til polær er")
    x227label.place(x=40,y=420)


x225label=tkinter.Label(vinduet)                    
x225label.config(text = "x1")
x225label.place(x=45,y=330)

x226label=tkinter.Label(vinduet)                    
x226label.config(text = "y1")
x226label.place(x=120,y=330)

x24label=tkinter.Label(vinduet)                    
x24label.config(text = "Kartasian til polær")
x24label.place(x=8,y=300) 

    


Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=KartasianTilPolær)     
Knap2.place(x=60,y=400) 




#__________________________________________


x24inputfelt=tkinter.Entry(vinduet)
x24inputfelt.config(width=10)
x24inputfelt.place(x=460,y=500)

x25inputfelt=tkinter.Entry(vinduet)
x25inputfelt.config(width=10)
x25inputfelt.place(x=380,y=500)

x89inputfelt=tkinter.Entry(vinduet)
x89inputfelt.config(width=10)
x89inputfelt.place(x=300,y=500)



def enhedsvektor2Dog3D ():
    x1=float(x89inputfelt.get())                                      
    y1=float(x25inputfelt.get())


    if(x24inputfelt.get()==""):

        lændgde = hey.enhedsvektor2D(x1,y1)
        x,y = hey.enhedsvektor2D(x1,y1)
        tegn(x1,y1)

        x27label=tkinter.Label(vinduet)                    
        x27label.config(text = f"{x} , {y}")
        x27label.place(x=500,y=560) 
    

        x22label=tkinter.Label(vinduet)                    
        x22label.config(text = "Koordinater til enhedsvektor 2D er")
        x22label.place(x=300,y=560) 



    if(x24inputfelt.get()!=""):
        z1=float(x24inputfelt.get())

        længde = hey.enhedsvektor3D (x1,y1,z1)
        x,y,z= hey.enhedsvektor3D(x1,y1,z1)    
             


        x28label=tkinter.Label(vinduet)                    
        x28label.config(text = f"{x} , {y} , {z}")
        x28label.place(x=495,y=560) 

        x22label=tkinter.Label(vinduet)                    
        x22label.config(text = "Koordinater til enhedsvektor 3D er")
        x22label.place(x=300,y=560) 


x27label=tkinter.Label(vinduet)                    
x27label.config(text = "x1")
x27label.place(x=330,y=470) 

x27label=tkinter.Label(vinduet)                    
x27label.config(text = "y1")
x27label.place(x=390,y=470) 

x27label=tkinter.Label(vinduet)                    
x27label.config(text = "z1")
x27label.place(x=470,y=470) 

Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=enhedsvektor2Dog3D)   
Knap2.place(x=370,y=530) 

x24label=tkinter.Label(vinduet)                    
x24label.config(text = "Enhedsvektor")
x24label.place(x=230,y=440) 








#______________________________________________


x0inputfelt=tkinter.Entry(vinduet)
x0inputfelt.config(width=10)
x0inputfelt.place(x=850,y=570)

x01inputfelt=tkinter.Entry(vinduet)
x01inputfelt.config(width=10)
x01inputfelt.place(x=930,y=570)

x02inputfelt=tkinter.Entry(vinduet)
x02inputfelt.config(width=10)
x02inputfelt.place(x=1010,y=570)

x03inputfelt=tkinter.Entry(vinduet)
x03inputfelt.config(width=10)
x03inputfelt.place(x=1090,y=570)

x04inputfelt=tkinter.Entry(vinduet)
x04inputfelt.config(width=10)
x04inputfelt.place(x=1170,y=570)

x05inputfelt=tkinter.Entry(vinduet)
x05inputfelt.config(width=10)
x05inputfelt.place(x=1250,y=570)


def projektionAOgB():             
    x1=float(x0inputfelt.get())
    y1=float(x01inputfelt.get())
    x2=float(x01inputfelt.get())
    y2=float(x03inputfelt.get())                     
    z1=float(x04inputfelt.get())
    z2=float(x05inputfelt.get())

    
    ProjektionA= hey.projektionA (x1,y1,z1,x2,y2,z2)
    tegn3D(x1,y1,z1,x2,y2,z2)

    ProjektionB=hey.projektionB (x1,y1,z1,x2,y2,z2)
    tegn3D(x1,y1,z1,x2,y2,z2)


    
    x28label=tkinter.Label(vinduet)                    
    x28label.config(text = f"{ProjektionA} , {ProjektionB} ")
    x28label.place(x=960,y=630) 

    x22label=tkinter.Label(vinduet)                    
    x22label.config(text = "projektion A og B er")
    x22label.place(x=850,y=630) 






Knap20=tkinter.Button(vinduet)
Knap20.config(width=12,text="Beregn",command=projektionAOgB)   
Knap20.place(x=1000,y=610) 

x22label=tkinter.Label(vinduet)                    
x22label.config(text = "x1")
x22label.place(x=880,y=550) 

x22label=tkinter.Label(vinduet)                    
x22label.config(text = "y1")
x22label.place(x=950,y=550) 

x22label=tkinter.Label(vinduet)                    
x22label.config(text = "x2")
x22label.place(x=1030,y=550) 

x22label=tkinter.Label(vinduet)                    
x22label.config(text = "y2")
x22label.place(x=1100,y=550) 

x22label=tkinter.Label(vinduet)                    
x22label.config(text = "z1")
x22label.place(x=1200,y=550) 

x22label=tkinter.Label(vinduet)                    
x22label.config(text = "z2")
x22label.place(x=1280,y=550) 

x22label=tkinter.Label(vinduet)                    
x22label.config(text = "projektion")
x22label.place(x=830,y=500) 




#_____________________________________




x400inputfelt=tkinter.Entry(vinduet)
x400inputfelt.config(width=10)
x400inputfelt.place(x=40,y=650)

x401inputfelt=tkinter.Entry(vinduet)
x401inputfelt.config(width=10)
x401inputfelt.place(x=120,y=650)


def tværvektor2d ():
    x1 = float(x400inputfelt.get())          
    y1 = float(x401inputfelt.get())

    tvær= hey.tværvektor2d(x1,y1)
    tegn(x1,y1)

    x29label=tkinter.Label(vinduet)                    
    x29label.config(text = "koordinater til tværvektor er")
    x29label.place(x=40,y=730)

    
    x28label=tkinter.Label(vinduet)                    
    x28label.config(text = f"{tvær}")
    x28label.place(x=195,y=730) 


x29label=tkinter.Label(vinduet)                    
x29label.config(text = "x1")
x29label.place(x=40,y=620)

x29label=tkinter.Label(vinduet)                    
x29label.config(text = "y1")
x29label.place(x=120,y=620)

Knap5=tkinter.Button(vinduet)
Knap5.config(width=12,text="Beregn",command=tværvektor2d)   
Knap5.place(x=60,y=680)

x29label=tkinter.Label(vinduet)                    
x29label.config(text = "tværvektor")
x29label.place(x=40,y=580)






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
    x1 = float(x27inputfelt.get())   
    y1 = float(x28inputfelt.get())                   
    x2 = float(x29inputfelt.get())
    y2 = float(x30inputfelt.get())

    vektorx,vektory = hey.punktvektor (x1,y1,x2,y2)


    x30label=tkinter.Label(vinduet)                    
    x30label.config(text =f"{vektorx} , {vektory}" )
    x30label.place(x=490,y=730)

    
    x31label=tkinter.Label(vinduet)                    
    x31label.config(text ="vektoren mellem de 4 punkter er" )
    x31label.place(x=300,y=730)

x31label=tkinter.Label(vinduet)                    
x31label.config(text ="x1" )
x31label.place(x=330,y=620)

x32label=tkinter.Label(vinduet)                    
x32label.config(text ="y1" )
x32label.place(x=400,y=620)

x33label=tkinter.Label(vinduet)                    
x33label.config(text ="x2" )
x33label.place(x=490,y=620)

x33label=tkinter.Label(vinduet)                    
x33label.config(text ="y2" )
x33label.place(x=570,y=620)


x311label=tkinter.Label(vinduet)                    
x311label.config(text ="Punktvektor" )
x311label.place(x=260,y=600)






Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=Beregnpunktvektor)     
Knap2.place(x=420,y=700) 



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
    x1=float(x31inputfelt.get())       
    y1=float(x32inputfelt.get())
    x2= float(x34inputfelt.get())
    y2=float(x35inputfelt.get())
    z1=float(x33inputfelt.get())
    z2=float(x36inputfelt.get())



    Dot,LængdeV1,LængdeV2,Theta = hey.Prikprodukt(x1,y1,x2,y2,z1,z2)
    tegn3D(x1,y1,x2,y2,z1,z2)

    
    x30label=tkinter.Label(vinduet)                    
    x30label.config(text =f"{Dot} , {LængdeV1} , {LængdeV2} , {Theta}" )
    x30label.place(x=1100,y=300)

       
    x31label=tkinter.Label(vinduet)                    
    x31label.config(text = "Dotprodukt, LængdeV1 , LængdeV2 , Theta:" )
    x31label.place(x=860,y=300)



x31label=tkinter.Label(vinduet)                    
x31label.config(text = "x1" )
x31label.place(x=880,y=180)

x32label=tkinter.Label(vinduet)                    
x32label.config(text = "y1" )
x32label.place(x=960,y=180)

x32label=tkinter.Label(vinduet)                    
x32label.config(text = "z1" )
x32label.place(x=1040,y=180)

x32label=tkinter.Label(vinduet)                    
x32label.config(text = "x2" )
x32label.place(x=1120,y=180)

x32label=tkinter.Label(vinduet)                    
x32label.config(text = "y2" )
x32label.place(x=1200,y=180)

x32label=tkinter.Label(vinduet)                    
x32label.config(text = "z2" )
x32label.place(x=1280,y=180)

x31label=tkinter.Label(vinduet)                    
x31label.config(text = "Prikproudkt" )
x31label.place(x=820,y=150)


Knap2=tkinter.Button(vinduet)
Knap2.config(width=12,text="Beregn",command=BergenPrikprodukt)     
Knap2.place(x=1000,y=260) 






















    
    








         









    




















































vinduet.mainloop()
