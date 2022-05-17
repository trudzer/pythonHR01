import random
import os

FORMATIONS = ["3-5-2", "4-4-2", "4-2-3-1", "4-3-3", "4-4-1-1", "4-1-2-1-2", "4-1-2-1-2", "5-2-1-2", "5-2-3", "3-4-3", "4-1-4-1", "4-2-2-2", "4-1-2-2-1", "5-2-2-1", "3-2-2-2-1", "3-2-1-3",  "3-2-3-2", "5-3-1-1", "3-2-3-2", "4-3-3", "4-3-3"]

def TheGK(GK, NUMBERS):
    randGK = random.randint(0, len(GK) - 1)
    randNum = random.randint(0, len(NUMBERS) - 1)

    print("\n{:<30}{}".format("", "GK"))
    print("{:<30}{}".format("", GK[randGK]))
    print("{:<30}({})".format("", NUMBERS[randNum]))

    GK1 = GK[randGK]
    NUM1 = NUMBERS[randNum]

    for i in range(len(GK) - 1):
        if (GK[i] == GK1):
            GK.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

def FourInTheBack(LB, CB, RB, NUMBERS):
    randLB = random.randint(0, len(LB) - 1)
    randCB = random.randint(0, len(CB) - 1)
    randCB2 = random.randint(0, len(CB) - 1)
    randRB = random.randint(0, len(RB) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)
    randNum3 = random.randint(0, len(NUMBERS) - 1)
    randNum4 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    while (randNum3 == randNum1 or randNum3 == randNum2):
        randNum3 = random.randint(0, len(NUMBERS) - 1)
        if (randNum3 != randNum1 and randNum3 != randNum2):
            break

    while (randNum4 == randNum1 or randNum4 == randNum2 or randNum4 == randNum3):
        randNum4 = random.randint(0, len(NUMBERS) - 1)
        if (randNum4 != randNum1 and randNum4 != randNum2 and randNum4 != randNum3):
            break


    print("\n{:<20}{:<20}{:<20}{}".format("LB", "CB", "CB", "RB"))
    print("{:<20}".format(LB[randLB]), end="")
    print("{:<20}".format(CB[randCB]),end="")
    while (randCB2 == randCB):
        randCB2 = random.randint(0, len(CB) - 1)
        if (randCB2 != randCB):
            break
    print("{:<20}".format(CB[randCB2]), end="")
    print(RB[randRB])
    print("{:<20}{:<20}{:<20}{}".format("(" + str(NUMBERS[randNum1]) + ")", "(" + str(NUMBERS[randNum2]) + ")", "(" + str(NUMBERS[randNum3]) + ")", "(" + str(NUMBERS[randNum4]) + ")"))

    CB1 = CB[randCB]
    CB2 = CB[randCB2]
    LB1 = LB[randLB]
    RB1 = RB[randRB]

    NUM1 = NUMBERS[randNum1]
    NUM2 = NUMBERS[randNum2]
    NUM3 = NUMBERS[randNum3]
    NUM4 = NUMBERS[randNum4]

    for i in range(len(CB) - 1):
        if (CB[i] == CB1):
            CB.pop(i)

    for i in range(len(CB) - 1):
        if (CB[i] == CB2):
            CB.pop(i)

    for i in range(len(LB) - 1):
        if (LB[i] == LB1):
            LB.pop(i)

    for i in range(len(RB) - 1):
        if (RB[i] == RB1):
            RB.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM2):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM3):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM4):
            NUMBERS.pop(i)


def ThreeInTheBack(CB, NUMBERS):
    randCB = random.randint(0, len(CB) - 1)
    randCB2 = random.randint(0, len(CB) - 1)
    randCB3 = random.randint(0, len(CB) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)
    randNum3 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    while (randNum3 == randNum1 or randNum3 == randNum2):
        randNum3 = random.randint(0, len(NUMBERS) - 1)
        if (randNum3 != randNum1 and randNum3 != randNum2):
            break

    print("\n{:<10}{:<20}{:<20}{}".format("","CB","CB","CB"))
    print("{:<10}{:<20}".format("", CB[randCB]), end="")
    while (randCB2 == randCB  or randCB2 == randCB3):
        randCB2 = random.randint(0, len(CB) - 1)
        if (randCB2 != randCB and randCB2 != randCB3):
            break
    print("{:<20}".format(CB[randCB2]), end="")
    while (randCB3 == randCB  or randCB3 == randCB2):
        randCB3 = random.randint(0, len(CB) - 1)
        if (randCB3 != randCB and randCB3 != randCB2):
            break
    print(CB[randCB3])
    print("{:<10}{:<20}{:<20}{}".format("","(" + str(NUMBERS[randNum1]) + ")", "(" + str(NUMBERS[randNum2]) + ")", "(" + str(NUMBERS[randNum3]) + ")" ))

    CB1 = CB[randCB]
    CB2 = CB[randCB2]
    CB3 = CB[randCB3]

    NUM1 = NUMBERS[randNum1]
    NUM2 = NUMBERS[randNum2]
    NUM3 = NUMBERS[randNum3]

    for i in range(len(CB) - 1):
        if (CB[i] == CB1):
            CB.pop(i)

    for i in range(len(CB) - 1):
        if (CB[i] == CB2):
            CB.pop(i)

    for i in range(len(CB) - 1):
        if (CB[i] == CB3):
            CB.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM2):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM3):
            NUMBERS.pop(i)

def FiveInTheBack(LB, CB, RB, NUMBERS):
    randLB = random.randint(0, len(LB) - 1)
    randRB = random.randint(0, len(RB) - 1)
    randCB = random.randint(0, len(CB) - 1)
    randCB2 = random.randint(0, len(CB) - 1)
    randCB3 = random.randint(0, len(CB) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)
    randNum3 = random.randint(0, len(NUMBERS) - 1)
    randNum4 = random.randint(0, len(NUMBERS) - 1)
    randNum5 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    while (randNum3 == randNum1 or randNum3 == randNum2):
        randNum3 = random.randint(0, len(NUMBERS) - 1)
        if (randNum3 != randNum1 and randNum3 != randNum2):
            break

    while (randNum4 == randNum1 or randNum4 == randNum2 or randNum4 == randNum3):
        randNum4 = random.randint(0, len(NUMBERS) - 1)
        if (randNum4 != randNum1 and randNum4 != randNum2 and randNum4 != randNum3):
            break

    while (randNum5 == randNum1 or randNum5 == randNum2 or randNum5 == randNum3 or randNum5 == randNum4):
        randNum5 = random.randint(0, len(NUMBERS) - 1)
        if (randNum5 != randNum1 and randNum5 != randNum2 and randNum5 != randNum3 and randNum5 != randNum4):
            break

    print("\n{:<60}{}".format("LWB","RWB"))
    print("{:<60}{}".format(LB[randLB], RB[randRB]))
    print("{:<60}{}".format("(" + str(NUMBERS[randNum1]) + ")", "(" + str(NUMBERS[randNum2]) + ")"))
    print("{:<10}{:<20}{:<20}{}".format("","CB","CB","CB"))
    print("{:<10}{:<20}".format("", CB[randCB]), end="")
    while (randCB2 == randCB  or randCB2 == randCB3):
        randCB2 = random.randint(0, len(CB) - 1)
        if (randCB2 != randCB and randCB2 != randCB3):
            break
    print("{:<20}".format(CB[randCB2]), end="")
    while (randCB3 == randCB  or randCB3 == randCB2):
        randCB3 = random.randint(0, len(CB) - 1)
        if (randCB3 != randCB and randCB3 != randCB2):
            break
    print(CB[randCB3])
    print("{:<10}{:<20}{:<20}{}".format("","(" + str(NUMBERS[randNum3]) + ")", "(" + str(NUMBERS[randNum4]) + ")", "(" + str(NUMBERS[randNum5]) + ")" ))

    CB1 = CB[randCB]
    CB2 = CB[randCB2]
    CB3 = CB[randCB3]
    LB1 = LB[randLB]
    RB1 = RB[randRB]

    NUM1 = NUMBERS[randNum1]
    NUM2 = NUMBERS[randNum2]
    NUM3 = NUMBERS[randNum3]
    NUM4 = NUMBERS[randNum4]
    NUM5 = NUMBERS[randNum5]

    for i in range(len(CB) - 1):
        if (CB[i] == CB1):
            CB.pop(i)

    for i in range(len(CB) - 1):
        if (CB[i] == CB2):
            CB.pop(i)

    for i in range(len(CB) - 1):
        if (CB[i] == CB3):
            CB.pop(i)

    for i in range(len(LB) - 1):
        if (LB[i] == LB1):
            LB.pop(i)

    for i in range(len(RB) - 1):
        if (RB[i] == RB1):
            RB.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM2):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM3):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM4):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM5):
            NUMBERS.pop(i)

def TwoCDM(CDM, NUMBERS):
    randCDM = random.randint(0, len(CDM) - 1)
    randCDM2 = random.randint(0, len(CDM) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    print("\n{:<20}{:<20}{}".format("","CDM","CDM"))
    print("{:<20}{:<20}".format("",CDM[randCDM]), end="")
    while (randCDM2 == randCDM):
        randCDM2 = random.randint(0, len(CDM) - 1)
        if (randCDM2 != randCDM):
            break
    print(CDM[randCDM2])
    print("{:<20}{:<20}{}".format("","(" + str(NUMBERS[randNum1]) + ")", "(" + str(NUMBERS[randNum2]) + ")"))

    CDM1 = CDM[randCDM]
    CDM2 = CDM[randCDM2]

    NUM1 = NUMBERS[randNum1]
    NUM2 = NUMBERS[randNum2]

    for i in range(len(CDM) - 1):
        if (CDM[i] == CDM1):
            CDM.pop(i)

    for i in range(len(CDM) - 1):
        if (CDM[i] == CDM2):
            CDM.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM2):
            NUMBERS.pop(i)

def OneCDM(CDM, NUMBERS):
    randCDM = random.randint(0, len(CDM) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)

    print("\n{:<30}{}".format("","CDM"))
    print("{:<30}{}".format("",CDM[randCDM]))
    print("{:<30}{}".format("","(" + str(NUMBERS[randNum1]) + ")"))

    CDM1 = CDM[randCDM]

    NUM1 = NUMBERS[randNum1]

    for i in range(len(CDM) - 1):
        if (CDM[i] == CDM1):
            CDM.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

def FourInTheMiddle(CM, LM, RM, NUMBERS):
    randCM = random.randint(0, len(CM) - 1)
    randCM2 = random.randint(0, len(CM) - 1)
    randLM = random.randint(0, len(LM) - 1)
    randRM = random.randint(0, len(RM) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)
    randNum3 = random.randint(0, len(NUMBERS) - 1)
    randNum4 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    while (randNum3 == randNum1 or randNum3 == randNum2):
        randNum3 = random.randint(0, len(NUMBERS) - 1)
        if (randNum3 != randNum1 and randNum3 != randNum2):
            break

    while (randNum4 == randNum1 or randNum4 == randNum2 or randNum4 == randNum3):
        randNum4 = random.randint(0, len(NUMBERS) - 1)
        if (randNum4 != randNum1 and randNum4 != randNum2 and randNum4 != randNum3):
            break

    print("\n{:<20}{:<20}{:<20}{}".format("LM","CM","CM","RM"))
    print("{:<20}".format(LM[randLM]), end="")
    print("{:<20}".format(CM[randCM]), end="")
    while (randCM2 == randCM):
        randCM2 = random.randint(0, len(CM) - 1)
        if (randCM2 != randCM):
            break
    print("{:<20}".format(CM[randCM2]), end="")
    print(RM[randRM])
    print("{:<20}{:<20}{:<20}{}".format("(" + str(NUMBERS[randNum1]) + ")", "(" + str(NUMBERS[randNum2]) + ")", "(" + str(NUMBERS[randNum3]) + ")", "(" + str(NUMBERS[randNum4]) + ")"))

    CM1 = CM[randCM]
    CM2 = CM[randCM2]
    LM1 = LM[randLM]
    RM1 = RM[randRM]

    NUM1 = NUMBERS[randNum1]
    NUM2 = NUMBERS[randNum2]
    NUM3 = NUMBERS[randNum3]
    NUM4 = NUMBERS[randNum4]

    for i in range(len(CM) - 1):
        if (CM[i] == CM1):
            CM.pop(i)

    for i in range(len(CM) - 1):
        if (CM[i] == CM2):
            CM.pop(i)

    for i in range(len(LM) - 1):
        if (LM[i] == LM1):
            LM.pop(i)

    for i in range(len(RM) - 1):
        if (RM[i] == RM1):
            RM.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM2):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM3):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM4):
            NUMBERS.pop(i)

def ThreeCMInTheMiddle(CM, NUMBERS):
    randCM = random.randint(0, len(CM) - 1)
    randCM2 = random.randint(0, len(CM) - 1)
    randCM3 = random.randint(0, len(CM) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)
    randNum3 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    while (randNum3 == randNum1 or randNum3 == randNum2):
        randNum3 = random.randint(0, len(NUMBERS) - 1)
        if (randNum3 != randNum1 and randNum3 != randNum2):
            break

    print("\n{:<10}{:<20}{:<20}{}".format("","CM","CM","CM"))
    print("{:<10}{:<20}".format("",CM[randCM]), end="")
    while (randCM2 == randCM  or randCM2 == randCM3):
        randCM2 = random.randint(0, len(CM) - 1)
        if (randCM2 != randCM and randCM2 != randCM3):
            break
    print("{:<20}".format(CM[randCM2]), end="")
    while (randCM3 == randCM or randCM3 == randCM2):
        randCM3 = random.randint(0, len(CM) - 1)
        if (randCM3 != randCM and randCM3 != randCM2):
            break
    print(CM[randCM3])
    print("{:<10}{:<20}{:<20}{}".format("","(" + str(NUMBERS[randNum1]) + ")", "(" + str(NUMBERS[randNum2]) + ")", "(" + str(NUMBERS[randNum3]) + ")" ))

    CM1 = CM[randCM]
    CM2 = CM[randCM2]
    CM3 = CM[randCM3]

    NUM1 = NUMBERS[randNum1]
    NUM2 = NUMBERS[randNum2]
    NUM3 = NUMBERS[randNum3]

    for i in range(len(CM) - 1):
        if (CM[i] == CM1):
            CM.pop(i)

    for i in range(len(CM) - 1):
        if (CM[i] == CM2):
            CM.pop(i)

    for i in range(len(CM) - 1):
        if (CM[i] == CM3):
            CM.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM2):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM3):
            NUMBERS.pop(i)

def LeftRight(LM, RM, NUMBERS):
    randLM = random.randint(0, len(LM) - 1)
    randRM = random.randint(0, len(RM) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    print("\n{:<60}{}".format("LM","RM"))
    print("{:<60}".format(LM[randLM]), end="")
    print(RM[randRM])
    print("{:<60}{}".format("(" + str(NUMBERS[randNum1]) + ")", "(" + str(NUMBERS[randNum2]) + ")"))

    LM1 = LM[randLM]
    RM1 = RM[randRM]

    NUM1 = NUMBERS[randNum1]
    NUM2 = NUMBERS[randNum2]

    for i in range(len(LM) - 1):
        if (LM[i] == LM1):
            LM.pop(i)

    for i in range(len(RM) - 1):
        if (RM[i] == RM1):
            RM.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM2):
            NUMBERS.pop(i)

def TwoCM(CM, NUMBERS):
    randCM = random.randint(0, len(CM) - 1)
    randCM2 = random.randint(0, len(CM) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    print("\n{:<20}{:<20}{:<20}".format("","CM","CM"))
    print("{:<20}{:<20}".format("",CM[randCM]), end="")
    while (randCM2 == randCM):
        randCM2 = random.randint(0, len(CM) - 1)
        if (randCM2 != randCM):
            break
    print(CM[randCM2])
    print("{:<20}{:<20}{:<20}".format("","(" + str(NUMBERS[randNum1]) + ")", "(" + str(NUMBERS[randNum2]) + ")"))

    CM1 = CM[randCM]
    CM2 = CM[randCM2]

    NUM1 = NUMBERS[randNum1]
    NUM2 = NUMBERS[randNum2]

    for i in range(len(CM) - 1):
        if (CM[i] == CM1):
            CM.pop(i)

    for i in range(len(CM) - 1):
        if (CM[i] == CM2):
            CM.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM2):
            NUMBERS.pop(i)

def OneCAM(CAM, NUMBERS):
    randCAM = random.randint(0, len(CAM) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)

    print("\n{:<30}{}".format("","CAM"))
    print("{:<30}{}".format("",CAM[randCAM]))
    print("{:<30}{}".format("","(" + str(NUMBERS[randNum1]) + ")"))

    CAM1 = CAM[randCAM]

    NUM1 = NUMBERS[randNum1]

    for i in range(len(CAM) - 1):
        if (CAM[i] == CAM1):
            CAM.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

def TwoCAM(CAM, NUMBERS):
    randCAM = random.randint(0, len(CAM) - 1)
    randCAM2 = random.randint(0, len(CAM) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    print("\n{:<10}{:<40}{}".format("","CAM","CAM"))
    print("{:<10}{:<40}".format("",CAM[randCAM]), end="")
    print(CAM[randCAM2])
    print("{:<10}{:<40}{}".format("","(" + str(NUMBERS[randNum1]) + ")", "(" + str(NUMBERS[randNum2]) + ")"))

    CAM1 = CAM[randCAM]
    CAM2 = CAM[randCAM2]

    NUM1 = NUMBERS[randNum1]
    NUM2 = NUMBERS[randNum2]

    for i in range(len(CAM) - 1):
        if (CAM[i] == CAM1):
            CAM.pop(i)

    for i in range(len(CAM) - 1):
        if (CAM[i] == CAM2):
            CAM.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM2):
            NUMBERS.pop(i)
            
def LeftCAMRight(LM, RM, CAM, NUMBERS):
    randLM = random.randint(0, len(LM) - 1)
    randRM = random.randint(0, len(RM) - 1)
    randCAM = random.randint(0, len(CAM) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)
    randNum3 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    while (randNum3 == randNum1 or randNum3 == randNum2):
        randNum3 = random.randint(0, len(NUMBERS) - 1)
        if (randNum3 != randNum1 and randNum3 != randNum2):
            break

    print("\n{:<30}{:<30}{}".format("LM","CAM","RM"))
    print("{:<30}".format(LM[randLM]), end="")
    print("{:<30}".format(CAM[randCAM]), end="")
    print(RM[randRM])
    print("{:<30}{:<30}{}".format("(" + str(NUMBERS[randNum1]) + ")", "(" + str(NUMBERS[randNum2]) + ")", "(" + str(NUMBERS[randNum3]) + ")"))

    CAM1 = CAM[randCAM]
    LM1 = LM[randLM]
    RM1 = RM[randRM]

    NUM1 = NUMBERS[randNum1]
    NUM2 = NUMBERS[randNum2]
    NUM3 = NUMBERS[randNum3]

    for i in range(len(CAM) - 1):
        if (CAM[i] == CAM1):
            CAM.pop(i)

    for i in range(len(LM) - 1):
        if (LM[i] == LM1):
            LM.pop(i)

    for i in range(len(RM) - 1):
        if (RM[i] == RM1):
            RM.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM2):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM3):
            NUMBERS.pop(i)

def OneCF(CF, NUMBERS):
    randCF = random.randint(0, len(CF) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)

    print("\n{:<30}{}".format("","CF"))
    print("{:<30}{}".format("",CF[randCF]))
    print("{:<30}{}".format("","(" + str(NUMBERS[randNum1]) + ")"))

    CF1 = CF[randCF]

    NUM1 = NUMBERS[randNum1]

    for i in range(len(CF) - 1):
        if (CF[i] == CF1):
            CF.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

def OneST(ST, NUMBERS):
    randST = random.randint(0, len(ST) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)

    print("{:<30}{}".format("","ST"))
    print("{:<30}{}".format("",ST[randST]))
    print("{:<30}{}".format("","(" + str(NUMBERS[randNum1]) + ")"))

    ST1 = ST[randST]

    NUM1 = NUMBERS[randNum1]

    for i in range(len(ST) - 1):
        if (ST[i] == ST1):
            ST.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

def TwoST(ST, NUMBERS):
    randST = random.randint(0, len(ST) - 1)
    randST2 = random.randint(0, len(ST) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    print("{:<20}{:<20}{}".format("","ST","ST"))
    print("{:<20}{:<20}".format("",ST[randST]), end="")
    while (randST2 == randST):
        randST2 = random.randint(0, len(ST) - 1)
        if (randST2 != randST):
            break
    print(ST[randST2])
    print("{:<20}{:<20}{}".format("","(" + str(NUMBERS[randNum1]) + ")", "(" + str(NUMBERS[randNum2]) + ")"))

    ST1 = ST[randST]
    ST2 = ST[randST2]
    NUM1 = NUMBERS[randNum1]
    NUM2 = NUMBERS[randNum2]

    for i in range(len(ST) - 1):
        if (ST[i] == ST1):
            ST.pop(i)

    for i in range(len(ST) - 1):
        if (ST[i] == ST2):
            ST.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM2):
            NUMBERS.pop(i)

def FrontThree(RW, CF, LW, NUMBERS):
    randRW = random.randint(0, len(RW) - 1)
    randCF = random.randint(0, len(CF) - 1)
    randLW = random.randint(0, len(LW) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)
    randNum3 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    while (randNum3 == randNum1 or randNum3 == randNum2):
        randNum3 = random.randint(0, len(NUMBERS) - 1)
        if (randNum3 != randNum1 and randNum3 != randNum2):
            break

    print("{:<10}{:<20}{:<20}{}".format("","LW","CF","RW"))
    print("{:<10}{:<20}".format("",LW[randLW]), end="")
    print("{:<20}".format(CF[randCF]), end="")
    print("{}".format(RW[randRW]))
    print("{:<10}{:<20}{:<20}{}".format("","(" + str(NUMBERS[randNum1]) + ")", "(" + str(NUMBERS[randNum2]) + ")", "(" + str(NUMBERS[randNum3]) + ")"))

    LW1 = LW[randLW]
    CF1 = CF[randCF]
    RW1 = RW[randRW]

    NUM1 = NUMBERS[randNum1]
    NUM2 = NUMBERS[randNum2]
    NUM3 = NUMBERS[randNum3]

    for i in range(len(LW) - 1):
        if (LW[i] == LW1):
            LW.pop(i)

    for i in range(len(CF) - 1):
        if (CF[i] == CF1):
            CF.pop(i)

    for i in range(len(RW) - 1):
        if (RW[i] == RW1):
            RW.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM1):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM2):
            NUMBERS.pop(i)

    for i in range(len(NUMBERS) - 1):
        if (NUMBERS[i] == NUM3):
            NUMBERS.pop(i)

def generateTeam(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST, NUMBERS):
    randFormation = random.randint(0, len(FORMATIONS) - 1)
    #randFormation = 0

    if (randFormation == 0):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST, NUMBERS)
        LeftCAMRight(LM, RM, CAM, NUMBERS)
        TwoCDM(CDM, NUMBERS)
        ThreeInTheBack(CB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 1):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST, NUMBERS)
        FourInTheMiddle(CM, LM, RM, NUMBERS)
        FourInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 2):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST, NUMBERS)
        LeftCAMRight(LM, RM, CAM, NUMBERS)
        TwoCDM(CDM, NUMBERS)
        FourInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)
        

    if (randFormation == 3):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        FrontThree(RW, CF, LW, NUMBERS)
        ThreeCMInTheMiddle(CM, NUMBERS)
        FourInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 4):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST, NUMBERS)
        OneCAM(CAM, NUMBERS)
        FourInTheMiddle(CM, LM, RM, NUMBERS)
        FourInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 5):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST, NUMBERS)
        OneCAM(CAM, NUMBERS)
        LeftRight(LM, RM, NUMBERS)
        OneCDM(CDM, NUMBERS)
        FourInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 6):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST, NUMBERS)
        OneCAM(CAM, NUMBERS)
        TwoCM(CM, NUMBERS)
        OneCDM(CDM, NUMBERS)
        FourInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 7):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST, NUMBERS)
        OneCAM(CAM, NUMBERS)
        TwoCDM(CDM, NUMBERS)
        FiveInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 8):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        FrontThree(RW, CF, LW, NUMBERS)
        TwoCM(CM, NUMBERS)
        FiveInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)
        
    if (randFormation == 9):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        FrontThree(RW, CF, LW, NUMBERS)
        FourInTheMiddle(CM, LM, RM, NUMBERS)
        ThreeInTheBack(CB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 10):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST, NUMBERS)
        FourInTheMiddle(CM, LM, RM, NUMBERS)
        OneCDM(CDM, NUMBERS)
        FourInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 11):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST, NUMBERS)
        TwoCAM(CAM, NUMBERS)
        TwoCDM(CDM, NUMBERS)
        FourInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 12):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST, NUMBERS)
        TwoCAM(CAM, NUMBERS)
        LeftRight(LM, RM, NUMBERS)
        OneCDM(CDM, NUMBERS)
        FourInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 13):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST, NUMBERS)
        LeftRight(LM, RM, NUMBERS)
        TwoCDM(CDM, NUMBERS)
        FiveInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 14):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST, NUMBERS)
        TwoCAM(CAM, NUMBERS)
        LeftRight(LM, RM, NUMBERS)
        TwoCDM(CDM, NUMBERS)
        ThreeInTheBack(CB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 15):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        FrontThree(RW, CF, LW, NUMBERS)
        TwoCAM(CAM, NUMBERS)
        TwoCDM(CDM, NUMBERS)
        ThreeInTheBack(CB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 16):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST, NUMBERS)
        ThreeCMInTheMiddle(CM, NUMBERS)
        TwoCDM(CDM, NUMBERS)
        ThreeInTheBack(CB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 17):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST, NUMBERS)
        OneCAM(CAM, NUMBERS)
        ThreeCMInTheMiddle(CM, NUMBERS)
        FiveInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 18):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST, NUMBERS)
        LeftCAMRight(LM, RM, CAM, NUMBERS)
        TwoCDM(CDM, NUMBERS)
        ThreeInTheBack(CB, NUMBERS)
        TheGK(GK, NUMBERS)

    if (randFormation == 19):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        FrontThree(RW, CF, LW, NUMBERS)
        OneCAM(CAM, NUMBERS)
        TwoCDM(CDM, NUMBERS)
        FourInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)
    
    if (randFormation == 20):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        FrontThree(RW, CF, LW, NUMBERS)
        OneCAM(CAM, NUMBERS)
        TwoCM(CDM, NUMBERS)
        FourInTheBack(LB, CB, RB, NUMBERS)
        TheGK(GK, NUMBERS)

    randFormation = random.randint(0, len(FORMATIONS) - 1)

def generateBench(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST, NUMBERS):
    randGK = random.randint(0, len(GK) - 1)
    randLB = random.randint(0, len(LB) - 1)
    randCB = random.randint(0, len(CB) - 1)
    randRB = random.randint(0, len(RB) - 1)
    randCDM = random.randint(0, len(CDM) - 1)
    randCM = random.randint(0, len(CM) - 1)
    randCAM = random.randint(0, len(CAM) - 1)
    randLM = random.randint(0, len(LM) - 1)
    randRM = random.randint(0, len(RM) - 1)
    randRW = random.randint(0, len(RW) - 1)
    randCF = random.randint(0, len(CF) - 1)
    randLW = random.randint(0, len(LW) - 1)
    randST = random.randint(0, len(ST) - 1)

    randNum1 = random.randint(0, len(NUMBERS) - 1)
    randNum2 = random.randint(0, len(NUMBERS) - 1)
    randNum3 = random.randint(0, len(NUMBERS) - 1)
    randNum4 = random.randint(0, len(NUMBERS) - 1)
    randNum5 = random.randint(0, len(NUMBERS) - 1)
    randNum6 = random.randint(0, len(NUMBERS) - 1)
    randNum7 = random.randint(0, len(NUMBERS) - 1)
    randNum8 = random.randint(0, len(NUMBERS) - 1)
    randNum9 = random.randint(0, len(NUMBERS) - 1)
    randNum10 = random.randint(0, len(NUMBERS) - 1)
    randNum11 = random.randint(0, len(NUMBERS) - 1)
    randNum12 = random.randint(0, len(NUMBERS) - 1)
    randNum13 = random.randint(0, len(NUMBERS) - 1)

    while (randNum2 == randNum1):
        randNum2 = random.randint(0, len(NUMBERS) - 1)
        if (randNum2 != randNum1):
            break

    while (randNum3 == randNum1 or randNum3 == randNum2):
        randNum3 = random.randint(0, len(NUMBERS) - 1)
        if (randNum3 != randNum1 and randNum3 != randNum2):
            break

    while (randNum4 == randNum1 or randNum4 == randNum2 or randNum4 == randNum3):
            randNum4 = random.randint(0, len(NUMBERS) - 1)
            if (randNum4 != randNum1 and randNum4 != randNum2 and randNum4 != randNum3):
                break

    while (randNum5 == randNum1 or randNum5 == randNum2 or randNum5 == randNum3 or randNum5 == randNum4):
            randNum5 = random.randint(0, len(NUMBERS) - 1)
            if (randNum5 != randNum1 and randNum5 != randNum2 and randNum5 != randNum3 and randNum5 != randNum4):
                break

    while (randNum6 == randNum1 or randNum6 == randNum2 or randNum6 == randNum3 or randNum6 == randNum4 or randNum6 == randNum5):
            randNum6 = random.randint(0, len(NUMBERS) - 1)
            if (randNum6 != randNum1 and randNum6 != randNum2 and randNum6 != randNum3 and randNum6 != randNum4 and randNum6 != randNum5):
                break

    while (randNum7 == randNum1 or randNum7 == randNum2 or randNum7 == randNum3 or randNum7 == randNum4 or randNum7 == randNum5 or randNum7 == randNum6):
            randNum7 = random.randint(0, len(NUMBERS) - 1)
            if (randNum7 != randNum1 and randNum7 != randNum2 and randNum7 != randNum3 and randNum7 != randNum4 and randNum7 != randNum5 and randNum7 != randNum6):
                break

    while (randNum8 == randNum1 or randNum8 == randNum2 or randNum8 == randNum3 or randNum8 == randNum4 or randNum8 == randNum5 or randNum8 == randNum6 or randNum8 == randNum7):
            randNum8 = random.randint(0, len(NUMBERS) - 1)
            if (randNum8 != randNum1 and randNum8 != randNum2 and randNum8 != randNum3 and randNum8 != randNum4 and randNum8 != randNum5 and randNum8 != randNum6 and randNum8 != randNum7):
                break

    while (randNum9 == randNum1 or randNum9 == randNum2 or randNum9 == randNum3 or randNum9 == randNum4 or randNum9 == randNum5 or randNum9 == randNum6 or randNum9 == randNum7 or randNum9 == randNum8):
            randNum9 = random.randint(0, len(NUMBERS) - 1)
            if (randNum9 != randNum1 and randNum9 != randNum2 and randNum9 != randNum3 and randNum9 != randNum4 and randNum9 != randNum5 and randNum9 != randNum6 and randNum9 != randNum7 and randNum9 != randNum8):
                break

    while (randNum10 == randNum1 or randNum10 == randNum2 or randNum10 == randNum3 or randNum10 == randNum4 or randNum10 == randNum5 or randNum10 == randNum6 or randNum10 == randNum7 or randNum10 == randNum8 or randNum10 == randNum9):
            randNum10 = random.randint(0, len(NUMBERS) - 1)
            if (randNum10 != randNum1 and randNum10 != randNum2 and randNum10 != randNum3 and randNum10 != randNum4 and randNum10 != randNum5 and randNum10 != randNum6 and randNum10 != randNum7 and randNum10 != randNum8 and randNum10 != randNum9):
                break

    while (randNum11 == randNum1 or randNum11 == randNum2 or randNum11 == randNum3 or randNum11 == randNum4 or randNum11 == randNum5 or randNum11 == randNum6 or randNum11 == randNum7 or randNum11 == randNum8 or randNum11 == randNum9 or randNum11 == randNum10):
            randNum11 = random.randint(0, len(NUMBERS) - 1)
            if (randNum11 != randNum1 and randNum10 != randNum2 and randNum10 != randNum3 and randNum11 != randNum4 and randNum11 != randNum5 and randNum11 != randNum6 and randNum11 != randNum7 and randNum11 != randNum8 and randNum11 != randNum9 and randNum11 != randNum10):
                break

    while (randNum12 == randNum1 or randNum12 == randNum2 or randNum12 == randNum3 or randNum12 == randNum4 or randNum12 == randNum5 or randNum12 == randNum6 or randNum12 == randNum7 or randNum12 == randNum8 or randNum12 == randNum9 or randNum12 == randNum10 or randNum12 == randNum11):
            randNum12 = random.randint(0, len(NUMBERS) - 1)
            if (randNum12 != randNum1 and randNum10 != randNum2 and randNum10 != randNum3 and randNum12 != randNum4 and randNum12 != randNum5 and randNum12 != randNum6 and randNum12 != randNum7 and randNum12 != randNum8 and randNum12 != randNum9 and randNum12 != randNum10 and randNum12 != randNum11):
                break

    while (randNum13 == randNum1 or randNum13 == randNum2 or randNum13 == randNum3 or randNum13 == randNum4 or randNum13 == randNum5 or randNum13 == randNum6 or randNum13 == randNum7 or randNum13 == randNum8 or randNum13 == randNum9 or randNum13 == randNum10 or randNum13 == randNum11 or randNum13 == randNum12):
            randNum13 = random.randint(0, len(NUMBERS) - 1)
            if (randNum13 != randNum1 and randNum10 != randNum2 and randNum10 != randNum3 and randNum13 != randNum4 and randNum13 != randNum5 and randNum13 != randNum6 and randNum13 != randNum7 and randNum13 != randNum8 and randNum13 != randNum9 and randNum13 != randNum10 and randNum13 != randNum11 and randNum13 != randNum12):
                break

    print("GK:  {:<20}{}".format(GK[randGK], "(" + str(NUMBERS[randNum1]) + ")"))
    print("LB:  {:<20}{}".format(LB[randLB], "(" + str(NUMBERS[randNum2]) + ")"))
    print("CB:  {:<20}{}".format(CB[randCB], "(" + str(NUMBERS[randNum3]) + ")"))
    print("RB:  {:<20}{}".format(RB[randRB], "(" + str(NUMBERS[randNum4]) + ")"))
    print("CDM: {:<20}{}".format(CDM[randCDM], "(" + str(NUMBERS[randNum5]) + ")"))
    print("CM:  {:<20}{}".format(CM[randCM], "(" + str(NUMBERS[randNum6]) + ")"))
    print("CAM: {:<20}{}".format(CAM[randCAM], "(" + str(NUMBERS[randNum7]) + ")"))
    print("LM:  {:<20}{}".format(LM[randLM], "(" + str(NUMBERS[randNum8] ) + ")"))
    print("RM:  {:<20}{}".format(RM[randRM], "(" + str(NUMBERS[randNum9] ) + ")"))
    print("RW:  {:<20}{}".format(RW[randRW], "(" + str(NUMBERS[randNum10]) + ")"))
    print("CF:  {:<20}{}".format(CF[randCF], "(" + str(NUMBERS[randNum11]) + ")"))
    print("LW:  {:<20}{}".format(LW[randLW], "(" + str(NUMBERS[randNum12]) + ")"))
    print("ST:  {:<20}{}".format(ST[randST], "(" + str(NUMBERS[randNum13]) + ")"))

    GK1 = GK[randGK]
    CB1 = CB[randCB]
    LB1 = LB[randLB]
    RB1 = RB[randRB]
    CDM1 = CDM[randCDM]
    CM1 = CM[randCM]
    CAM1 = CAM[randCAM]
    LM1 = LM[randLM]
    RM1 = RM[randRM]
    LW1 = LW[randLW]
    CF1 = CF[randCF]
    RW1 = RW[randRW]
    ST1 = ST[randST]

    for i in range(len(GK) - 1):
        if (GK[i] == GK1):
            GK.pop(i)

    for i in range(len(CB) - 1):
        if (CB[i] == CB1):
            CB.pop(i)

    for i in range(len(LB) - 1):
        if (LB[i] == LB1):
            LB.pop(i)

    for i in range(len(RB) - 1):
        if (RB[i] == RB1):
            RB.pop(i)

    for i in range(len(CDM) - 1):
        if (CDM[i] == CDM1):
            CDM.pop(i)

    for i in range(len(CM) - 1):
        if (CM[i] == CM1):
            CM.pop(i)

    for i in range(len(CAM) - 1):
        if (CAM[i] == CAM1):
            CAM.pop(i)

    for i in range(len(LM) - 1):
        if (LM[i] == LM1):
            LM.pop(i)

    for i in range(len(RM) - 1):
        if (RM[i] == RM1):
            RM.pop(i)

    for i in range(len(LW) - 1):
        if (LW[i] == LW1):
            LW.pop(i)

    for i in range(len(CF) - 1):
        if (CF[i] == CF1):
            CF.pop(i)

    for i in range(len(RW) - 1):
        if (RW[i] == RW1):
            RW.pop(i)

    for i in range(len(ST) - 1):
        if (ST[i] == ST1):
            ST.pop(i)

def longName(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST):
    tempGK = ""
    tempLB = ""
    tempCB = ""
    tempRB = ""
    tempCDM = ""
    tempCM = ""
    tempCAM = ""
    tempLM = ""
    tempRM = ""
    tempRW = ""
    tempCF = ""
    tempLW = ""
    tempST = ""
    tempArr = []

    for i in GK:
        if (len(i) > len(tempGK)):
            tempGK = i
    for i in LB:
        if (len(i) > len(tempLB)):
            tempLB = i
    for i in CB:
        if (len(i) > len(tempCB)):
            tempCB = i
    for i in RB:
        if (len(i) > len(tempRB)):
            tempRB = i
    for i in CDM:
        if (len(i) > len(tempCDM)):
            tempCDM = i
    for i in CM:
        if (len(i) > len(tempCM)):
            tempCM = i
    for i in CAM:
        if (len(i) > len(tempCAM)):
            tempCAM = i
    for i in LM:
        if (len(i) > len(tempLM)):
            tempLM = i
    for i in RM:
        if (len(i) > len(tempRM)):
            tempRM = i
    for i in RW:
        if (len(i) > len(tempRW)):
            tempRW = i
    for i in CF:
        if (len(i) > len(tempCF)):
            tempCF = i
    for i in LW:
        if (len(i) > len(tempLW)):
            tempLW = i
    for i in ST:
        if (len(i) > len(tempST)):
            tempST = i

    tempArr.append(tempGK)
    tempArr.append(tempLB)
    tempArr.append(tempCB)
    tempArr.append(tempRB)
    tempArr.append(tempCDM)
    tempArr.append(tempCM)
    tempArr.append(tempCAM)
    tempArr.append(tempLM)
    tempArr.append(tempRM)
    tempArr.append(tempRW)
    tempArr.append(tempCF)
    tempArr.append(tempLW)
    tempArr.append(tempST)

    tempLong = ""
    for i in tempArr:
        if len(i) > len(tempLong):
            tempLong = i
    
    print("name:" + tempLong + "\nlength: " + (str(len(tempLong))))

def clear():
    os.system("cls")

def main():
    inp = input
    while (inp != "q".upper()):
        clear()
        GK = ["Oblak", "Alisson", "Ter Stegen", "Courtois", "Neuer", "Ederson", "De Gea", "Szczesny", "Handanovic", "Leno", "Gulácsi", "Lloris", "Donnarumma", "Navas", "Sommer", "Onana", "Meret", "Casteels", "Rui Patrício", "Fabianski", "Strakosha", "Musso", "Pickford", "Kepa", "Hrádecký", "Anthony Lopes", "Cilliessen", "Mandanda", "Muslera", "Sirigu", "Schmeichel", "Mendy", "Unai Simón", "Pavlenka", "Pau López", "Maignan", "Benítez", "Rulli", "Neto", "Lecomte", "Andrada", "Asenjo", "Ospina", "Ruffier", "Henderson", "David Soria", "Dúbravka", "Pacheco", "Pope", "Cragno", "Aitor Fernández", "Bounou", "Armani", "Vaclík", "Areola"]
        LB = ["Robertson", "Guerreiro", "Jordi Alba", "Hernandez", "Alex Sandro", "Tagliafico", "Davies", "Renan Lodi", "Hernández", "Chilwell", "F.Mendy", "Alex Telles", "Kolarov", "Marcelo", "Tierney", "Acuna", "Álex Grimaldo", "José Gayà", "B.Mendy", "Digne", "Juan Bernat", "Reguilón", "Fabra", "Spinazzola"]
        CB = ["Van Dijk", "Sergio Ramos", "Varane", "Koulibaly", "Alaba", "Piqué", "Süle", "De Ligt", "Skriniar", "Lenglet", "Giménez", "Laporte", "De Vrij", "Thiago Silva", "Chiellini", "Maguire", "Umtiti", "Acerbi", "Manolas", "Alderweireld", "Bonucci", "Rúben Dias", "Koundé", "Sánchez", "Kimpembe", "Ginter", "Romagnoli", "Felipe", "Vertonghen", "Benatia", "Pau Torres", "Éder Militao", "Djené", "Rüdiger", "Joe Gomez", "Diego Carlos", "Savic", "Boateng", "David Luiz"]
        RB = ["Alexander-Arnold", "Carvajal", "Ricardo Pereira", "Jesus Navas", "Wan-Bissaka", "Hakimi", "Nélson Semedo", "Pavard", "Trippier", "Sergi Roberto", "Kyle Walker", "Cuadrado", "Azpilicueta", "Di Lorenzo", "Bellerín", "Joao Cancelo", "Florenzi", "Meunier", "Mário Fernandes", "Youcef Atal", "Dumfries", "Danilo", "Lars Bender", "Dest"]
        CDM = ["Kimmich", "Casemiro", "Sergio Busquets", "Marquinhos", "Fabinho", "Pjanic", "Rodri", "Partey", "Jorginho", "Witsel", "Fernandinho", "Ndidi", "Allan", "Javi Martínez", "Zakaria", "Torreira", "Emre Can", "Xhaka", "Lucas Leiva", "Barrios", "Paredes", "Matic", "Delaney", "Gabi"]
        CM = ["Kanté", "Thiago", "Kroos", "De Jong", "Saúl", "Verratti", "Milinkovic-Savic", "Luis Alberto", "Pogba", "Koke", "Dani Parejo", "Modric", "Iniesta", "Valverde", "Arthur", "Sabitzer", "Goretzka", "Brozovic", "Gündogan", "Nainggolan", "Henderson", "Rakitic", "Wijnaldum", "Ndombèlé", "Fabián Ruiz", "Bentancur", "De Paul", "Sergio Canales", "Pellegrini", "Dani Ceballos", "Rúben Neves", "Barella", "Tolisso", "Tielemans", "Kovacic", "Gueye", "Aránguiz", "Ramsey", "Vidal", "Matuidi", "Santi Cazorla", "Joao Moutinho", "Paulinho"]
        CAM = ["De Bruyne", "Bruno Fernandes", "Havertz", "Marcos Llorente", "Coutinho", "Papu Gómez", "Isco", "Eriksen", "David Silva", "Odegaard", "Calhanoglu", "Brandt", "Fekir", "Maddison", "Van De Beek", "Zielinski", "Draxler", "Özil", "Oscar", "Mount", "Zaniolo", "Forsberg", "De Arrascaeta", "Mkhitaryan"]
        LM = ["Heung-Min Son", "Kostic", "Carrasco", "Perisic", "Felipe Anderson", "Thomas Lemar", "Gosens", "Bergwijn", "El Shaarawy", "Vitolo", "Saint-Maximin", "Lulic", "Bamba", "Claesson", "Deulofeu", "Cornet", "Fraser", "Jony", "Bouanga", "Pablo FFornals", "Barnes", "Saka", "Szoboszlai", "Redmond"]
        RM = ["Pizzi", "Corona", "Lucas Moura", "Correa", "Visca", "Everton Ribeiro", "Caligiuri", "Joaquín", "Candreva", "Ayoze Pérez", "Hateboer", "Lazzari", "Lamela"]
        RW = ["Messi", "Salah", "Bernardo Silva", "Gnabry", "Di María", "Sancho", "Mahrez", "Ziyech", "Pépé", "Thauvin", "Ocampos", "Pablo Sarabia", "James Rodríguez", "Douglas Costa", "Willian", "Bale", "Chiesa", "Asensio", "Portu", "Coman", "Berghuis", "José Callejón", "Ferran Torres", "Malcom"]
        CF = ["Dybala", "Müller", "Ilicic", "Lobato", "Correa", "Joao Félix", "Tevez", "Kruse", "Joao Pedro", "Corte Real", "Giovinco", "Quaison", "Marega", "Waldschmidt", "Moniz", "Vietto", "Philipp", "Jonathan David", "Zárate"]
        LW = ["Ronaldo", "Neymar", "Mané","Sterling", "Griezmann", "Eden Hazard", "Rashford", "Sané", "Dembéle", "Oyarzabal", "Insigne", "Richarlison", "Payet", "Pavón", "Grealish", "Rebic", "Ansu Fati", "Lozano", "Pulisic", "Diogo Jota", "Goncalo Guedes", "Bruno Henrique", "Thorgan Hazard", "Promes", "Éverton", "Zaha", "Taison", "Vinícius Júnior", "Rashica", "Perotti", "Baldé", "Diaby"]
        ST = ["Lewandowski", "Mbappé", "Kane", "Agüero", "Aubameyang", "Suárez", "Benzema", "Roberto Firmino", "Immobile", "Håland", "Werner", "Vardy", "Icardi", "Lukaku", "Cavani", "Martínez", "Gabriel Jesus", "Zapata", "Jiménez", "Depay", "Iago Aspas", "Ben Yedder", "Mertens", "Dzeko", "Higuaín", "Ibrahimovic", "Weghorst", "Belotti", "Morata", "Lacazette", "Mandzukic", "Jovic", "André Silva", "Danny Ings", "Moussa Dembéle", "Volland", "Milik", "Gerard Moreno", "Martial", "Muriel", "Rodrigo", "Tadic", "Dzyuba", "Falcao", "Arnautovic", "Calbert-Lewin", "Abraham", "Gómez", "Wilson", "Williams", "Alario", "Gabriel Barbosa", "Benedetto", "Paco Alcácer", "Alex Teixeira", "Caputo", "Giroud", "Diego Costa", "Sánchez", "Quagliarella", "Osimhen", "Schick", "Embolo", "King", "Lasagna"]
        NUMBERS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
        print("---------------------------------------------------------------------------------")
        #longName(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST)
        print("1. Generate 1 team\n2. Generate 2 teams\nQ. Quit")
        print("---------------------------------------------------------------------------------")
        inp = str(input("INPUT: ").upper())
        if (inp == "1"):
            clear()
            print("---------------------------------------------------------------------------------")
            print("Team:")
            generateTeam(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST, NUMBERS)
            print("\n---------------------------------------------------------------------------------")
            print("\nBench:")
            generateBench(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST, NUMBERS)
            print()
            input("Press enter to continue...")
        elif (inp == "2"):
            clear()
            print("---------------------------------------------------------------------------------")
            print("Team 1:")
            generateTeam(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST, NUMBERS)
            print("\n---------------------------------------------------------------------------------")
            NUMBERS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
            print("\nTeam 2:")
            generateTeam(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST, NUMBERS)
            print("\n---------------------------------------------------------------------------------")
            print("\nTeam 2 Bench:\n")
            generateBench(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST, NUMBERS)
            print("\n---------------------------------------------------------------------------------")
            print("\nTeam 1 Bench:\n")
            generateBench(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST, NUMBERS)
            print()
            input("Press enter to continue...")
        elif (inp == "q".upper()):
            break
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
