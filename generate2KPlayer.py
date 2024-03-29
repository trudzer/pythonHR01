import math
import random

MIN = 40
TEMPMIN = 45
MAX = 50

BRONZE = 80
SILVER = 85
GOLD = 90
HOF = 95

def calcCMtoInch(heightCM):
    feet = math.floor(heightCM / 30.48)
    inches = round((heightCM % 30.48) / 2.54)
    if inches == 12:
        feet += 1
        inches = 0
    newHeight = "{}'{}\"".format(feet, inches)
    return newHeight

def generatePlayer(ToP, POS, OSP, ISP, DP, AP, PP, RP):
    PG = 0 
    SG = 0
    SF = 0 
    PF = 0
    C = 0
    if POS == "PG":
        PG = 20
    if POS == "SG":
        SG = 20
    if POS == "SF":
        SF = 20
    if POS == "PF":
        PF = 20
    if POS == "C":
        C = 20

    if ToP == "R":
        MIN = 35
        TEMPMIN = 40
        MAX = 45
    if ToP == "Y":
        MIN = 40
        TEMPMIN = 45
        MAX = 50
    if ToP == "AS":
        MIN = 45
        TEMPMIN = 50
        MAX = 55
    if ToP == "SS":
        MIN = 50
        TEMPMIN = 55
        MAX = 55

    if POS == "C":
        height = random.randint(206, 221)
        weight = random.randint(88, 113)
    if POS == "PF":
        height = random.randint(198, 213)
        weight = random.randint(80, 110)
    if POS == "SF":
        height = random.randint(193, 208)
        weight = random.randint(71, 103)
    if POS == "SG":
        height = random.randint(188, 206)
        weight = random.randint(66, 95)
    if POS == "PG":
        height = random.randint(183, 201)
        weight = random.randint(62, 88)

    #Athleticism
    speed = min(math.ceil(random.randint(MIN, MAX + round(PG / 4) + round(SG / 4)) * AP) + (PG + SG + SF + (round(PF / 1.8)) + (round(C / 3))), 99)
    acceleration = min(math.ceil(random.randint(speed - 5, min(speed + 10, 99))), 99)
    if POS == "SF":
        if height <= 201:
            newSpeed = speed + 5
            newAcceleration = acceleration + 5
            speed = min(99, newSpeed)
            acceleration = min(99, newAcceleration)
    if POS == "PF":
            if height <= 206:
                newSpeed = speed + 10
                newAcceleration = acceleration + 10
                speed = min(99, newSpeed)
                acceleration = min(99, newAcceleration)
    if POS == "C":
            if height <= 210:
                if ToP == "R":
                    newSpeed = speed + 15
                    newAcceleration = acceleration + 15
    strength = min(math.ceil(random.randint(MIN, MAX) * AP) + (PF + C), 99)
    vertical = min(math.ceil(random.randint(MIN, MAX + round(PG / 4) + round(SG / 4) + round(SF / 4) + round(PF / 4)) * AP) + (PG + SG + SF + PF), 99)
    stamina = min(math.ceil(random.randint(MAX + round(PG / 4) + round(SG / 4), MAX + round(PG / 4) + round(SG / 4) + 5) * AP) + (PG + SG + SF + PF + C), 99)
    hustle = min(math.ceil(random.randint(MIN, MAX) * AP) + (PG + SG + SF), 99)
    overallDurability = min(math.ceil(random.randint(TEMPMIN, MAX) * AP) + (PG + SG + SF + PF + C), 99)

    #Outside Scoring
    closeShot = min(math.ceil(random.randint(MIN, MAX) * OSP) + (PG + SG + SF + PF + C), 99)
    midRangeShot = min(math.ceil(random.randint(MIN, MAX) * OSP) + (PG + SG + SF + PF + C), 99)
    threePointShot = min(math.ceil(random.randint(MIN, MAX) * OSP) + (PG + SG + SF + PF + C), 99)
    freeThrow = min(math.ceil(random.randint(round((closeShot / 4) + (midRangeShot / 4)), MAX) * OSP) + (PG + SG + SF + PF + C), 99)
    shotIQ = min(random.randint(max(closeShot, midRangeShot, threePointShot) - 5, max(closeShot, midRangeShot, threePointShot) + 5), 99)
    offensiveConsistency = min(random.randint((round(shotIQ / 2) + round(stamina / 2)) - 5, (round(shotIQ / 2) + round(stamina / 2))), 99)
    #Inside Scoring
    layup = min(math.ceil(random.randint(MIN, MAX) * ISP) + (PG + SG + SF + PF + C), 99)
    if POS == "PG":
        tempCloseShot = min(closeShot, layup)
        tempLayup = max(closeShot, layup)
        layup = tempLayup
        closeShot = tempCloseShot
        values = [closeShot, midRangeShot, threePointShot]
        values = sorted(values)
        values.reverse()
        threePointShot = values[0]
        closeShot = values[1]
        midRangeShot = values[2]
        offensiveConsistency = min(random.randint((round(shotIQ / 2) + round(stamina / 2)) - 5, (round(shotIQ / 2) + round(stamina / 2)) + 5), 99)
    if POS == "SG":
        values = [closeShot, midRangeShot, threePointShot]
        values = sorted(values)
        values.reverse()
        threePointShot = values[0]
        midRangeShot = values[1]
        closeShot = values[2]
        freeThrow = min(math.ceil(random.randint(round((closeShot / 4) + (midRangeShot / 4)), MAX) * OSP) + (PG + SG + SF + PF + C), 99)
        shotIQ = min(random.randint(max(closeShot, midRangeShot, threePointShot) - 5, max(closeShot, midRangeShot, threePointShot) + 5), 99)
        offensiveConsistency = min(random.randint((round(shotIQ / 2) + round(stamina / 2)) - 5, (round(shotIQ / 2) + round(stamina / 2)) + 5), 99)
    if POS == "C" or POS == "PF":
        values = [closeShot, midRangeShot, threePointShot]
        values = sorted(values)
        values.reverse()
        closeShot = values[0]
        threePointShot = values[1]
        midRangeShot = values[2]
        offensiveConsistency = min(random.randint(shotIQ - 5, shotIQ + 5), 99)
    standingDunk = min(math.ceil(random.randint(MIN, MAX) * ISP) + (SF + PF + C), 99)
    drivingDunk = min(math.ceil(random.randint(MIN, MAX) * ISP) + (SF + PF + C), 99)
    postHook = min(math.ceil(random.randint(MIN, MAX) * ISP) + (SF + PF + C), 99)
    postFade = min(math.ceil(random.randint(MIN, MAX) * ISP) + (SG + SF + PF + C), 99)
    postControl = min(math.ceil(random.randint(MIN, MAX) * ISP) + (SG + SF + PF + C), 99)
    drawFoul = min(math.ceil(random.randint(MIN, MAX) * ISP) + (PG + SG + SF + PF + C), 99)
    hands = min(math.ceil(random.randint(TEMPMIN + round(PF / 4) + round(C / 4), MAX + round(PF / 4) + round(C / 4)) * ISP) + (PG + SG + SF + PF + C), 99)
    if POS == "PF" or POS == "C":
        tempCloseShot = max(closeShot, layup)
        tempLayup = min(closeShot, layup)
        layup = tempLayup
        closeShot = tempCloseShot
    if POS == "PG":
        if height >= 194:
            newDrivingDunk = drivingDunk + 20
            newStandingDunk = standingDunk + 20
            standingDunk = min(99, newStandingDunk)
            drivingDunk = min(99, newDrivingDunk)
    if POS == "SG":
            if height >= 197:
                newDrivingDunk = drivingDunk + 20
                newStandingDunk = standingDunk + 20
                standingDunk = min(99, newStandingDunk)
                drivingDunk = min(99, newDrivingDunk)
    if POS == "PG" or POS == "SG" or POS == "SF":
        tempStandingDunk = min(standingDunk, drivingDunk)
        tempDrivingDunk = max(standingDunk, drivingDunk)
        tempPostHook = min(postHook, postFade)
        tempPostFade = max(postHook, postFade)
        drivingDunk = tempDrivingDunk
        standingDunk = tempStandingDunk
        postHook = tempPostHook
        postFade = tempPostFade
    if POS == "C" or POS == "PF":
        tempStandingDunk = max(standingDunk, drivingDunk)
        tempDrivingDunk = min(standingDunk, drivingDunk)
        tempPostHook = max(postHook, postFade)
        tempPostFade = min(postHook, postFade)
        drivingDunk = tempDrivingDunk
        standingDunk = tempStandingDunk
        postHook = tempPostHook
        postFade = tempPostFade
    freeThrow = min(math.ceil(random.randint(round((closeShot / 4) + (midRangeShot / 4)), MAX) * OSP) + (PG + SG + SF + PF + C), 99)
    shotIQ = min(random.randint(max(closeShot, midRangeShot, threePointShot) - 5, max(closeShot, midRangeShot, threePointShot) + 5), 99)
    
    #Playmaking
    ballHandle = min(math.ceil(random.randint(MIN + round(PG / 4) + round(SG / 4), MAX  + round(PG / 4) + round(SG / 4)) * PP) + (PG + SG + SF + (round(PF / 1.5))), 99)
    speedWithBall = min(math.ceil((speed + acceleration + ballHandle) / 3), 99)
    if POS == "SF":
        if height <= 201:
            newSpeedWithBall = speedWithBall + 5
            speedWithBall = min(99, newSpeedWithBall)
    if POS == "PF":
            if height <= 206:
                newSpeedWithBall = speedWithBall + 10
                speedWithBall = min(99, newSpeedWithBall)
    if POS == "C":
            if height <= 210:
                if ToP == "R":
                    newSpeedWithBall = speedWithBall + 15
                    speedWithBall = min(99, newSpeedWithBall)
    passVision = min(math.ceil(random.randint(MIN, MAX) * PP) + (PG + round(SG / 2) + SF + round(PF / 2) + C), 99)
    passIQ = min(math.ceil(random.randint(round(MIN / 2) + round(passVision / 4), round(MAX / 2) + round(passVision / 4)) * PP) + (PG + round(SG / 2) + SF + round(PF / 2) + C), 99)
    passAccuracy = min(math.ceil(random.randint(round(passIQ / 4) + round(passVision / 4), MAX) * PP) + (PG + round(SG / 2) + SF + C), 99)
    
    #Defending
    interiorDefense = min(math.ceil(random.randint(MIN, MAX) * DP) + (PF + C), 99)
    perimeterDefense = min(math.ceil(random.randint(MIN, MAX) * DP) + (PG + SG + SF), 99)
    steal = min(random.randint(perimeterDefense - 5, perimeterDefense + 10), 99)
    block = min(random.randint(interiorDefense - 5, interiorDefense + 10), 99)
    if POS == "PG" or POS == "SG" or POS == "SF":
        tempPerimeterDefense = max(perimeterDefense, interiorDefense)
        tempInteriorDefense = min(perimeterDefense, interiorDefense)
        tempSteal = max(steal, block)
        tempBlock = min(steal, block)
        steal = tempSteal
        block = tempBlock
        interiorDefense = tempInteriorDefense
        perimeterDefense = tempPerimeterDefense
    if POS == "PF" or POS == "C":
        tempPerimeterDefense = min(perimeterDefense, interiorDefense)
        tempInteriorDefense = max(perimeterDefense, interiorDefense)
        tempSteal = min(steal, block)
        tempBlock = max(steal, block)
        steal = tempSteal
        block = tempBlock
        interiorDefense = tempInteriorDefense
        perimeterDefense = tempPerimeterDefense
    lateralQuickness = min(random.randint((round(acceleration / 2) + round(speed / 2)) - 5, (round(acceleration / 2) + round(speed / 2))), 99)
    if POS == "SF":
        if height <= 201:
            newLateralQuickness = lateralQuickness + 5
            lateralQuickness = min(99, newLateralQuickness)
    if POS == "PF":
            if height <= 206:
                newLateralQuickness = lateralQuickness + 10
                lateralQuickness = min(99, newLateralQuickness)
    if POS == "C":
            if height <= 210:
                if ToP == "R":
                    newLateralQuickness = lateralQuickness + 15
                    lateralQuickness = min(99, newLateralQuickness)
    helpDefenseIQ = min(math.ceil(random.randint(MIN, MAX) * DP) + (PG + SG + SF + PF + C), 99)
    passPerception = min(random.randint(round(passIQ / 2) + round(helpDefenseIQ / 2) - 5, round(passIQ / 2) + round(helpDefenseIQ / 2)), 99)
    defensiveConsistency = min(random.randint((round(helpDefenseIQ / 2) + round(stamina / 2)) - 5, (round(helpDefenseIQ / 2) + round(stamina / 2))), 99)
    
    #Rebounding
    defensiveRebound = min(math.ceil(random.randint(MIN, MAX) * RP) + (SF + PF + C), 99)
    offensiveRebound = min(math.ceil(random.randint(round(defensiveRebound / 2), MAX) * RP) + (SF + PF + C), 99)
    if POS == "PG":
        if height >= 194:
            newOffensiveRebound = offensiveRebound + 20
            newDefensiveRebound = defensiveRebound + 20
            defensiveRebound = min(99, newDefensiveRebound)
            offensiveRebound = min(99, newOffensiveRebound)

    if POS == "SG":
            if height >= 197:
                newOffensiveRebound = offensiveRebound + 20
                newDefensiveRebound = defensiveRebound + 20
                defensiveRebound = min(99, newDefensiveRebound)
                offensiveRebound = min(99, newOffensiveRebound)

    if POS == "PG" or POS == "SG" or POS == "C":
        tempOffensiveRebound = min(offensiveRebound, defensiveRebound)
        tempDefensiveRebound = max(offensiveRebound, defensiveRebound)
        defensiveRebound = tempDefensiveRebound
        offensiveRebound = tempOffensiveRebound

    outsideScoring = math.floor((closeShot 
                                + midRangeShot 
                                + threePointShot 
                                + freeThrow 
                                + shotIQ
                                + offensiveConsistency) / 6)
    
    insideScoring = math.floor((layup
                                + standingDunk
                                + drivingDunk
                                + postHook
                                + postFade
                                + postControl
                                + drawFoul
                                + hands) / 8)
    
    athleticism = math.floor((speed
                            + acceleration
                            + strength
                            + vertical
                            + stamina
                            + hustle
                            + overallDurability) / 7)
    
    playmaking = math.floor((passAccuracy
                            + ballHandle
                            + speedWithBall
                            + passIQ
                            + passVision) / 5)
    
    defending = math.floor((interiorDefense
                            + perimeterDefense
                            + steal
                            + block
                            + lateralQuickness
                            + helpDefenseIQ
                            + passPerception
                            + defensiveConsistency) / 8)
    
    rebounding = math.floor((offensiveRebound
                            + defensiveRebound) / 2)
    #Other
    wingspan = random.randint(height - 4, height + 25 - round(PG / 3) + round(SG / 3))
    intangibles = random.randint(70, 99)
    potential = random.randint(90, 99)
    workEthic = random.randint(1,3)
    number = random.randint(0, 99)
    handness = random.randint(0, 1)
    
    playerStats = (
        f"\n"
        f"{outsideScoring} Outside Scoring {insideScoring:>15} Inside Scoring\n"
        f"--------------------\t\t--------------------\n"
        f"{closeShot} Close Shot {layup:>20} Layup\n"
        f"{midRangeShot} Mid-Range Shot {standingDunk:>16} Standing Dunk\n"
        f"{threePointShot} Three-Point Shot {drivingDunk:>14} Driving Dunk\n"
        f"{freeThrow} Free Throw {postHook:>20} Post Hook\n"
        f"{shotIQ} Shot IQ {postFade:>23} Post Fade\n"
        f"{offensiveConsistency} Offensive Consistency {postControl:>9} Post Control\n"
        f"{drawFoul:>34} Draw Foul\n"
        f"{hands:>34} Hands\n"
        f"\n"
        f"{defending} Defending {athleticism:>21} Athleticism\n"
        f"--------------------\t\t--------------------\n"
        f"{interiorDefense} Interior Defense {speed:>14} Speed\n"
        f"{perimeterDefense} Perimeter Defense {acceleration:>13} Acceleration\n"
        f"{steal} Steal {strength:>25} Strength\n"
        f"{block} Block {vertical:>25} Vertical\n"
        f"{lateralQuickness} Lateral Quickness {stamina:>13} Stamina\n"
        f"{helpDefenseIQ} Help Defense IQ {hustle:>15} Hustle\n"
        f"{passPerception} Pass Perception {overallDurability:>15} Overall Durability\n"
        f"{defensiveConsistency} Defensive Consistency\n"
        f"\n"
        f"{playmaking} Playmaking {rebounding:>20} Rebounding\n"
        f"--------------------\t\t--------------------\n"
        f"{passAccuracy} Pass Accuracy {offensiveRebound:>17} Offensive Rebound\n"
        f"{ballHandle} Ball Handle {defensiveRebound:>19} Defensive Rebound\n"
        f"{speedWithBall} Speed with Ball\n"
        f"{passIQ} Pass IQ\n"
        f"{passVision} Pass Vision\n"
        f"\n"
        f"--------------------\t\t--------------------\n"
        f"{intangibles} Intangibles {height:>20} cm ({calcCMtoInch(height)} ft)\n"
        f"{potential} Potential {weight:>22} KG ({round(weight * 2.20462)} lbs)\n"
        f"{'Left Hand ' if handness == 0 else 'Right Hand'} {wingspan:>24} cm ({calcCMtoInch(wingspan)}) ft\n"
        f"Number {number}\n"
        f"\n"
    )

    badges = [
        f"{'Acrobat: Bronze' if layup >= BRONZE and layup < SILVER else ''}",
        f"{'Acrobat: Silver' if layup >= SILVER and layup < GOLD else ''}",
        f"{'Acrobat: Gold' if layup >= GOLD and layup < HOF else ''}",
        f"{'Acrobat: Hall of Fame' if layup >= HOF else ''}",
    
        f"{'Aerial Wizard: Bronze' if max(drivingDunk, standingDunk) >= BRONZE and max(drivingDunk, standingDunk) < SILVER else ''}",
        f"{'Aerial Wizard: Silver' if max(drivingDunk, standingDunk) >= SILVER and max(drivingDunk, standingDunk) < GOLD else ''}",
        f"{'Aerial Wizard: Gold' if max(drivingDunk, standingDunk) >= GOLD and max(drivingDunk, standingDunk) < HOF else ''}",
        f"{'Aerial Wizard: Hall of Fame' if max(drivingDunk, standingDunk) >= HOF else ''}",
        
        f"{'Backdown Punisher: Bronze' if postControl >= BRONZE and postControl < SILVER and strength >= BRONZE else ''}",
        f"{'Backdown Punisher: Silver' if postControl >= SILVER and postControl < GOLD and strength >= SILVER else ''}",
        f"{'Backdown Punisher: Gold' if postControl >= GOLD and postControl < HOF and strength >= GOLD else ''}",
        f"{'Backdown Punisher: Hall of Fame' if postControl >= HOF and strength >= HOF else ''}",
        
        f"{'Dream Shake: Bronze' if postControl >= BRONZE and postControl < SILVER and closeShot >= BRONZE else ''}",
        f"{'Dream Shake: Silver' if postControl >= SILVER and postControl < GOLD and closeShot >= SILVER else ''}",
        f"{'Dream Shake: Gold' if postControl >= GOLD and postControl < HOF and closeShot >= GOLD else ''}",
        f"{'Dream Shake: Hall of Fame' if postControl >= HOF and closeShot >= HOF else ''}",
                
        f"{'Dropstepper: Bronze' if postControl >= BRONZE and postControl < SILVER and strength >= BRONZE else ''}",
        f"{'Dropstepper: Silver' if postControl >= SILVER and postControl < GOLD and strength >= SILVER else ''}",
        f"{'Dropstepper: Gold' if postControl >= GOLD and postControl < HOF and strength >= GOLD else ''}",
        f"{'Dropstepper: Hall of Fame' if postControl >= HOF and strength >= HOF else ''}",
    
        f"{'Fast Twitch: Bronze' if max(standingDunk, closeShot) >= BRONZE and max(standingDunk, closeShot) < SILVER else ''}",
        f"{'Fast Twitch: Silver' if max(standingDunk, closeShot) >= SILVER and max(standingDunk, closeShot) < GOLD else ''}",
        f"{'Fast Twitch: Gold' if max(standingDunk, closeShot) >= GOLD and max(standingDunk, closeShot) < HOF else ''}",
        f"{'Fast Twitch: Hall of Fame' if max(standingDunk, closeShot) >= HOF else ''}",
        
        f"{'Fearless Finisher: Bronze' if max(drivingDunk, layup) >= BRONZE and max(drivingDunk, layup) < SILVER else ''}",
        f"{'Fearless Finisher: Silver' if max(drivingDunk, layup) >= SILVER and max(drivingDunk, layup) < GOLD else ''}",
        f"{'Fearless Finisher: Gold' if max(drivingDunk, layup) >= GOLD and max(drivingDunk, layup) < HOF else ''}",
        f"{'Fearless Finisher: Hall of Fame' if max(drivingDunk, layup) >= HOF else ''}",
        
        f"{'Giant Slayer: Bronze' if max(layup, drivingDunk) >= BRONZE and max(layup, drivingDunk) < SILVER and height <= 196 else ''}",
        f"{'Giant Slayer: Silver' if max(layup, drivingDunk) >= SILVER and max(layup, drivingDunk) < GOLD and height <= 196 else ''}",
        f"{'Giant Slayer: Gold' if max(layup, drivingDunk) >= GOLD and max(layup, drivingDunk) < HOF and height <= 196 else ''}",
        f"{'Giant Slayer: Hall of Fame' if max(layup, drivingDunk) >= HOF and height <= 196 else ''}",
        
        f"{'Masher: Bronze' if max(standingDunk, closeShot) >= BRONZE and max(standingDunk, closeShot) < SILVER else ''}",
        f"{'Masher: Silver' if max(standingDunk, closeShot) >= SILVER and max(standingDunk, closeShot) < GOLD else ''}",
        f"{'Masher: Gold' if max(standingDunk, closeShot) >= GOLD and max(standingDunk, closeShot) < HOF else ''}",
        f"{'Masher: Hall of Fame' if max(standingDunk, closeShot) >= HOF else ''}",

        f"{'Post Spin Technician: Bronze' if postControl >= BRONZE and postControl < SILVER and hands >= BRONZE else ''}",
        f"{'Post Spin Technician: Silver' if postControl >= SILVER and postControl < GOLD and hands >= SILVER else ''}",
        f"{'Post Spin Technician: Gold' if postControl >= GOLD and postControl < HOF and hands >= GOLD else ''}",
        f"{'Post Spin Technician: Hall of Fame' if postControl >= HOF and hands >= HOF else ''}",
  
        f"{'Posterizer: Bronze' if max(standingDunk, drivingDunk) >= BRONZE and max(standingDunk, drivingDunk) < SILVER else ''}",
        f"{'Posterizer: Silver' if max(standingDunk, drivingDunk) >= SILVER and max(standingDunk, drivingDunk) < GOLD else ''}",
        f"{'Posterizer: Gold' if max(standingDunk, drivingDunk) >= GOLD and max(standingDunk, drivingDunk) < HOF else ''}",
        f"{'Posterizer: Hall of Fame' if max(standingDunk, drivingDunk) >= HOF else ''}",
        
        f"{'Pro Touch: Bronze' if max(layup, closeShot) >= BRONZE and max(layup, closeShot) < SILVER else ''}",
        f"{'Pro Touch: Silver' if max(layup, closeShot) >= SILVER and max(layup, closeShot) < GOLD else ''}",
        f"{'Pro Touch: Gold' if max(layup, closeShot) >= GOLD and max(layup, closeShot) < HOF else ''}",
        f"{'Pro Touch: Hall of Fame' if max(layup, closeShot) >= HOF else ''}",
 
        f"{'Rise Up: Bronze' if standingDunk >= BRONZE and standingDunk < SILVER else ''}",
        f"{'Rise Up: Silver' if standingDunk >= SILVER and standingDunk < GOLD else ''}",
        f"{'Rise Up: Gold' if standingDunk >= GOLD and standingDunk < HOF else ''}",
        f"{'Rise Up: Hall of Fame' if standingDunk >= HOF else ''}",

        f"{'Slithery: Bronze' if max(layup, drivingDunk) >= BRONZE and max(layup, drivingDunk) < SILVER else ''}",
        f"{'Slithery: Silver' if max(layup, drivingDunk) >= SILVER and max(layup, drivingDunk) < GOLD and acceleration >= BRONZE else ''}",
        f"{'Slithery: Gold' if max(layup, drivingDunk) >= GOLD and max(layup, drivingDunk) < HOF and acceleration >= SILVER else ''}",
        f"{'Slithery: Hall of Fame' if max(layup, drivingDunk) >= HOF and acceleration >= GOLD else ''}",
        
        f"{'Bunny: Bronze' if max(drivingDunk, layup) >= BRONZE and max(drivingDunk, layup) < SILVER and hands >= BRONZE else ''}",
        f"{'Bunny: Silver' if max(drivingDunk, layup) >= SILVER and max(drivingDunk, layup) < GOLD  and hands >= SILVER and vertical >= BRONZE  else ''}",
        f"{'Bunny: Gold' if max(drivingDunk, layup) >= GOLD and max(drivingDunk, layup) < HOF and hands >= GOLD and vertical >= SILVER else ''}",
        f"{'Bunny: Hall of Fame' if max(drivingDunk, layup) >= HOF and hands >= HOF and vertical >= GOLD else ''}",

        f"{'Float Game: Bronze' if max(layup, closeShot) >= BRONZE and max(layup, closeShot) < SILVER and hands >= BRONZE else ''}",
        f"{'Float Game: Silver' if max(layup, closeShot) >= SILVER and max(layup, closeShot) < GOLD and hands >= SILVER else ''}",
        f"{'Float Game: Gold' if max(layup, closeShot) >= GOLD and max(layup, closeShot) < HOF and hands >= GOLD else ''}",
        f"{'Float Game: Hall of Fame' if max(layup, closeShot) >= HOF and hands >= HOF else ''}",

        f"{'Hook Specialist: Bronze' if postHook >= BRONZE and postHook < SILVER else ''}",
        f"{'Hook Specialist: Silver' if postHook >= SILVER and postHook < GOLD else ''}",
        f"{'Hook Specialist: Gold' if postHook >= GOLD and postHook < HOF else ''}",
        f"{'Hook Specialist: Hall of Fame' if postHook >= HOF else ''}",

        f"{'Precision Dunker: Bronze' if max(standingDunk, drivingDunk) >= BRONZE and max(standingDunk, drivingDunk) < SILVER and hands >= BRONZE else ''}",
        f"{'Precision Dunker: Silver' if max(standingDunk, drivingDunk) >= SILVER and max(standingDunk, drivingDunk) < GOLD and hands >= SILVER else ''}",
        f"{'Precision Dunker: Gold' if max(standingDunk, drivingDunk) >= GOLD and max(standingDunk, drivingDunk) < HOF and hands >= GOLD else ''}",
        f"{'Precision Dunker: Hall of Fame' if max(standingDunk, drivingDunk) >= HOF and hands >= HOF else ''}",

        f"{'Scooper: Bronze' if layup >= BRONZE and layup < SILVER and ballHandle >= BRONZE else ''}",
        f"{'Scooper: Silver' if layup >= SILVER and layup < GOLD and ballHandle >= SILVER else ''}",
        f"{'Scooper: Gold' if layup >= GOLD and layup < HOF and ballHandle >= GOLD else ''}",
        f"{'Scooper: Hall of Fame' if layup >= HOF and ballHandle >= HOF else ''}",
 
        f"{'Spin Cycle: Bronze' if layup >= BRONZE + 2 and layup < SILVER + 2 and ballHandle >= BRONZE else ''}",
        f"{'Spin Cycle: Silver' if layup >= SILVER + 2 and layup < GOLD + 2 and ballHandle >= SILVER else ''}",
        f"{'Spin Cycle: Gold' if layup >= GOLD + 2 and layup < HOF + 2 and ballHandle >= GOLD else ''}",
        f"{'Spin Cycle: Hall of Fame' if layup >= HOF + 2 and ballHandle >= HOF else ''}",

        f"{'Two Step: Bronze' if layup >= BRONZE and layup < SILVER and hands >= BRONZE else ''}",
        f"{'Two Step: Silver' if layup >= SILVER and layup < GOLD and hands >= SILVER else ''}",
        f"{'Two Step: Gold' if layup >= GOLD and layup < HOF and hands >= GOLD else ''}",
        f"{'Two Step: Hall of Fame' if layup >= HOF and hands >= HOF else ''}",

        f"{'Whistle: Bronze' if drawFoul >= BRONZE and drawFoul < SILVER else ''}",
        f"{'Whistle: Silver' if drawFoul >= SILVER and drawFoul < GOLD else ''}",
        f"{'Whistle: Gold' if drawFoul >= GOLD and drawFoul < HOF else ''}",
        f"{'Whistle: Hall of Fame' if drawFoul >= HOF else ''}",

        f"{'Agent 3: Bronze' if threePointShot >= BRONZE and threePointShot < SILVER and ballHandle >= BRONZE else ''}",
        f"{'Agent 3: Silver' if threePointShot >= SILVER and threePointShot < GOLD and ballHandle >= SILVER else ''}",
        f"{'Agent 3: Gold' if threePointShot >= GOLD and threePointShot < HOF and ballHandle >= GOLD else ''}",
        f"{'Agent 3: Hall of Fame' if threePointShot >= HOF and ballHandle >= HOF else ''}",

        f"{'Blinders: Bronze' if shotIQ >= BRONZE and shotIQ < SILVER else ''}",
        f"{'Blinders: Silver' if shotIQ >= SILVER and shotIQ < GOLD and max(midRangeShot, threePointShot) >= BRONZE else ''}",
        f"{'Blinders: Gold' if shotIQ >= GOLD and shotIQ < HOF and max(midRangeShot, threePointShot) >= SILVER else ''}",
        f"{'Blinders: Hall of Fame' if shotIQ >= HOF and max(midRangeShot, threePointShot) >= GOLD else ''}",
        
        f"{'Catch and Shoot: Bronze' if max(midRangeShot, threePointShot) >= BRONZE and max(midRangeShot, threePointShot) < SILVER and shotIQ >= BRONZE else ''}",
        f"{'Catch and Shoot: Silver' if max(midRangeShot, threePointShot) >= SILVER and max(midRangeShot, threePointShot) < GOLD and shotIQ >= SILVER else ''}",
        f"{'Catch and Shoot: Gold' if max(midRangeShot, threePointShot) >= GOLD and max(midRangeShot, threePointShot) < HOF and shotIQ >= GOLD else ''}",
        f"{'Catch and Shoot: Hall of Fame' if max(midRangeShot, threePointShot) >= HOF and shotIQ >= HOF else ''}",
        
        f"{'Claymore: Bronze' if shotIQ >= BRONZE and shotIQ < SILVER else ''}",
        f"{'Claymore: Silver' if shotIQ >= SILVER and shotIQ < GOLD else ''}",
        f"{'Claymore: Gold' if shotIQ >= GOLD and shotIQ < HOF else ''}",
        f"{'Claymore: Hall of Fame' if shotIQ >= HOF else ''}",
        
        f"{'Comeback Kid: Bronze' if shotIQ >= BRONZE and shotIQ < SILVER and offensiveConsistency >= BRONZE else ''}",
        f"{'Comeback Kid: Silver' if shotIQ >= SILVER and shotIQ < GOLD and offensiveConsistency >= SILVER else ''}",
        f"{'Comeback Kid: Gold' if shotIQ >= GOLD and shotIQ < HOF and offensiveConsistency >= GOLD else ''}",
        f"{'Comeback Kid: Hall of Fame' if shotIQ >= HOF and offensiveConsistency >= HOF else ''}",

        f"{'Corner Specialist: Bronze' if threePointShot >= BRONZE and threePointShot < SILVER and shotIQ >= BRONZE else ''}",
        f"{'Corner Specialist: Silver' if threePointShot >= SILVER and threePointShot < GOLD and shotIQ >= SILVER else ''}",
        f"{'Corner Specialist: Gold' if threePointShot >= GOLD and threePointShot < HOF and shotIQ >= GOLD else ''}",
        f"{'Corner Specialist: Hall of Fame' if threePointShot >= HOF and shotIQ >= HOF else ''}",
        
        f"{'Deadeye: Bronze' if shotIQ >= BRONZE and shotIQ < SILVER else ''}",
        f"{'Deadeye: Silver' if shotIQ >= SILVER and shotIQ < GOLD and max(midRangeShot, threePointShot) >= BRONZE else ''}",
        f"{'Deadeye: Gold' if shotIQ >= GOLD and shotIQ < HOF and max(midRangeShot, threePointShot) >= SILVER else ''}",
        f"{'Deadeye: Hall of Fame' if shotIQ >= HOF and max(midRangeShot, threePointShot) >= GOLD else ''}",

        f"{'Green Machine: Bronze' if max(midRangeShot, threePointShot) >= BRONZE and max(midRangeShot, threePointShot) < SILVER and shotIQ >= BRONZE else ''}",
        f"{'Green Machine: Silver' if max(midRangeShot, threePointShot) >= SILVER and max(midRangeShot, threePointShot) < GOLD and shotIQ >= SILVER else ''}",
        f"{'Green Machine: Gold' if max(midRangeShot, threePointShot) >= GOLD and max(midRangeShot, threePointShot) < HOF and shotIQ >= GOLD else ''}",
        f"{'Green Machine: Hall of Fame' if max(midRangeShot, threePointShot) >= HOF and shotIQ >= HOF else ''}",
    
        f"{'Guard Up: Bronze' if shotIQ >= BRONZE and shotIQ < SILVER else ''}",
        f"{'Guard Up: Silver' if shotIQ >= SILVER and shotIQ < GOLD and max(midRangeShot, threePointShot) >= BRONZE else ''}",
        f"{'Guard Up: Gold' if shotIQ >= GOLD and shotIQ < HOF and max(midRangeShot, threePointShot) >= SILVER else ''}",
        f"{'Guard Up: Hall of Fame' if shotIQ >= HOF and max(midRangeShot, threePointShot) >= GOLD else ''}",
        
        f"{'Limitless Range: Bronze' if threePointShot >= BRONZE + 3 and threePointShot < SILVER + 3 else ''}",
        f"{'Limitless Range: Silver' if threePointShot >= SILVER + 3 and threePointShot < GOLD + 3 else ''}",
        f"{'Limitless Range: Gold' if threePointShot >= GOLD + 3 and threePointShot < HOF + 3 else ''}",
        f"{'Limitless Range: Hall of Fame' if threePointShot >= HOF + 3 else ''}",
        
        f"{'Middy Magician: Bronze' if midRangeShot >= BRONZE and midRangeShot < SILVER else ''}",
        f"{'Middy Magician: Silver' if midRangeShot >= SILVER and midRangeShot < GOLD else ''}",
        f"{'Middy Magician: Gold' if midRangeShot >= GOLD and midRangeShot < HOF else ''}",
        f"{'Middy Magician: Hall of Fame' if midRangeShot >= HOF else ''}",
        
        f"{'Slippery Off-Ball: Bronze' if shotIQ >= BRONZE and shotIQ < SILVER and offensiveConsistency >= BRONZE and acceleration >= BRONZE else ''}",
        f"{'Slippery Off-Ball: Silver' if shotIQ >= SILVER and shotIQ < GOLD and offensiveConsistency >= SILVER and acceleration >= SILVER else ''}",
        f"{'Slippery Off-Ball: Gold' if shotIQ >= GOLD and shotIQ < HOF and offensiveConsistency >= GOLD and acceleration >= GOLD else ''}",
        f"{'Slippery Off-Ball: Hall of Fame' if shotIQ >= HOF and offensiveConsistency >= HOF and acceleration >= HOF else ''}",
        
        f"{'Space Creator: Bronze' if shotIQ >= BRONZE and shotIQ < SILVER and ballHandle >= BRONZE else ''}",
        f"{'Space Creator: Silver' if shotIQ >= SILVER and shotIQ < GOLD and ballHandle >= SILVER else ''}",
        f"{'Space Creator: Gold' if shotIQ >= GOLD and shotIQ < HOF and ballHandle >= GOLD else ''}",
        f"{'Space Creator: Hall of Fame' if shotIQ >= HOF and ballHandle >= HOF else ''}",

        f"{'Free Points: Bronze' if freeThrow >= BRONZE and freeThrow < SILVER and offensiveConsistency >= BRONZE else ''}",
        f"{'Free Points: Silver' if freeThrow >= SILVER and freeThrow < GOLD and offensiveConsistency >= SILVER else ''}",
        f"{'Free Points: Gold' if freeThrow >= GOLD and freeThrow < HOF and offensiveConsistency >= GOLD else ''}",
        f"{'Free Points: Hall of Fame' if freeThrow >= HOF and offensiveConsistency >= HOF else ''}",
  
        f"{'Open Looks: Bronze' if shotIQ >= BRONZE and shotIQ < SILVER else ''}",
        f"{'Open Looks: Silver' if shotIQ >= SILVER and shotIQ < GOLD else ''}",
        f"{'Open Looks: Gold' if shotIQ >= GOLD and shotIQ < HOF else ''}",
        f"{'Open Looks: Hall of Fame' if shotIQ >= HOF else ''}",
        
        f"{'Post Fade Phenom: Bronze' if postFade >= BRONZE and postFade < SILVER else ''}",
        f"{'Post Fade Phenom: Silver' if postFade >= SILVER and postFade < GOLD else ''}",
        f"{'Post Fade Phenom: Gold' if postFade >= GOLD and postFade < HOF else ''}",
        f"{'Post Fade Phenom: Hall of Fame' if postFade >= HOF else ''}",

        f"{'Spot Finder: Bronze' if shotIQ >= BRONZE and shotIQ < SILVER else ''}",
        f"{'Spot Finder: Silver' if shotIQ >= SILVER and shotIQ < GOLD else ''}",
        f"{'Spot Finder: Gold' if shotIQ >= GOLD and shotIQ < HOF else ''}",
        f"{'Spot Finder: Hall of Fame' if shotIQ >= HOF else ''}",

        f"{'Ankle Breaker: Bronze' if ballHandle >= BRONZE and ballHandle < SILVER else ''}",
        f"{'Ankle Breaker: Silver' if ballHandle >= SILVER and ballHandle < GOLD else ''}",
        f"{'Ankle Breaker: Gold' if ballHandle >= GOLD and ballHandle < HOF else ''}",
        f"{'Ankle Breaker: Hall of Fame' if ballHandle >= HOF else ''}",
        
        f"{'Bail Out: Bronze' if ballHandle >= BRONZE and ballHandle < SILVER and passIQ >= BRONZE else ''}",
        f"{'Bail Out: Silver' if ballHandle >= SILVER and ballHandle < GOLD and passIQ >= SILVER else ''}",
        f"{'Bail Out: Gold' if ballHandle >= GOLD and ballHandle < HOF and passIQ >= GOLD else ''}",
        f"{'Bail Out: Hall of Fame' if ballHandle >= HOF and passIQ >= HOF else ''}",
        
        f"{'Break Starter: Bronze' if passAccuracy >= BRONZE and passAccuracy < SILVER and defensiveRebound >= BRONZE else ''}",
        f"{'Break Starter: Silver' if passAccuracy >= SILVER and passAccuracy < GOLD and defensiveRebound >= SILVER else ''}",
        f"{'Break Starter: Gold' if passAccuracy >= GOLD and passAccuracy < HOF and defensiveRebound >= GOLD else ''}",
        f"{'Break Starter: Hall of Fame' if passAccuracy >= HOF and defensiveRebound >= HOF else ''}",
        
        f"{'Dimer: Bronze' if passAccuracy >= BRONZE and passAccuracy < SILVER and passIQ >= BRONZE else ''}",
        f"{'Dimer: Silver' if passAccuracy >= SILVER and passAccuracy < GOLD and passIQ >= SILVER else ''}",
        f"{'Dimer: Gold' if passAccuracy >= GOLD and passAccuracy < HOF and passIQ >= GOLD else ''}",
        f"{'Dimer: Hall of Fame' if passAccuracy >= HOF and passIQ >= HOF else ''}",
        
        f"{'Handles For Days: Bronze' if ballHandle >= BRONZE and ballHandle < SILVER and stamina >= BRONZE else ''}",
        f"{'Handles For Days: Silver' if ballHandle >= SILVER and ballHandle < GOLD and stamina >= SILVER else ''}",
        f"{'Handles For Days: Gold' if ballHandle >= GOLD and ballHandle < HOF and stamina >= GOLD else ''}",
        f"{'Handles For Days: Hall of Fame' if ballHandle >= HOF and stamina >= HOF else ''}",
        
        f"{'Hyperdrive: Bronze' if ballHandle >= BRONZE and ballHandle < SILVER else ''}",
        f"{'Hyperdrive: Silver' if ballHandle >= SILVER and ballHandle < GOLD else ''}",
        f"{'Hyperdrive: Gold' if ballHandle >= GOLD and ballHandle < HOF else ''}",
        f"{'Hyperdrive: Hall of Fame' if ballHandle >= HOF else ''}",
        
        f"{'Killer Combos: Bronze' if ballHandle >= BRONZE + 3 and ballHandle < SILVER +3 else ''}",
        f"{'Killer Combos: Silver' if ballHandle >= SILVER + 3 and ballHandle < GOLD + 3 else ''}",
        f"{'Killer Combos: Gold' if ballHandle >= GOLD + 3 and ballHandle < HOF + 3 else ''}",
        f"{'Killer Combos: Hall of Fame' if ballHandle >= HOF + 3 else ''}",
        
        f"{'Needle Threader: Bronze' if passAccuracy >= BRONZE and passAccuracy < SILVER and passIQ >= BRONZE else ''}",
        f"{'Needle Threader: Silver' if passAccuracy >= SILVER and passAccuracy < GOLD and passIQ >= SILVER else ''}",
        f"{'Needle Threader: Gold' if passAccuracy >= GOLD and passAccuracy < HOF and passIQ >= GOLD else ''}",
        f"{'Needle Threader: Hall of Fame' if passAccuracy >= HOF and passIQ >= HOF else ''}",
        
        f"{'Post Playmaker: Bronze' if passAccuracy >= BRONZE and passAccuracy < SILVER and postControl >= BRONZE else ''}",
        f"{'Post Playmaker: Silver' if passAccuracy >= SILVER and passAccuracy < GOLD and postControl >= SILVER else ''}",
        f"{'Post Playmaker: Gold' if passAccuracy >= GOLD and passAccuracy < HOF and postControl >= GOLD else ''}",
        f"{'Post Playmaker: Hall of Fame' if passAccuracy >= HOF and postControl >= HOF else ''}",
        
        f"{'Special Delivery: Bronze' if passVision >= BRONZE and passVision < SILVER and passIQ >= BRONZE else ''}",
        f"{'Special Delivery: Silver' if passVision >= SILVER and passVision < GOLD and passIQ >= SILVER else ''}",
        f"{'Special Delivery: Gold' if passVision >= GOLD and passVision < HOF and passIQ >= GOLD else ''}",
        f"{'Special Delivery: Hall of Fame' if passVision >= HOF and passIQ >= HOF else ''}",
        
        f"{'Unpluckable: Bronze' if hands >= BRONZE and hands < SILVER and ballHandle >= BRONZE else ''}",
        f"{'Unpluckable: Silver' if hands >= SILVER and hands < GOLD and ballHandle >= SILVER else ''}",
        f"{'Unpluckable: Gold' if hands >= GOLD and hands < HOF and ballHandle >= GOLD else ''}",
        f"{'Unpluckable: Hall of Fame' if hands >= HOF and ballHandle >= HOF else ''}",
    
        f"{'Big Driver: Bronze' if max(drivingDunk, layup) >= BRONZE and max(drivingDunk, layup) < SILVER and max(closeShot, midRangeShot) >= BRONZE else ''}",
        f"{'Big Driver: Silver' if max(drivingDunk, layup) >= SILVER and max(drivingDunk, layup) < GOLD and max(closeShot, midRangeShot) >= SILVER else ''}",
        f"{'Big Driver: Gold' if max(drivingDunk, layup) >= GOLD and max(drivingDunk, layup) < HOF and max(closeShot, midRangeShot) >= GOLD else ''}",
        f"{'Big Driver: Hall of Fame' if max(drivingDunk, layup) >= HOF and max(closeShot, midRangeShot) >= HOF else ''}",

        f"{'Blow-By: Bronze' if acceleration >= BRONZE and acceleration < SILVER else ''}",
        f"{'Blow-By: Silver' if acceleration >= SILVER and acceleration < GOLD else ''}",
        f"{'Blow-By: Gold' if acceleration >= GOLD and acceleration < HOF else ''}",
        f"{'Blow-By: Hall of Fame' if acceleration >= HOF else ''}",

        f"{'Physical Handles: Bronze' if ballHandle >= BRONZE and ballHandle < SILVER and strength >= BRONZE else ''}",
        f"{'Physical Handles: Silver' if ballHandle >= SILVER and ballHandle < GOLD and strength >= SILVER else ''}",
        f"{'Physical Handles: Gold' if ballHandle >= GOLD and ballHandle < HOF and strength >= GOLD else ''}",
        f"{'Physical Handles: Hall of Fame' if ballHandle >= HOF and strength >= HOF else ''}",

        f"{'Relay Passer: Bronze' if passIQ >= BRONZE and passIQ < SILVER else ''}",
        f"{'Relay Passer: Silver' if passIQ >= SILVER and passIQ < GOLD else ''}",
        f"{'Relay Passer: Gold' if passIQ >= GOLD and passIQ < HOF else ''}",
        f"{'Relay Passer: Hall of Fame' if passIQ >= HOF else ''}",

        f"{'Speed Booster: Bronze' if acceleration >= BRONZE and acceleration < SILVER and ballHandle >= BRONZE else ''}",
        f"{'Speed Booster: Silver' if acceleration >= SILVER and acceleration < GOLD and ballHandle >= SILVER else ''}",
        f"{'Speed Booster: Gold' if acceleration >= GOLD and acceleration < HOF and ballHandle >= GOLD else ''}",
        f"{'Speed Booster: Hall of Fame' if acceleration >= HOF and ballHandle >= HOF else ''}",
        
        f"{'Touch Passer: Bronze' if passVision >= BRONZE and passVision < SILVER and passIQ >= BRONZE else ''}",
        f"{'Touch Passer: Silver' if passVision >= SILVER and passVision < GOLD and passIQ >= SILVER else ''}",
        f"{'Touch Passer: Gold' if passVision >= GOLD and passVision < HOF and passIQ >= GOLD else ''}",
        f"{'Touch Passer: Hall of Fame' if passVision >= HOF and passIQ >= HOF else ''}",
        
        f"{'Triple Strike: Bronze' if acceleration >= BRONZE and acceleration < SILVER and ballHandle >= BRONZE else ''}",
        f"{'Triple Strike: Silver' if acceleration >= SILVER and acceleration < GOLD and ballHandle >= SILVER else ''}",
        f"{'Triple Strike: Gold' if acceleration >= GOLD and acceleration < HOF and ballHandle >= GOLD else ''}",
        f"{'Triple Strike: Hall of Fame' if acceleration >= HOF and ballHandle >= HOF else ''}",
        
        f"{'Anchor: Bronze' if block >= BRONZE and block < SILVER and defensiveConsistency >= BRONZE else ''}",
        f"{'Anchor: Silver' if block >= SILVER and block < GOLD and defensiveConsistency >= SILVER else ''}",
        f"{'Anchor: Gold' if block >= GOLD and block < HOF and defensiveConsistency >= GOLD else ''}",
        f"{'Anchor: Hall of Fame' if block >= HOF and defensiveConsistency >= HOF else ''}",
        
        f"{'Ankle Braces: Bronze' if lateralQuickness >= BRONZE and lateralQuickness < SILVER and perimeterDefense >= BRONZE else ''}",
        f"{'Ankle Braces: Silver' if lateralQuickness >= SILVER and lateralQuickness < GOLD and perimeterDefense >= SILVER else ''}",
        f"{'Ankle Braces: Gold' if lateralQuickness >= GOLD and lateralQuickness < HOF and perimeterDefense >= GOLD else ''}",
        f"{'Ankle Braces: Hall of Fame' if lateralQuickness >= HOF and perimeterDefense >= HOF else ''}",
        
        f"{'Challenger: Bronze' if perimeterDefense >= BRONZE and perimeterDefense < SILVER and block >= BRONZE else ''}",
        f"{'Challenger: Silver' if perimeterDefense >= SILVER and perimeterDefense < GOLD and block >= SILVER else ''}",
        f"{'Challenger: Gold' if perimeterDefense >= GOLD and perimeterDefense < HOF and block >= GOLD else ''}",
        f"{'Challenger: Hall of Fame' if perimeterDefense >= HOF and block >= HOF else ''}",
        
        f"{'Chase Down Artist: Bronze' if block >= BRONZE and block < SILVER and helpDefenseIQ >= BRONZE else ''}",
        f"{'Chase Down Artist: Silver' if block >= SILVER and block < GOLD and helpDefenseIQ >= SILVER else ''}",
        f"{'Chase Down Artist: Gold' if block >= GOLD and block < HOF and helpDefenseIQ >= GOLD else ''}",
        f"{'Chase Down Artist: Hall of Fame' if block >= HOF and helpDefenseIQ >= HOF else ''}",
        
        f"{'Clamps: Bronze' if perimeterDefense >= BRONZE and perimeterDefense < SILVER and strength >= BRONZE else ''}",
        f"{'Clamps: Silver' if perimeterDefense >= SILVER and perimeterDefense < GOLD and strength >= SILVER else ''}",
        f"{'Clamps: Gold' if perimeterDefense >= GOLD and perimeterDefense < HOF and strength >= GOLD else ''}",
        f"{'Clamps: Hall of Fame' if perimeterDefense >= HOF and strength >= HOF else ''}",
        
        f"{'Glove: Bronze' if steal >= BRONZE and steal < SILVER else ''}",
        f"{'Glove: Silver' if steal >= SILVER and steal < GOLD else ''}",
        f"{'Glove: Gold' if steal >= GOLD and steal < HOF else ''}",
        f"{'Glove: Hall of Fame' if steal >= HOF else ''}",
        
        f"{'Interceptor: Bronze' if passPerception >= BRONZE and passPerception < SILVER else ''}",
        f"{'Interceptor: Silver' if passPerception >= SILVER and passPerception < GOLD else ''}",
        f"{'Interceptor: Gold' if passPerception >= GOLD and passPerception < HOF else ''}",
        f"{'Interceptor: Hall of Fame' if passPerception >= HOF else ''}",
        
        f"{'Off-Ball Pest: Bronze' if strength >= BRONZE and strength < SILVER and helpDefenseIQ >= BRONZE else ''}",
        f"{'Off-Ball Pest: Silver' if strength >= SILVER and strength < GOLD and helpDefenseIQ >= SILVER else ''}",
        f"{'Off-Ball Pest: Gold' if strength >= GOLD and strength < HOF and helpDefenseIQ >= GOLD else ''}",
        f"{'Off-Ball Pest: Hall of Fame' if strength >= HOF and helpDefenseIQ >= HOF else ''}",
        
        f"{'Pick Dodger: Bronze' if lateralQuickness >= BRONZE and lateralQuickness < SILVER else ''}",
        f"{'Pick Dodger: Silver' if lateralQuickness >= SILVER and lateralQuickness < GOLD else ''}",
        f"{'Pick Dodger: Gold' if lateralQuickness >= GOLD and lateralQuickness < HOF else ''}",
        f"{'Pick Dodger: Hall of Fame' if lateralQuickness >= HOF else ''}",
        
        f"{'Post Lockdown: Bronze' if interiorDefense >= BRONZE and interiorDefense < SILVER else ''}",
        f"{'Post Lockdown: Silver' if interiorDefense >= SILVER and interiorDefense < GOLD else ''}",
        f"{'Post Lockdown: Gold' if interiorDefense >= GOLD and interiorDefense < HOF else ''}",
        f"{'Post Lockdown: Hall of Fame' if interiorDefense >= HOF else ''}",
  
        f"{'Pogo Stick: Bronze' if vertical >= BRONZE and vertical < SILVER and defensiveConsistency >= BRONZE else ''}",
        f"{'Pogo Stick: Silver' if vertical >= SILVER and vertical < GOLD and defensiveConsistency >= SILVER else ''}",
        f"{'Pogo Stick: Gold' if vertical >= GOLD and vertical < HOF and defensiveConsistency >= GOLD else ''}",
        f"{'Pogo Stick: Hall of Fame' if vertical >= HOF and defensiveConsistency >= HOF else ''}",
        
        f"{'Work Horse: Bronze' if defensiveConsistency >= BRONZE and defensiveConsistency < SILVER and helpDefenseIQ >= BRONZE else ''}",
        f"{'Work Horse: Silver' if defensiveConsistency >= SILVER and defensiveConsistency < GOLD and helpDefenseIQ >= SILVER else ''}",
        f"{'Work Horse: Gold' if defensiveConsistency >= GOLD and defensiveConsistency < HOF and helpDefenseIQ >= GOLD else ''}",
        f"{'Work Horse: Hall of Fame' if defensiveConsistency >= HOF and helpDefenseIQ >= HOF else ''}",

        f"{'Fast Feet: Bronze' if perimeterDefense >= BRONZE and perimeterDefense < SILVER and lateralQuickness >= BRONZE else ''}",
        f"{'Fast Feet: Silver' if perimeterDefense >= SILVER and perimeterDefense < GOLD and lateralQuickness >= SILVER else ''}",
        f"{'Fast Feet: Gold' if perimeterDefense >= GOLD and perimeterDefense < HOF and lateralQuickness >= GOLD else ''}",
        f"{'Fast Feet: Hall of Fame' if perimeterDefense >= HOF and lateralQuickness >= HOF else ''}",
        
        f"{'Right Stick Ripper: Bronze' if steal >= BRONZE and steal < SILVER else ''}",
        f"{'Right Stick Ripper: Silver' if steal >= SILVER and steal < GOLD else ''}",
        f"{'Right Stick Ripper: Gold' if steal >= GOLD and steal < HOF else ''}",
        f"{'Right Stick Ripper: Hall of Fame' if steal >= HOF else ''}",
        
        f"{'Brick Wall: Bronze' if strength >= BRONZE and strength < SILVER else ''}",
        f"{'Brick Wall: Silver' if strength >= SILVER and strength < GOLD else ''}",
        f"{'Brick Wall: Gold' if strength >= GOLD and strength < HOF else ''}",
        f"{'Brick Wall: Hall of Fame' if strength >= HOF else ''}",

        f"{'Bulldozer: Bronze' if postControl >= BRONZE and postControl < SILVER and strength >= BRONZE else ''}",
        f"{'Bulldozer: Silver' if postControl >= SILVER and postControl < GOLD and strength >= SILVER else ''}",
        f"{'Bulldozer: Gold' if postControl >= GOLD and postControl < HOF and strength >= GOLD < HOF else ''}",
        f"{'Bulldozer: Hall of Fame' if postControl >= HOF and strength >= HOF else ''}",

        f"{'Immovable Enforcer: Bronze' if strength >= BRONZE and strength < SILVER else ''}",
        f"{'Immovable Enforcer: Silver' if strength >= SILVER and strength < GOLD else ''}",
        f"{'Immovable Enforcer: Gold' if strength >= GOLD and strength < HOF else ''}",
        f"{'Immovable Enforcer: Hall of Fame' if strength >= HOF else ''}",

        f"{'94 Feet: Bronze' if lateralQuickness >= BRONZE and lateralQuickness < SILVER and defensiveConsistency >= BRONZE else ''}",
        f"{'94 Feet: Silver' if lateralQuickness >= SILVER and lateralQuickness < GOLD and defensiveConsistency >= SILVER else ''}",
        f"{'94 Feet: Gold' if lateralQuickness >= GOLD and lateralQuickness < HOF and defensiveConsistency >= GOLD else ''}",
        f"{'94 Feet: Hall of Fame' if lateralQuickness >= HOF and defensiveConsistency >= HOF else ''}",

        f"{'Boxout Beast: Bronze' if interiorDefense >= BRONZE and interiorDefense < SILVER and strength >= BRONZE else ''}",
        f"{'Boxout Beast: Silver' if interiorDefense >= SILVER and interiorDefense < GOLD and strength >= SILVER else ''}",
        f"{'Boxout Beast: Gold' if interiorDefense >= GOLD and interiorDefense < HOF and strength >= GOLD else ''}",
        f"{'Boxout Beast: Hall of Fame' if interiorDefense >= HOF and strength >= HOF else ''}",

        f"{'Rebound Chaser: Bronze' if max(offensiveRebound, defensiveRebound) >= BRONZE and max(offensiveRebound, defensiveRebound) < SILVER else ''}",
        f"{'Rebound Chaser: Silver' if max(offensiveRebound, defensiveRebound) >= SILVER and max(offensiveRebound, defensiveRebound) < GOLD else ''}",
        f"{'Rebound Chaser: Gold' if max(offensiveRebound, defensiveRebound) >= GOLD and max(offensiveRebound, defensiveRebound) < HOF else ''}",
        f"{'Rebound Chaser: Hall of Fame' if max(offensiveRebound, defensiveRebound) >= HOF else ''}",

        f"{'Work Ethic: Bronze' if workEthic == 0 else ''}",
        f"{'Work Ethic: Silver' if workEthic == 1 else ''}",
        f"{'Work Ethic: Gold' if workEthic == 2 else ''}",
        f"{'Work Ethic: Hall of Fame' if workEthic == 3 else ''}",
    ]
    
    playerStats += "Badges:\n" + "\n".join(filter(None, badges))
    
    return playerStats
    
def main():
    userInput = input
    typeOfPlayer = ""
    while userInput != 0:
        userInput = int(input("0. Quit\n\n1. PG\n2. SG\n3. SF\n4. PF\n5. C\n\nInput: "))
        if userInput == 1:
            print("1. Rookie\n2. Young\n3. All-Star\n4. Superstar")
            userInput = int(input("Input: "))
            if userInput == 1:
                typeOfPlayer = "R"
            if userInput == 2:
                typeOfPlayer = "Y"
            if userInput == 3:
                typeOfPlayer = "AS"
            if userInput == 4:
                typeOfPlayer = "SS"
            print("Choose Playstyle")
            print("1. Scoring Machine\n2. 2-Way Sharpshooter\n3. Slashing Shot Creator\n4. Sharpshooting Playmaker\n5. 2-Way All Around Threat")
            proficiencyChoice = int(input("Enter a number from 1 to 5 to select a playstyle: "))

            if proficiencyChoice == 1:
                print(generatePlayer(typeOfPlayer,"PG", 1.3, 1.3, 1.0, 1.3, 1.2, 1.0))

            elif proficiencyChoice == 2:
                print(generatePlayer(typeOfPlayer,"PG", 1.3, 1.2, 1.3, 1.2, 1.2, 1.2))

            elif proficiencyChoice == 3:
                print(generatePlayer(typeOfPlayer,"PG", 1.2, 1.3, 1.0, 1.3, 1.2, 1.0))

            elif proficiencyChoice == 4:
                print(generatePlayer(typeOfPlayer,"PG", 1.3, 1.2, 1.0, 1.3, 1.3, 1.0))

            elif proficiencyChoice == 5:
                print(generatePlayer(typeOfPlayer,"PG", 1.2, 1.2, 1.2, 1.3, 1.2, 1.2))
            else:
                print("Invalid playstyle choice. Please enter a number between 1 and 5")
            userInput = input("\nPress Enter to continue...\n")
        elif userInput == 2:
            print("1. Rookie\n2. Young\n3. All-Star\n4. Superstar")
            userInput = int(input("Input: "))
            if userInput == 1:
                typeOfPlayer = "R"
            if userInput == 2:
                typeOfPlayer = "Y"
            if userInput == 3:
                typeOfPlayer = "AS"
            if userInput == 4:
                typeOfPlayer = "SS"
            print("Choose Playstyle")
            print("1. Scoring Machine\n2. 2-Way Sharpshooter\n3. Slashing Playmaker\n4. 2-Way Slasher\n5. Playmaking Sharpshooter")
            proficiencyChoice = int(input("Enter a number from 1 to 5 to select a playstyle: "))

            if proficiencyChoice == 1:
                print(generatePlayer(typeOfPlayer,"SG", 1.3, 1.3, 1.0, 1.2, 1.1, 1.0))

            elif proficiencyChoice == 2:
                print(generatePlayer(typeOfPlayer,"SG", 1.3, 1.1, 1.3, 1.2, 1.0, 1.1))

            elif proficiencyChoice == 3:
                print(generatePlayer(typeOfPlayer,"SG", 1.2, 1.3, 1.0, 1.3, 1.4, 1.0))

            elif proficiencyChoice == 4:
                print(generatePlayer(typeOfPlayer,"SG", 1.2, 1.3, 1.3, 1.3, 1.0, 1.2))

            elif proficiencyChoice == 5:
                print(generatePlayer(typeOfPlayer,"SG", 1.3, 1.1, 1.1, 1.2, 1.4, 1.0))
            else:
                print("Invalid playstyle choice. Please enter a number between 1 and 5")
            userInput = input("\nPress Enter to continue...\n")
        elif userInput == 3:
            print("1. Rookie\n2. Young\n3. All-Star\n4. Superstar")
            userInput = int(input("Input: "))
            if userInput == 1:
                typeOfPlayer = "R"
            if userInput == 2:
                typeOfPlayer = "Y"
            if userInput == 3:
                typeOfPlayer = "AS"
            if userInput == 4:
                typeOfPlayer = "SS"
            print("Choose Playstyle")
            print("1. 3-Level Scorer\n2. 2-Way Sharpshooter\n3. Lockdown Playmaker\n4. Slasher\n5. 2-Way Finisher")
            proficiencyChoice = int(input("Enter a number from 1 to 5 to select a playstyle: "))

            if proficiencyChoice == 1:
                print(generatePlayer(typeOfPlayer,"SF", 1.3, 1.1, 1.0, 1.3, 1.2, 1.0))

            elif proficiencyChoice == 2:
                print(generatePlayer(typeOfPlayer,"SF", 1.3, 1.1, 1.3, 1.1, 1.0, 1.2))

            elif proficiencyChoice == 3:
                print(generatePlayer(typeOfPlayer,"SF", 1.2, 1.2, 1.3, 1.3, 1.3, 1.3))

            elif proficiencyChoice == 4:
                print(generatePlayer(typeOfPlayer,"SF", 1.2, 1.4, 1.0, 1.4, 1.1, 1.2))

            elif proficiencyChoice == 5:
                print(generatePlayer(typeOfPlayer,"SF", 1.1, 1.4, 1.3, 1.2, 1.0, 1.3))
            else:
                print("Invalid playstyle choice. Please enter a number between 1 and 5")
            userInput = input("\nPress Enter to continue...\n")
        elif userInput == 4:
            print("1. Rookie\n2. Young\n3. All-Star\n4. Superstar")
            userInput = int(input("Input: "))
            if userInput == 1:
                typeOfPlayer = "R"
            if userInput == 2:
                typeOfPlayer = "Y"
            if userInput == 3:
                typeOfPlayer = "AS"
            if userInput == 4:
                typeOfPlayer = "SS"
            print("Choose Playstyle")
            print("1. 3-Level Scorer\n2. Glass Cleaning Big\n3. Interior Threat\n4. 2-Way Rim Protector\n5. 2-Way Playmaking Slasher")
            proficiencyChoice = int(input("Enter a number from 1 to 5 to select a playstyle: "))

            if proficiencyChoice == 1:
                print(generatePlayer(typeOfPlayer,"PF", 1.3, 1.1, 1.0, 1.2, 1.2, 1.1))

            elif proficiencyChoice == 2:
                print(generatePlayer(typeOfPlayer,"PF", 1.1, 1.2, 1.2, 1.3, 1.2, 1.4))

            elif proficiencyChoice == 3:
                print(generatePlayer(typeOfPlayer,"PF", 1.1, 1.4, 1.3, 1.2, 1.2, 1.4))

            elif proficiencyChoice == 4:
                print(generatePlayer(typeOfPlayer,"PF", 1.2, 1.2, 1.4, 1.2, 1.2, 1.4))

            elif proficiencyChoice == 5:
                print(generatePlayer(typeOfPlayer,"PF", 1.2, 1.3, 1.3, 1.4, 1.6, 1.2))
            else:
                print("Invalid playstyle choice. Please enter a number between 1 and 5")
            userInput = input("\nPress Enter to continue...\n")
        elif userInput == 5:
            print("1. Rookie\n2. Young\n3. All-Star\n4. Superstar")
            userInput = int(input("Input: "))
            if userInput == 1:
                typeOfPlayer = "R"
            if userInput == 2:
                typeOfPlayer = "Y"
            if userInput == 3:
                typeOfPlayer = "AS"
            if userInput == 4:
                typeOfPlayer = "SS"
            print("Choose Playstyle")
            print("1. Paint Beast\n2. 2-Way Facilitator\n3. Glass Cleaning Stretch Big\n4. 3-Level Stretch Big\n5. 2-Way Slashing Rim Protector")
            proficiencyChoice = int(input("Enter a number from 1 to 5 to select a playstyle: "))

            if proficiencyChoice == 1:
                print(generatePlayer(typeOfPlayer,"C", 1.1, 1.3, 1.2, 1.2, 1.0, 1.4))

            elif proficiencyChoice == 2:
                print(generatePlayer(typeOfPlayer,"C", 1.2, 1.2, 1.3, 1.2, 1.3, 1.2))

            elif proficiencyChoice == 3:
                print(generatePlayer(typeOfPlayer,"C", 1.3, 1.1, 1.0, 1.2, 1.0, 1.4))

            elif proficiencyChoice == 4:
                print(generatePlayer(typeOfPlayer,"C", 1.4, 1.1, 1.0, 1.2, 1.1, 1.2))

            elif proficiencyChoice == 5:
                print(generatePlayer(typeOfPlayer,"C", 1.1, 1.3, 1.3, 1.3, 1.1, 1.3))
            else:
                print("Invalid playstyle choice. Please enter a number between 1 and 5")
            userInput = input("\nPress Enter to continue...\n")
        elif userInput == 0:
            print("\nGoodbye")
        else:
            print("Invalid input. Please enter a valid position")
if __name__ == "__main__":
    main()
        
