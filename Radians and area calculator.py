import math
import tkinter as tk

class functions:
    def __init__(self):
        pass
    def Num_squared(self,num):
        num = num*num
        return num
    def Radians(self): #calculates area of a sector of a circle as well as coterminals
        pie = math.pi
        py = pie*2
        rIn = input('enter radians: ')
        thetaIn = input('enter theta: ')
        theta = int(thetaIn)
        r = int(rIn)
        centralAngle = theta/360
        squared = r*r
        pye = py*r
        final = pye*centralAngle
        area = pie*squared
        actualArea = centralAngle*area
        print(final)
        print(final/pie)
        print('area : ')
        print(actualArea)
        print('area in terms of pi :')
        print(actualArea/pie)
    def Quadrant(self): #takes radians like pi/6 and returns degrees and coterminals
        In = input('enter numerator : ')
        under = input('enter denomenator : ')
        p = math.pi
        pIn = float(In)*p
        rUnder = float(under)
        fraction = pIn/rUnder
        divPi = fraction/p
        final = divPi*180
        print(final)
        print(final + 360)
        print (final - 360)
    def Terms_of_rads(self): #degrees to radians calculator, but not quite terms of rads
        inp = input('Enter degrees : ')
        angle = float(inp)
        rads = math.radians(angle)
        pi = math.pi
        ArrayList = [pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 7*pi/6, 5*pi/4, 4*pi/3, 3*pi/2]
        l_ist = ["pi/6", "pi/4", "pi/3", "pi/2", "2pi/3", "3pi/4", "5pi/6", "pi", "7pi/6", "5pi/4", "3pi/2"]
        its = 0
        for x in ArrayList:
            if(rads == x):
                print(l_ist[its])
            its+=1
    def Pythagorean(self): #Pythagorean theorom, what else do you need?
        input1 = input()
        input2 = input()
        ad = float(input1)
        a = ad*ad
        hy = float(input2)
        h = hy*hy
        l = h + a
        print(math.sqrt(l))
        print(l)
    def sinCos(self): #returns either sin or cos based on trig identities
        sin = input('enter sin : ')
        sIn = float(sin)
        Sin = sIn*sIn
        cos = 1-Sin
        print(math.sqrt(cos))
    def Law_of_cos(self): #does the third side in a non-right triangle
        a = input('enter a : ')
        b = input('enter b : ')
        c = input('enter theta : ')
        cNum = float(c)
        bNum = float(b)
        aNum = float(a)
        pi = math.pi
        piOver = pi/180
        cForReal = cNum*piOver
        print(cForReal)
        bSq = bNum*bNum
        aSq = aNum*aNum
        ab = aNum*bNum
        abab = 2*ab
        cos = math.cos(cForReal)
        abCos = abab*cos
        AB = aSq + bSq
        cSq = AB - abCos
        print(cSq)
        print(math.sqrt(cSq))
    def Law_of_arcCos(self): #does the angle if you know all sides
        a = input('enter A :')
        b = input('enter B :')
        c = input('enter C :')
        fA = float(a)
        fB = float(b)
        fC = float(c)
        aSq = fA*fA
        bSq = fB*fB
        cSq = fC*fC
        pi= math.pi
        pie = 180/pi
        ab = fA*fB
        abab = ab*2
        aSqbSq = aSq + bSq
        cec = aSqbSq - cSq
        abCec = cec/abab
        z = math.acos(abCec)
        print(z*pie)
        print(math.acos(math.radians(z)))
        print(z)
    def Law_of_sin(self): #does the side b if sin of b sin of a are all known
        a = input('enter side a : ')
        angle = input('enter angle A : ')
        angleB = input('enter angle B : ')
        fa = float(a)
        fA = float(angle)
        fB = float(angleB)
        sinA = math.sin(math.radians(fA))
        sinB = math.sin(math.radians(fB))
        totalA = fa/sinA
        x = totalA*sinB
        print(x)
    def Law_of_arcSin(self): #Returns other angle idk Ich bin hevaiing una stroek
        a = input('enter side a : ')
        sideB = input('enter side b : ')
        angleA = input('enter angle A : ')
        fa = float(a)
        fb = float(sideB)
        fA = float(angleA)
        sinA = math.sin(math.radians(fA))
        totalA = sinA/fa
        x = totalA*fb
        y = math.asin(x)
        print(math.asin(x))
        print(math.degrees(y))
    def Area_with_sin(self): # Returns area of non right triangle
        a = input('enter a : ')
        b = input('enter b : ')
        c = input('enter angle : ')
        A = float(a)
        B = float(b)
        C = float(c)
        sinC = math.sin(math.radians(C))
        halfA = A/2
        timesSin = B*sinC
        x = halfA*timesSin
        print(x) # Answer we use for points
        print(math.degrees(x)) # Actual answer

def main():
    def thing():
        btn1.configure(command=getattr(calc,clicked.get()))
    calc = functions()
    root = tk.Tk()
    root.attributes("-topmost",True)
    root.title("Calc (short for calculator for any new viewers)")
    options = [
        "Law_of_cos",
        "Law_of_sin",
        "Law_of_arcCos",
        "Law_of_arcSin",
        "Area_with_sin",
        "Pythagorean",
        "Terms_of_rads",
        "Quadrant",
        "Radians",
        "Num_squared"
    ]
    clicked = tk.StringVar(root)
    clicked.set(options[1])
    lbl1 = tk.OptionMenu(root,clicked,*options)
    lbl1.pack()
    btn1 = tk.Button(root,text="Confirm",command=thing)
    btn1.pack()
    while True:
        thing()
        root.update()


main()