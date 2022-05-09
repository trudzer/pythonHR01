import random

FORMATIONS = ["3-5-2", "4-4-2", "4-2-3-1", "4-3-3", "4-4-1-1", "4-1-2-1-2", "4-1-2-1-2", "5-2-1-2", "5-2-3", "3-4-3", "4-1-4-1", "4-2-2-2", "4-1-2-2-1", "5-2-2-1", "3-2-2-2-1", "3-2-1-3",  "3-2-3-2", "5-3-1-1", "3-2-3-2"]

def TheGK(GK):
    randGK = random.randint(0, len(GK) - 1)

    print("\n{:<30}{}".format("", "GK"))
    print("{:<30}{}".format("", GK[randGK]))

    GK1 = GK[randGK]

    for i in range(len(GK) - 1):
        if (GK[i] == GK1):
            GK.pop(i)

def FourInTheBack(LB, CB, RB):
    randLB = random.randint(0, len(LB) - 1)
    randCB = random.randint(0, len(CB) - 1)
    randCB2 = random.randint(0, len(CB) - 1)
    randRB = random.randint(0, len(RB) - 1)

    print("\n{:<20}{:<20}{:<20}{}".format("LB", "CB", "CB", "RB"))
    print("{:<20}".format(LB[randLB]), end="")
    print("{:<20}".format(CB[randCB]),end="")
    while (randCB2 == randCB):
        randCB2 = random.randint(0, len(CB) - 1)
        if (randCB2 != randCB):
            break
    print("{:<20}".format(CB[randCB2]), end="")
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

    print("\n{:<60}{}".format("LWB","RWB"))
    print("{:<60}{}".format(LB[randLB], RB[randRB]))
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

    print("\n{:<10}{:<40}{}".format("","CDM","CDM"))
    print("{:<10}{:<40}".format("",CDM[randCDM]), end="")
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

    print("\n{:<30}{}".format("","CDM"))
    print("{:<30}{}".format("",CDM[randCDM]))

    CDM1 = CDM[randCDM]

    for i in range(len(CDM) - 1):
        if (CDM[i] == CDM1):
            CDM.pop(i)

def FourInTheMiddle(CM, LM, RM):
    randCM = random.randint(0, len(CM) - 1)
    randCM2 = random.randint(0, len(CM) - 1)
    randLM = random.randint(0, len(LM) - 1)
    randRM = random.randint(0, len(RM) - 1)

    print("\n{:<20}{:<20}{:<20}{}".format("LM","CM","CM","RM"))
    print("{:<20}".format(LM[randLM]), end="")
    print("{:<20}".format(CM[randCM]), end="")
    while (randCM2 == randCM):
        randCM2 = random.randint(0, len(CM) - 1)
        if (randCM2 != randCM):
            break
    print("{:<20}".format(CM[randCM2]), end="")
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

    print("\n{:<60}{}".format("LM","RM"))
    print("{:<60}".format(LM[randLM]), end="")
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

    print("\n{:<20}{:<20}{:<20}".format("","CM","CM"))
    print("{:<20}{:<20}".format("",CM[randCM]), end="")
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

    print("\n{:<30}{}".format("","CAM"))
    print("{:<30}{}".format("",CAM[randCAM]))

    CAM1 = CAM[randCAM]

    for i in range(len(CAM) - 1):
        if (CAM[i] == CAM1):
            CAM.pop(i)

def TwoCAM(CAM):
    randCAM = random.randint(0, len(CAM) - 1)
    randCAM2 = random.randint(0, len(CAM) - 1)

    print("\n{:<10}{:<40}{}".format("","CAM","CAM"))
    print("{:<10}{:<40}".format("",CAM[randCAM]), end="")
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

    print("\n{:<30}{:<30}{}".format("LM","CAM","RM"))
    print("{:<30}".format(LM[randLM]), end="")
    print("{:<30}".format(CAM[randCAM]), end="")
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

    print("\n{:<30}{}".format("","CF"))
    print("{:<30}{}".format("",CF[randCF]))

    CF1 = CF[randCF]

    for i in range(len(CF) - 1):
        if (CF[i] == CF1):
            CF.pop(i)

def OneST(ST):
    randST = random.randint(0, len(ST) - 1)

    print("{:<30}{}".format("","ST"))
    print("{:<30}{}".format("",ST[randST]))

    ST1 = ST[randST]

    for i in range(len(ST) - 1):
        if (ST[i] == ST1):
            ST.pop(i)

def TwoST(ST):
    randST = random.randint(0, len(ST) - 1)
    randST2 = random.randint(0, len(ST) - 1)

    print("{:<20}{:<20}{}".format("","ST","ST"))
    print("{:<20}{:<20}".format("",ST[randST]), end="")
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

    print("{:<10}{:<20}{:<20}{}".format("","LW","CF","RW"))
    print("{:<10}{:<20}".format("",LW[randLW]), end="")
    print("{:<20}".format(CF[randCF]), end="")
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

    if (randFormation == 18):
        print("\t\t{}\n".format(FORMATIONS[randFormation]))
        TwoST(ST)
        LeftCAMRight(LM, RM, CAM)
        TwoCDM(CDM)
        ThreeInTheBack(CB)
        TheGK(GK)

    randFormation = random.randint(0, len(FORMATIONS) - 1)

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

def main():
    inp = input
    while (inp != "q".upper()):
        GK = ["Oblak", "Alisson", "Ter Stegen", "Courtois", "Neuer", "Ederson", "De Gea", "Szczesny", "Handanovic", "Leno", "Gulácsi", "Lloris", "Donnarumma", "Navas", "Sommer", "Onana", "Meret", "Casteels", "Rui Patrício", "Fabianski", "Strakosha", "Musso", "Pickford", "Kepa"]
        LB = ["Robertson", "Guerreiro", "Jordi Alba", "Hernandez", "Alex Sandro", "Tagliafico", "Davies", "Renan Lodi", "Hernández", "Chilwell", "F.Mendy", "Alex Telles", "Kolarov", "Marcelo", "Tierney", "Acuna", "Álex Grimaldo", "José Gayà", "B.Mendy", "Digne", "Juan Bernat", "Reguilón", "Fabra", "Spinazolla"]
        CB = ["Van Dijk", "Sergio Ramos", "Varane", "Koulibaly", "Alaba", "Piqué", "Süle", "De Ligt", "Skriniar", "Lenglet", "Giménez", "Laporte", "De Vrij", "Thiago Silva", "Chiellini", "Maguire", "Umtiti", "Acerbi", "Manolas", "Alderweireld", "Bonucci", "Rúben Dias", "Koundé", "Sánchez", "Kimpembe", "Ginter", "Romagnoli", "Felipe", "Vertonghen", "Benatia", "Pau Torres", "Éder Militao", "Djené", "Rüdiger", "Joe Gomez", "Diego Carlos", "Savic", "Boateng", "David Luiz"]
        RB = ["Alexander-Arnold", "Carvajal", "Ricardo Pereira", "Jesus Navas", "Wan-Bissaka", "Hakimi", "Nélson Semedo", "Pavard", "Trippier", "Sergi Roberto", "Kyle Walker", "Cuadrado", "Azpilicueta", "Di Lorenzo", "Bellerín", "Joao Cancelo", "Florenzi", "Meunier", "Mário Fernandes", "Youcef Atal", "Dumfries", "Danilo", "Lars Bender", "Dest"]
        CDM = ["Kimmich", "Casemiro", "Sergio Busquets", "Marquinhos", "Fabinho", "Pjanic", "Rodri", "Partey", "Jorginho", "Witsel", "Fernandinho", "Ndidi", "Allan", "Javi Martínez", "Zakaria", "Torreira", "Emre Can", "Xhaka", "Lucas Leiva", "Barrios", "Paredes", "Matic", "Delaney", "Gabi"]
        CM = ["Kanté", "Thiago", "Kroos", "De Jong", "Saúl", "Verratti", "Milinkovic-Savic", "Luis Alberto", "Pogba", "Koke", "Dani Parejo", "Modric", "Iniesta", "Valverde", "Arthur", "Sabitzer", "Goretzka", "Brozovic", "Gündogan", "Nainggolan", "Henderson", "Rakitic", "Wijnaldum", "Ndombèlé", "Fabián Ruiz", "Bentancur", "De Paul", "Sergio Canales", "Pellegrini", "Dani Ceballos", "Rúben Neves", "Barella", "Tolisso", "Tielemans", "Kovacic", "Gueye", "Aránguiz", "Ramsey", "Vidal", "Matuidi", "Santi Cazorla", "Joao Moutinho", "Paulinho"]
        CAM = ["De Bruyne", "Bruno Fernandes", "Havertz", "Marcos Llorente", "Coutinho", "Papu Gómez", "Isco", "Eriksen", "David Silva", "Odegaard", "Calhanoglu", "Brandt", "Fekir", "Maddison", "Van De Beek", "Zielinski", "Draxler", "Özil", "Oscar", "Mount", "Zaniolo", "Forsberg", "De Arrascaeta", "Mkhitaryan"]
        LM = ["Heung-Min Son", "Kostic", "Carrasco", "Perisic", "Felipe Anderson", "Thomas Lemar", "Gosens", "Bergwijn", "El Shaarawy", "Vitolo", "Saint-Maximin", "Lulic", "Bamba", "Claesson", "Deulofeu", "Cornet", "Fraser", "Jony", "Bouanga", "Pablo FFornals", "Barnes", "Saka", "Szoboszlai", "Redmond"]
        RM = ["Pizzi", "Corona", "Lucas Moura", "Correa", "Visca", "Everton Ribeiro", "Caligiuri", "Joaquín", "Candreva", "Ayoze Pérez", "Hateboer", "Lazzari", "Lamela"]
        RW = ["Messi", "Salah", "Bernardo Silva", "Gnabry", "Di María", "Sancho", "Mahrez", "Ziyech", "Pépé", "Thauvin", "Ocampos", "Pablo Sarabia", "James Rodríguez", "Douglas Costa", "Willian", "Bale", "Chiesa", "Asensio", "Portu", "Coman", "Berghuis", "José Callejón", "Ferran Torres", "Malcom"]
        CF = ["Dybala", "Müller", "Ilicic", "Lobato", "Correa", "Joao Félix", "Tevez", "Kruse", "Joao Pedro", "Corte Real", "Giovinco", "Quaison", "Marega", "Waldschmidt", "Moniz", "Vietto", "Philipp", "Jonathan David", "Zárate"]
        LW = ["Dembéle", "Oyarzabal", "Insigne", "Richarlison", "Payet", "Pavón", "Grealish", "Rebic", "Ansu Fati", "Lozano", "Pulisic", "Diogo Jota", "Goncalo Guedes", "Bruno Henrique", "Thorgan Hazard", "Promes", "Éverton", "Zaha", "Taison", "Vinícius Júnior", "Rashica", "Perotti", "Baldé", "Diaby"]
        ST = ["Lewandowski", "Mbappé", "Kane", "Agüero", "Aubameyang", "Suárez", "Benzema", "Roberto Firmino", "Immobile", "Håland", "Werner", "Vardy", "Icardi", "Lukaku", "Cavani", "Martínez", "Gabriel Jesus", "Zapata", "Jiménez", "Depay", "Iago Aspas", "Ben Yedder", "Mertens", "Dzeko", "Higuaín", "Ibrahimovic", "Weghorst", "Belotti", "Morata", "Lacazette", "Mandzukic", "Jovic", "André Silva", "Danny Ings", "Moussa Dembéle", "Volland", "Milik", "Gerard Moreno", "Martial", "Muriel", "Rodrigo", "Tadic", "Dzyuba", "Falcao", "Arnautovic", "Calbert-Lewin", "Abraham", "Gómez", "Wilson", "Williams", "Alario", "Gabriel Barbosa", "Benedetto", "Paco Alcácer", "Alex Teixeira", "Caputo", "Giroud", "Diego Costa", "Sánchez", "Quagliarella", "Osimhen", "Schick", "Embolo", "King", "Lasagna"]
        print("------------------------------")
        #longName(GK, LB, CB, RB, CDM, CM, CAM, LM, RM, RW, CF, LW, ST)
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
