import math

def numSquared(num):
    num = num*num
    return num

def Radians(): #calculates area of a sector of a circle as well as coterminals
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
#Radians()


def quadrantCalc(): #takes radians like pi/6 and returns degrees and coterminals
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
#quadrantCalc()

def termsOfRad(): #degrees to radians calculator, but not quite terms of rads
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
#termsOfRad()

def pythagoreanTheorem(): #Pythagorean theorom, what else do you need?
    input1 = input()
    input2 = input()
    ad = float(input1)
    a = ad*ad
    hy = float(input2)
    h = hy*hy
    l = h + a
    print(math.sqrt(l))
    print(l)
#pythagoreanTheorem()

def sinCos(): #returns either sin or cos based on trig identities
    sin = input('enter sin : ')
    sIn = float(sin)
    Sin = sIn*sIn
    cos = 1-Sin
    print(math.sqrt(cos))
#sinCos()


def lawOfCos(): #does the third side in a non-right triangle
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
#lawOfCos()

def lawOfarcCos(): #does the angle if you know all sides
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
    print(math.degrees(z))
#lawOfarcCos()


def lawOfSin(): #does the side b if sin of b sin of a are all known
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
lawOfSin()

# sin90/5 = sinB/8
def lawOfArcSin(): #Returns other angle idk Ich bin hevaiing una stroek
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
#lawOfArcSin()


def areaWithSin(): # Returns area of non right triangle
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
#areaWithSin()

