#import ui.p
import math
def Vektor2DLængde(x1,y1,x2,y2):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    længde = math.sqrt((x1**2) + (y1**2))
    længde2 = math.sqrt(x2**2 + y2**2)
    print('længden af vektor1=')
    print(længde)
    print('længden af vektor2=')
    print(længde2)