import math

def calcReach(height, ws):
    return math.floor(height + (ws / 2) - (0.2 * ws))

def calcHeight(height, ws, basket, HEIGHT, WS):
    differenceInReach = calcReach(height, ws) - calcReach(HEIGHT, WS)
    equivalentBasketHeight = basket - differenceInReach
    return math.floor(equivalentBasketHeight)

def calcCMtoInch(heightCM):
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

    print(f"\n(A) Height: {HEIGHT}cm ({calcCMtoInch(HEIGHT)}), wingspan: {WS}cm ({calcCMtoInch(WS)}) and standing reach: {REACH}cm ({calcCMtoInch(REACH)})")
    print(f"(B) Height: {otherHeight}cm ({calcCMtoInch(otherHeight)}), wingspan: {otherWS}cm ({calcCMtoInch(otherWS)}) and standing reach: {otherReach}cm ({calcCMtoInch(otherReach)})")
    print(f"A basket height of {equivalentHeight}cm ({calcCMtoInch(equivalentHeight)}) for person (A) is equivalent to a basket height of {BASKET}cm ({calcCMtoInch(BASKET)}) for person (B)")

if __name__ == "__main__":
    main()
