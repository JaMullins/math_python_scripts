import math

def geoSequence():
    num = float(input("enter first term : ")) #just the first term of equation
    ratio = float(input("enter common ratio : ")) #percent of the previous term, I.E., if its .5 it halves each time
    sumNum = float(input("enter sumNum : ")) #Amount of terms you want to be added together, hence "sumNum"
    denominator = 1 - ratio
    numerator = 1 - pow(ratio, sumNum)
    frac = numerator/denominator
    print(num*frac)
#geoSequence()

def findZero():
    start = float(input("enter first term : "))
    ratio = float(input("enter common ratio : "))
    num = 0
    multiplier = pow(ratio, num)
    done = False
    
    while done == False:
        if (start * multiplier) == 0:
            print(num)
            done = True
            break
        else:
            num = num + 1
            multiplier = pow(ratio, num)
findZero()
