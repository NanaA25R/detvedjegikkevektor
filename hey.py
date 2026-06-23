import math

def Vektor2DLængde(x1,y1):
    x1 = float(x1)
    y1 = float(y1)

    længde = math.sqrt((x1**2) + (y1**2))
    
    print('længden af vektor1=')
    print(længde)
    return(længde)

def  Vektor2Dminus(x1,y1,x2,y2):
    minus1X2 = float (x1-x2)
    minus1Y2 = float (y1-y2)

    minus2X1 = float (x2-x1)
    minus2Y1 = float (y2-y1)

    print('minusverdien af v1-v2 er')
    print('x=')
    print(minus1X2)
    

    print('Y=')
    print(minus1Y2)

    print("minusværdien af v2-v1 er")
    print('x=')
    print(minus2X1)

    print('Y=')
    print(minus2Y1)
    return(minus2Y1,minus1X2,minus1Y2,minus2X1)



def Vektor3Dminus(x1,y1,x2,y2,z1,z2):
    minus1X2 = (x1-x2)
    minus1Y2 = (y1-y2)
    minus1Z2 = (z1-z2)

    minus2X1 = (x2-x1)
    minus2Y1 = (y2-y1)
    minus2Z1 = (z2-z1)

    print('minusverdien af v1-v2 er')
    print('x=')
    print(minus1X2)
    print('Y=')
    print(minus1Y2)
    print('Z=')
    print(minus1Z2)


    print("minusværdien af v2-v1 er")
    print('x=')
    print(minus2X1)
    print('Y=')
    print(minus2Y1)
    print('Z=')
    print(minus2Z1)
    return(minus1X2,minus1Y2,minus1Z2,minus2X1,minus2Y1,minus2Z1)

def vektor2Dplus(x1,y1,x2,y2):
    plusX = (x1+x2)
    plusY = (y1+y2)
    print('x=')
    print(plusX)
    print('Y=')
    print(plusY)
    return(plusX,plusY)

def vektor3Dplus(x1,y1,x2,y2,z1,z2):
    plusX = (x1+x2)
    plusY = (y1+y2)
    plusZ = (z1+z2)
    print('x=')
    print(plusX)
    print('Y=')
    print(plusY)
    print('Z=')
    print(plusZ)
    return(plusX,plusY,plusZ)

def Vektor2DlægdeAFplus(x1,x2,y1,y2):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    plusX = (x1+x2)
    plusY = (y1+y2)
  
    længdeAfplus = math.sqrt(plusY**2+plusX**2)
    print(længdeAfplus)
    return(længdeAfplus)

def skallar2D (x1,y1,s):
    skallarpruduktX = (x1*s) 
    skallarpruduktY = (y1*s) 
    return(skallarpruduktX,skallarpruduktY)
   
    

def skallar3D (x1,y1,z1,s):
    skallarpruduktX = (x1*s) 
    skallarpruduktY = (y1*s) 
    skallarpruduktZ = (z1*s) 
    return(skallarpruduktX,skallarpruduktY,skallarpruduktZ)


def Vektor2Dvinkel(x1,x2,y1,y2):
    Vinkel = math.acos((x1*x2+y1*y2)/(math.sqrt((x1**2) + (y1**2))*(math.sqrt((x2**2) + (y2**2)))))
    return(math.degrees(Vinkel))
    
def Vektor3Dvinkel(x1,x2,y1,y2,z1,z2):
    Vinkel3D = math.acos((x1*x2+y1*y2+z1*z2)/(math.sqrt((x1**2) + (y1**2) + (z1**2))*(math.sqrt((x2**2) + (y2**2) + (z2**2)))))
    print(math.degrees(Vinkel3D))
    return(math.degrees(Vinkel3D))

def krydsvektor3D (x1,x2,y1,y2,z1,z2):
    Xverdien = (y1*z2-z1*y2)
    Yverdien = (z1*x2-x1*z2)
    Zverdien = (x1*y2-y1*x2)
    return(Xverdien,Yverdien,Zverdien)

def polærTilKartasian (v,l):
    y1 = l*math.sin(v)
    x1 = l*math.cos(v)
    return(x1,y1)
 
def KartasianTilPolær (x1,y1):
    l = math.sqrt((x1**2) + (y1**2))
    v = math.atan(x1/y1)
    return(v,l)


def enhedsvektor2D (x1,y1):
    lændgde = math.sqrt((x1**2) + (y1**2))
    x = x1/ lændgde
    y= y1 /lændgde
    return(x,y)

def enhedsvektor3D (x1,y1,z1):
    lændgde = math.sqrt((x1**2) + (y1**2) + (z1**2))
    x = x1/ lændgde
    y = y1 /lændgde
    z = z1/lændgde
    return(x,y,z)

def projektionA(x1,y1,z1,x2,y2,z2):

    if z1 == None:
         z1 = 0
    if z2 == None:
         z2 = 0
    Dot = (x1*x2+y1*y2+z1*z2)
    A = math.sqrt(x1**2+y1**2+z1**2)
    ProjektionA= Dot/A
    return(ProjektionA)

def projektionB(x1,y1,z1,x2,y2,z2):
    if z1 == None:
         z1 = 0
    if z2 == None:
         z2 = 0
    Dot = (x1*x2+y1*y2+z1*z2)
    B = math.sqrt(x2**2+y2**2+z2**2)
    ProjektionB= Dot/B
    return(ProjektionB)

def tværvektor2d(x1,y1):
    if x1 == 0:
        return None
    tvær = -y1/x1
    return(tvær)

def punktvektor(x1,y1,x2,y2):
    vektorx = (x2-x1)
    vektory = (y2-y1)    
    return(vektorx,vektory)

def Prikprodukt(x1,y1,x2,y2,z1,z2):
    if z1 == None:
         z1 = 0
    if z2 == None:
         z2 = 0
    Dot = (x1 * x2 + y1 * y2 + z1 * z2)
    LængdeV1 = math.sqrt(x1**2+y1**2+z1**2)
    LængdeV2 = math.sqrt(x2**2+y2**2+z2**2)
    Theta = math.acos((Dot)/(LængdeV1*LængdeV2))
    return(Dot,LængdeV1,LængdeV2,Theta)


##############DONE####################