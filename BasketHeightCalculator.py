import math

def calcReach(height, ws):
    return math.floor(height + (ws / 2) - (0.2 * ws))
    
def calcJump(standingReach, basketHeight):
    return (basketHeight - standingReach) + 15
    
def calcHeight(height, ws, basket, HEIGHT, WS):
    differenceInReach = calcReach(height, ws) - calcReach(HEIGHT, WS)
    equivalentBasketHeight = basket - differenceInReach
    return math.floor(equivalentBasketHeight)
    
def calcCMtoInch(heightCM):
    inches = round(heightCM / 2.54)
    newHeight = "{}\"".format(inches)
    return newHeight

def calcCMtoFeet(heightCM):
    feet = math.floor(heightCM / 30.48)
    inches = round((heightCM % 30.48) / 2.54)
    if inches == 12:
        feet += 1
        inches = 0
    newHeight = "{}'{}\"".format(feet, inches)
    return newHeight
    
def calcInchtoCM(heightInch):
    feet, inches = map(int, heightInch.split("'"))
    totalCM = feet * 30.48 + inches * 2.54
    return totalCM

def main():
    HEIGHT = 190
    WS = 194
    BASKET = 305
    REACH = calcReach(HEIGHT, WS)

    otherHeight = input("Enter the height of the person in (cm) or (ft): ")
    otherWS = input("Enter the wingspan of the person in (cm) or (ft): ")
    
    if "'" in otherHeight:
        otherHeight = int(calcInchtoCM(otherHeight))
    else:
        otherHeight = int(otherHeight)
    if "'" in otherWS:
        otherWS = int(calcInchtoCM(otherWS))
    else:
        otherWS = int(otherWS)
        
    otherReach = calcReach(otherHeight, otherWS)
    equivalentHeight = calcHeight(otherHeight, otherWS, BASKET, HEIGHT, WS)

    print(f"\n(A) Height: {HEIGHT}cm ({calcCMtoFeet(HEIGHT)}), wingspan: {WS}cm ({calcCMtoFeet(WS)}) and standing reach: {REACH}cm ({calcCMtoFeet(REACH)})")
    print(f"(B) Height: {otherHeight}cm ({calcCMtoFeet(otherHeight)}), wingspan: {otherWS}cm ({calcCMtoFeet(otherWS)}) and standing reach: {otherReach}cm ({calcCMtoFeet(otherReach)})")
    print(f"A basket height of {equivalentHeight}cm ({calcCMtoFeet(equivalentHeight)}) for person (A) is equivalent to a basket height of {BASKET}cm ({calcCMtoFeet(BASKET)}) for person (B)")
    print(f"\nFor person (A) it will require {calcJump(REACH, BASKET)}cm ({calcCMtoInch(calcJump(REACH, BASKET))})")
    print(f"For person (B) it will require {calcJump(otherReach, BASKET)}cm ({calcCMtoInch(calcJump(otherReach, BASKET))})")

if __name__ == "__main__":
    main()
