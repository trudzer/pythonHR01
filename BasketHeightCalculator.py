import math

def calcReach(height, ws):
    return math.floor(height + (ws / 2) - (0.2 * ws))

def calcHeight(height, ws, basket, HEIGHT, WS):
    differenceInReach = calcReach(height, ws) - calcReach(HEIGHT, WS)
    equivalent_basket_height = basket - differenceInReach
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
    HEIGHT = 190
    WS = 194
    BASKET = 305

    otherHeight = int(input("Enter the height of the person (in cm): "))
    otherWS = int(input("Enter the wingspan of the person (in cm): "))
    REACH = calcReach(HEIGHT, WS)
    otherReach = calcReach(otherHeight, otherWS)
    equivalentHeight = calcHeight(otherHeight, otherWS, BASKET, HEIGHT, WS)

    print(f"\nThe person with height {HEIGHT}cm ({calcCMtoInch(HEIGHT)}), wingspan {WS}cm ({calcCMtoInch(WS)}) and standing reach {REACH}cm ({calcCMtoInch(REACH)})")
    print(f"The person with height {otherHeight}cm ({calcCMtoInch(otherHeight)}), wingspan {otherWS}cm ({calcCMtoInch(otherWS)}) and standing reach {otherReach}cm ({calcCMtoInch(otherReach)})")
    print(f"A basket height of {equivalentHeight}cm ({calcCMtoInch(equivalentHeight)}) is equivalent to a basket height of {BASKET}cm ({calcCMtoInch(BASKET)})")

if __name__ == "__main__":
    main()
