import math

HEIGHT = 190
WS = 194
BASKET = 305

def calcReach(height, ws):
    return math.floor(height + (0.07 * height) + (0.24 * ws))

REACH = calcReach(HEIGHT, WS)
    
def calcHeight(height, ws):
    differenceInReach = calcReach(height, ws) - REACH
    equivalent_basket_height = BASKET - differenceInReach
    return math.floor(equivalent_basket_height)

def calcCMtoInch(height_cm):
    feet = math.floor(height_cm / 30.48)
    inches = round((height_cm % 30.48) / 2.54)
    if inches == 12:
        feet += 1
        inches = 0
    newHeight = "{}'{}\"".format(feet, inches)
    return newHeight

def main():
    otherHeight = int(input("Enter the height of the person (in cm): "))
    otherWS = int(input("Enter the wingspan of the person (in cm): "))
    otherReach = calcReach(otherHeight, otherWS)
    equivalentHeight = calcHeight(otherHeight, otherWS)
    print(f"\nThe person with height {HEIGHT}cm ({calcCMtoInch(HEIGHT)}), wingspan {WS}cm ({calcCMtoInch(WS)}) and standing reach {REACH}cm ({calcCMtoInch(REACH)})\nThe person with height {otherHeight}cm ({calcCMtoInch(otherHeight)}), wingspan {otherWS}cm ({calcCMtoInch(otherWS)}) and standing reach {otherReach}cm ({calcCMtoInch(otherReach)}) \n\nA basket height of {equivalentHeight}cm ({calcCMtoInch(equivalentHeight)}) is equivelant to a basket height of {BASKET}cm ({calcCMtoInch(BASKET)})")

if __name__ == "__main__":
    main()
