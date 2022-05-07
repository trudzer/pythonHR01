import random

FORMATIONS = ["3-5-2", "4-4-2", "4-2-3-1", "4-3-3", "4-4-1-1", "4-1-2-1-2", "4-1-2-1-2", "5-2-1-2", "5-2-3", "3-4-3", "4-1-4-1", "4-2-2-2", "4-1-2-2-1", "5-2-2-1", "3-2-2-2-1", "3-2-1-3",  "3-2-3-2", "5-3-1-1"]

def TheGK(GK):
    randGK = random.randint(0, len(GK) - 1)

    print("\n\t\t{}".format(GK[randGK]))

    GK1 = GK[randGK]

    for i in range(len(GK) - 1):
        if (GK[i] == GK1):
            GK.pop(i)

def FourInTheBack(LB, CB, RB):
    randLB = random.randint(0, len(LB) - 1)
    randCB = random.randint(0, len(CB) - 1)
    randCB2 = random.randint(0, len(CB) - 1)
    randRB = random.randint(0, len(RB) - 1)

    print("\n{}\t".format(LB[randLB]), end="")
    print("{}\t\t".format(CB[randCB]),end="")
    while (randCB2 == randCB):
        randCB2 = random.randint(0, len(CB) - 1)
        if (randCB2 != randCB):
            break
    print("{}\t".format(CB[randCB2]), end="")
    print(RB[randRB])

    CB1 = CB[randCB]
    CB2 = CB[randCB2]
    LB1 = LB[randLB]
    RB1 = RB[randRB]

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


def ThreeInTheBack(CB):
    randCB = random.randint(0, len(CB) - 1)
    randCB2 = random.randint(0, len(CB) - 1)
    randCB3 = random.randint(0, len(CB) - 1)

    print("\n\t{}\t".format(CB[randCB]), end="")
    while (randCB2 == randCB  or randCB2 == randCB3):
        randCB2 = random.randint(0, len(CB) - 1)
        if (randCB2 != randCB and randCB2 != randCB3):
            break
    print("{}\t".format(CB[randCB2]), end="")
    while (randCB3 == randCB  or randCB3 == randCB2):
        randCB3 = random.randint(0, len(CB) - 1)
        if (randCB3 != randCB and randCB3 != randCB2):
            break
    print(CB[randCB3])

    CB1 = CB[randCB]
    CB2 = CB[randCB2]
    CB3 = CB[randCB3]

    for i in range(len(CB) - 1):
        if (CB[i] == CB1):
            CB.pop(i)

    for i in range(len(CB) - 1):
        if (CB[i] == CB2):
            CB.pop(i)

    for i in range(len(CB) - 1):
        if (CB[i] == CB3):
            CB.pop(i)

def FiveInTheBack(LB, CB, RB):
    randLB = random.randint(0, len(LB) - 1)
    randRB = random.randint(0, len(RB) - 1)
    randCB = random.randint(0, len(CB) - 1)
    randCB2 = random.randint(0, len(CB) - 1)
    randCB3 = random.randint(0, len(CB) - 1)

    print("\n{}\t\t\t\t{}\n".format(LB[randLB], RB[randRB]), end="")
    print("\n\t{}\t".format(CB[randCB]), end="")
    while (randCB2 == randCB  or randCB2 == randCB3):
        randCB2 = random.randint(0, len(CB) - 1)
        if (randCB2 != randCB and randCB2 != randCB3):
            break
    print("{}\t".format(CB[randCB2]), end="")
    while (randCB3 == randCB  or randCB3 == randCB2):
        randCB3 = random.randint(0, len(CB) - 1)
        if (randCB3 != randCB and randCB3 != randCB2):
            break
    print("{}".format(CB[randCB3]))

    CB1 = CB[randCB]
    CB2 = CB[randCB2]
    CB3 = CB[randCB3]
    LB1 = LB[randLB]
    RB1 = RB[randRB]

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

def TwoCDM(CDM):
    randCDM = random.randint(0, len(CDM) - 1)
    randCDM2 = random.randint(0, len(CDM) - 1)

    print("\n\t{}\t\t".format(CDM[randCDM]), end="")
    while (randCDM2 == randCDM):
        randCDM2 = random.randint(0, len(CDM) - 1)
        if (randCDM2 != randCDM):
            break
    print(CDM[randCDM2])

    CDM1 = CDM[randCDM]
    CDM2 = CDM[randCDM2]

    for i in range(len(CDM) - 1):
        if (CDM[i] == CDM1):
            CDM.pop(i)

    for i in range(len(CDM) - 1):
        if (CDM[i] == CDM2):
            CDM.pop(i)

def OneCDM(CDM):
    randCDM = random.randint(0, len(CDM) - 1)

    print("\n\t\t{}".format(CDM[randCDM]))

    CDM1 = CDM[randCDM]

    for i in range(len(CDM) - 1):
        if (CDM[i] == CDM1):
            CDM.pop(i)

def FourInTheMiddle(CM, LM, RM):
    randCM = random.randint(0, len(CM) - 1)
    randCM2 = random.randint(0, len(CM) - 1)
    randLM = random.randint(0, len(LM) - 1)
    randRM = random.randint(0, len(RM) - 1)

    print("\n{}\t".format(LM[randLM]), end="")
    print("{}\t\t".format(CM[randCM]), end="")
    while (randCM2 == randCM):
        randCM2 = random.randint(0, len(CM) - 1)
        if (randCM2 != randCM):
            break
    print("{}\t".format(CM[randCM2]), end="")
    print(RM[randRM])

    CM1 = CM[randCM]
    CM2 = CM[randCM2]
    LM1 = LM[randLM]
    RM1 = RM[randRM]

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

def ThreeCMInTheMiddle(CM):
    randCM = random.randint(0, len(CM) - 1)
    randCM2 = random.randint(0, len(CM) - 1)
    randCM3 = random.randint(0, len(CM) - 1)

    print("\n\t{}\t".format(CM[randCM]), end="")
    while (randCM2 == randCM  or randCM2 == randCM3):
        randCM2 = random.randint(0, len(CM) - 1)
        if (randCM2 != randCM and randCM2 != randCM3):
            break
    print("{}\t".format(CM[randCM2]), end="")
    while (randCM3 == randCM or randCM3 == randCM2):
        randCM3 = random.randint(0, len(CM) - 1)
        if (randCM3 != randCM and randCM3 != randCM2):
            break
    print(CM[randCM3])

    CM1 = CM[randCM]
    CM2 = CM[randCM2]
    CM3 = CM[randCM3]

    for i in range(len(CM) - 1):
        if (CM[i] == CM1):
            CM.pop(i)

    for i in range(len(CM) - 1):
        if (CM[i] == CM2):
            CM.pop(i)

    for i in range(len(CM) - 1):
        if (CM[i] == CM3):
            CM.pop(i)

def LeftRight(LM, RM):
    randLM = random.randint(0, len(LM) - 1)
    randRM = random.randint(0, len(RM) - 1)

    print("\n{}\t\t\t\t".format(LM[randLM]), end="")
    print(RM[randRM])

    LM1 = LM[randLM]
    RM1 = RM[randRM]

    for i in range(len(LM) - 1):
        if (LM[i] == LM1):
            LM.pop(i)

    for i in range(len(RM) - 1):
        if (RM[i] == RM1):
            RM.pop(i)

def TwoCM(CM):
    randCM = random.randint(0, len(CM) - 1)
    randCM2 = random.randint(0, len(CM) - 1)

    print("\n\t{}\t\t".format(CM[randCM]), end="")
    while (randCM2 == randCM):
        randCM2 = random.randint(0, len(CM) - 1)
        if (randCM2 != randCM):
            break
    print(CM[randCM2])

    CM1 = CM[randCM]
    CM2 = CM[randCM2]

    for i in range(len(CM) - 1):
        if (CM[i] == CM1):
            CM.pop(i)

    for i in range(len(CM) - 1):
        if (CM[i] == CM2):
            CM.pop(i)

def OneCAM(CAM):
    randCAM = random.randint(0, len(CAM) - 1)

    print("\n\t\t{}".format(CAM[randCAM]))

    CAM1 = CAM[randCAM]

    for i in range(len(CAM) - 1):
        if (CAM[i] == CAM1):
            CAM.pop(i)

def TwoCAM(CAM):
    randCAM = random.randint(0, len(CAM) - 1)
    randCAM2 = random.randint(0, len(CAM) - 1)

    print("\n\t{}\t\t".format(CAM[randCAM]), end="")
    print(CAM[randCAM2])

    CAM1 = CAM[randCAM]
    CAM2 = CAM[randCAM2]

    for i in range(len(CAM) - 1):
        if (CAM[i] == CAM1):
            CAM.pop(i)

    for i in range(len(CAM) - 1):
        if (CAM[i] == CAM2):
            CAM.pop(i)

def LeftCAMRight(LM, RM, CAM):
    randLM = random.randint(0, len(LM) - 1)
    randRM = random.randint(0, len(RM) - 1)
    randCAM = random.randint(0, len(CAM) - 1)

    print("\n{}\t\t".format(LM[randLM]), end="")
    print("{}\t\t".format(CAM[randCAM]), end="")
    print(RM[randRM])

    CAM1 = CAM[randCAM]
    LM1 = LM[randLM]
    RM1 = RM[randRM]

    for i in range(len(CAM) - 1):
        if (CAM[i] == CAM1):
            CAM.pop(i)

    for i in range(len(LM) - 1):
        if (LM[i] == LM1):
            LM.pop(i)

    for i in range(len(RM) - 1):
        if (RM[i] == RM1):
            RM.pop(i)

def OneCF(CF):
    randCF = random.randint(0, len(CF) - 1)

    print("\n\t\t{}".format(CF[randCF]))

    CF1 = CF[randCF]

    for i in range(len(CF) - 1):
        if (CF[i] == CF1):
            CF.pop(i)

def OneST(ST):
    randST = random.randint(0, len(ST) - 1)

    print("\t\t{}".format(ST[randST]))

    ST1 = ST[randST]

    for i in range(len(ST) - 1):
        if (ST[i] == ST1):
            ST.pop(i)

def TwoST(ST):
    randST = random.randint(0, len(ST) - 1)
    randST2 = random.randint(0, len(ST) - 1)

    print("\t{}\t\t".format(ST[randST]), end="")
    while (randST2 == randST):
        randST2 = random.randint(0, len(ST) - 1)
        if (randST2 != randST):
            break
    print(ST[randST2])

    ST1 = ST[randST]
    ST2 = ST[randST2]

    for i in range(len(ST) - 1):
        if (ST[i] == ST1):
            ST.pop(i)

    for i in range(len(ST) - 1):
        if (ST[i] == ST2):
            ST.pop(i)

def FrontThree(RW, CF, LW):
    randRW = random.randint(0, len(RW) - 1)
    randCF = random.randint(0, len(CF) - 1)
    randLW = random.randint(0, len(LW) - 1)

    print("\t{}\t".format(LW[randLW]), end="")
    print("{}\t".format(CF[randCF]), end="")
    print("{}".format(RW[randRW]))

    LW1 = LW[randLW]
    CF1 = CF[randCF]
    RW1 = RW[randRW]

    for i in range(len(LW) - 1):
        if (LW[i] == LW1):
            LW.pop(i)

    for i in range(len(CF) - 1):
        if (CF[i] == CF1):
            CF.pop(i)

    for i in range(len(RW) - 1):
        if (RW[i] == RW1):
            RW.pop(i)

def generateTeam(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST):
    randFormation = random.randint(0, len(FORMATIONS) - 1)
    #randFormation = 0

    if (randFormation == 0):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST)
        LeftCAMRight(LM, RM, CAM)
        TwoCDM(CDM)
        ThreeInTheBack(CB)
        TheGK(GK)

    if (randFormation == 1):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST)
        FourInTheMiddle(CM, LM, RM)
        FourInTheBack(LB, CB, RB)
        TheGK(GK)

    if (randFormation == 2):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST)
        LeftCAMRight(LM, RM, CAM)
        TwoCDM(CDM)
        FourInTheBack(LB, CB, RB)
        TheGK(GK)
        

    if (randFormation == 3):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        FrontThree(RW, CF, LW)
        ThreeCMInTheMiddle(CM)
        FourInTheBack(LB, CB, RB)
        TheGK(GK)

    if (randFormation == 4):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST)
        OneCAM(CAM)
        FourInTheMiddle(CM, LM, RM)
        FourInTheBack(LB, CB, RB)
        TheGK(GK)

    if (randFormation == 5):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST)
        OneCAM(CAM)
        LeftRight(LM, RM)
        OneCDM(CDM)
        FourInTheBack(LB, CB, RB)
        TheGK(GK)

    if (randFormation == 6):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST)
        OneCAM(CAM)
        TwoCM(CM)
        OneCDM(CDM)
        FourInTheBack(LB, CB, RB)
        TheGK(GK)

    if (randFormation == 7):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST)
        OneCAM(CAM)
        TwoCDM(CDM)
        FiveInTheBack(LB, CB, RB)
        TheGK(GK)

    if (randFormation == 8):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        FrontThree(RW, CF, LW)
        TwoCM(CM)
        FiveInTheBack(LB, CB, RB)
        TheGK(GK)
        
    if (randFormation == 9):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        FrontThree(RW, CF, LW)
        FourInTheMiddle(CM, LM, RM)
        ThreeInTheBack(CB)
        TheGK(GK)

    if (randFormation == 10):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST)
        FourInTheMiddle(CM, LM, RM)
        OneCDM(CDM)
        FourInTheBack(LB, CB, RB)
        TheGK(GK)

    if (randFormation == 11):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST)
        TwoCAM(CAM)
        TwoCDM(CDM)
        FourInTheBack(LB, CB, RB)
        TheGK(GK)

    if (randFormation == 12):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST)
        TwoCAM(CAM)
        LeftRight(LM, RM)
        OneCDM(CDM)
        FourInTheBack(LB, CB, RB)
        TheGK(GK)

    if (randFormation == 13):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST)
        LeftRight(LM, RM)
        TwoCDM(CDM)
        FiveInTheBack(LB, CB, RB)
        TheGK(GK)

    if (randFormation == 14):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST)
        TwoCAM(CAM)
        LeftRight(LM, RM)
        TwoCDM(CDM)
        ThreeInTheBack(CB)
        TheGK(GK)

    if (randFormation == 15):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        FrontThree(RW, CF, LW)
        TwoCAM(CAM)
        TwoCDM(CDM)
        ThreeInTheBack(CB)
        TheGK(GK)

    if (randFormation == 16):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST)
        ThreeCMInTheMiddle(CM)
        TwoCDM(CDM)
        ThreeInTheBack(CB)
        TheGK(GK)

    if (randFormation == 17):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        OneST(ST)
        OneCAM(CAM)
        ThreeCMInTheMiddle(CM)
        FiveInTheBack(LB, CB, RB)
        TheGK(GK)

    randFormation = random.randint(0, len(FORMATIONS) - 1)

def main():
    inp = input
    while (inp != "q".upper()):
        GK = ["GK1", "GK2", "GK3", "GK4", "GK5", "GK6", "GK7", "GK8", "GK9", "GK10", "GK11", "GK12", "GK13", "GK14", "GK15", "GK16", "GK17", "GK18", "GK19", "GK20", "GK21", "GK22", "GK23", "GK24"]
        LB = ["LB1", "LB2", "LB3", "LB4", "LB5", "LB6", "LB7", "LB8", "LB9", "LB10", "LB11", "LB12", "LB13", "LB14", "LB15", "LB16", "LB17", "LB18", "LB19", "LB20", "LB21", "LB22", "LB23", "LB24"]
        CB = ["CB1", "CB2", "CB3", "CB4", "CB5", "CB6", "CB7", "CB8", "CB9", "CB10", "CB11", "CB12", "CB13", "CB14", "CB15", "CB16", "CB17", "CB18", "CB19", "CB20", "CB21", "CB22", "CB23", "CB24"]
        RB = ["RB1", "RB2", "RB3", "RB4", "RB5", "RB6", "RB7", "RB8", "RB9", "RB10", "RB11", "RB12", "RB13", "RB14", "RB15", "RB16", "RB17", "RB18", "RB19", "RB20", "RB21", "RB22", "RB23", "RB24"]
        CDM = ["CDM1", "CDM2", "CDM3", "CDM4", "CDM5", "CDM6", "CDM7", "CDM8", "CDM9", "CDM10", "CDM11", "CDM12", "CDM13", "CDM14", "CDM15", "CDM16", "CDM17", "CDM18", "CDM19", "CDM20", "CDM21", "CDM22", "CDM23", "CDM24"]
        CM = ["CM1", "CM2", "CM3", "CM4", "CM5", "CM6", "CM7", "CM8", "CM9", "CM10", "CM11", "CM12", "CM13", "CM14", "CM15", "CM16", "CM17", "CM18", "CM19", "CM20", "CM21", "CM22", "CM23", "CM24", ]
        CAM = ["CAM1", "CAM2", "CAM3", "CAM4", "CAM5", "CAM6", "CAM7", "CAM8", "CAM9", "CAM10", "CAM11", "CAM12", "CAM13", "CAM14", "CAM15", "CAM16", "CAM17", "CAM18", "CAM19", "CAM20", "CAM21", "CAM22", "CAM23", "CAM24"]
        LM = ["LM1", "LM2", "LM3", "LM4", "LM5", "LM6", "LM7", "LM8", "LM9", "LM10", "LM11", "LM12", "LM13", "LM14", "LM15", "LM16", "LM17", "LM18", "LM19", "LM20", "LM21", "LM22", "LM23", "LM24"]
        RM = ["RM1", "RM2", "RM3", "RM4", "RM5", "RM6", "RM7", "RM8", "RM9", "RM10", "RM11", "RM12", "RM13", "RM14", "RM15", "RM16", "RM17", "RM18", "RM19", "RM20", "RM21", "RM22", "RM23", "RM24"]
        RW = ["RW1", "RW2", "RW3", "RW4", "RW5", "RW6", "RW7", "RW8", "RW9", "RW10", "RW11", "RW12", "RW13", "RW14", "RW15", "RW16", "RW17", "RW18", "RW19", "RW20", "RW21", "RW22", "RW23", "RW24"]
        CF = ["CF1", "CF2", "CF3", "CF4", "CF5", "CF6", "CF7", "CF8", "CF9", "CF10", "CF11", "CF12", "CF13", "CF14", "CF15", "CF16", "CF17", "CF18", "CF19", "CF20", "CF21", "CF22", "CF23", "CF24"]
        LW = ["LW1", "LW2", "LW3", "LW4", "LW5", "LW6", "LW7", "LW8", "LW9", "LW10", "LW11", "LW12", "LW13", "LW14", "LW15", "LW16", "LW17", "LW18", "LW19", "LW20", "LW21", "LW22", "LW23", "LW24"]
        ST = ["ST1", "ST2", "ST3", "ST4", "ST5", "ST6", "ST7", "ST8", "ST9", "ST10", "ST11", "ST12", "ST13", "ST14", "ST15", "ST16", "ST17", "ST18", "ST19", "ST20", "ST21", "ST22", "ST23", "ST24"]
        print("------------------------------")
        print("1. Generate 1 team\n2. Generate 2 teams\nQ. Quit")
        print("------------------------------")
        inp = str(input("INPUT: ").upper())
        if (inp == "1"):
            print("------------------------------")
            generateTeam(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST)
        elif (inp == "2"):
            print("------------------------------")
            print("Team 1:")
            generateTeam(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST)
            print("\n------------------------------")
            print("\nTeam 2:")
            generateTeam(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST)
        elif (inp == "q".upper()):
            break
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
