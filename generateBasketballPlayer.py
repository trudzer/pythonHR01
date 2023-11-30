import random

playerList = []

def generateStats(MPG, three_point_attempts, two_point_attempts, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists, steals, blocks, turnovers):
    adjust_stats = MPG / 48.0
    three_point_attempts *= adjust_stats
    two_point_attempts *= adjust_stats
    free_throw_attempts *= adjust_stats
    offensive_rebounds *= adjust_stats
    defensive_rebounds *= adjust_stats
    assists *= adjust_stats
    steals *= adjust_stats
    blocks *= adjust_stats
    turnovers *= adjust_stats
    return three_point_attempts, two_point_attempts, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists, steals, blocks, turnovers

def generatePlayer(POS, MPG, GP):
    if POS == "PG":
        height = random.randint(175, 203)
        weight = random.randint(69, 92)

        total_three_point_attempts = 0
        total_two_point_attempts = 0
        total_free_throw_attempts = 0
        total_offensive_rebounds = 0
        total_defensive_rebounds = 0
        total_assists = 0
        total_steals = 0
        total_blocks = 0
        total_turnovers = 0
        total_two_point_hit = 0
        total_three_point_hit = 0 
        total_free_throw_hit = 0
        
        insideScoring =     random.randint(25, 99)
        insideFinishing =   random.randint(45, 99)
        offensiveMovement = random.randint(55, 99)
        outsideScoring =    random.randint(45, 99)
        playmaking =        random.randint(55, 99)
        insideDefense =     random.randint(25, 99)
        exteriorDefense =   random.randint(45, 99)
        defensiveMovement = random.randint(25, 99)
        athletic =          random.randint(45, 99)
        ballMovement =      random.randint(45, 99)
        
        overall = round(100 * ((insideScoring / 100) * 0.05 
                            + (insideFinishing / 100) * 0.2
                            + (offensiveMovement / 100) * 0.05 
                            + (outsideScoring / 100) * 0.2 
                            + (playmaking / 100) * 0.2 
                            + (insideDefense / 100) * 0.02 
                            + (exteriorDefense / 100) * 0.2 
                            + (defensiveMovement / 100) * 0.05 
                            + (athletic / 100) * 0.05 
                            + (ballMovement / 100) * 0.1))
        
        for i in range(0, GP):
            three_point_attempts, two_point_attempts, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists, steals, blocks, turnovers = generateStats(
                MPG,
                random.uniform(0.0, (30.0 * (0.6 * (outsideScoring / 100) + 0.1 * (ballMovement / 100) + 0.3 * (offensiveMovement / 100)))),  # 3PA
                random.uniform(0.0, (40.0 * (0.4 * insideFinishing / 100) + 0.4 * (insideScoring / 100) + 0.1 * (offensiveMovement / 100) + 0.1 * (athletic * 0.1))),  # 2PA
                random.uniform(0.0, (25.0 * (outsideScoring / 100))),  # FTA
                random.uniform(0.0, (5.0 * (0.5 * (offensiveMovement / 100) + 0.5 * (athletic / 100)))),   # ORB
                random.uniform(0.0, (8.0 * (0.7 * (insideDefense / 100) +  0.1 * (athletic / 100) + 0.2 * (defensiveMovement / 100)))),   # DRB
                random.uniform(0.0, (25.0 * (0.6 * (playmaking / 100) + 0.3 * (offensiveMovement / 100) + 0.1 * (ballMovement / 100)))),  # AST
                random.uniform(0.0, (5.0 * ( 0.7 * (exteriorDefense / 100) + 0.2 * (defensiveMovement / 100) + 0.1 * (athletic / 100)))),   # STL
                random.uniform(0.0, (2.0 * (0.5 * insideDefense / 100) + 0.5 * (height / 100))),   # BLK
                random.uniform(0.0, (4.0 * (100 / ballMovement)))    # TOV
            )
            
            two_point_hit = round(random.uniform(0.25, 1.0) * ((0.05 * (height / 203) + 0.4 * (insideScoring / 100) + 0.4 * (insideFinishing / 100) + 0.05 * (athletic / 100) + 0.1 * (offensiveMovement / 100))) * two_point_attempts)
            three_point_hit = round(random.uniform(0.25, 1.0) * ((0.8 * (outsideScoring / 100) + (0.05 * (height / 203) + 0.15 * (offensiveMovement / 100)))) * three_point_attempts)
            free_throw_hit = round(random.uniform(0.95, ( 1 * (outsideScoring / 100))) * free_throw_attempts)
            
            total_three_point_attempts += three_point_attempts
            total_two_point_attempts += two_point_attempts
            total_free_throw_attempts += free_throw_attempts
            total_offensive_rebounds += offensive_rebounds
            total_defensive_rebounds += defensive_rebounds
            total_assists += assists
            total_steals += steals
            total_blocks += blocks
            total_turnovers += turnovers
            total_two_point_hit += two_point_hit
            total_three_point_hit += three_point_hit
            total_free_throw_hit += free_throw_hit
        
    if POS == "SG":
        height = random.randint(190, 208)
        weight = random.randint(73, 98)
        
        total_three_point_attempts = 0
        total_two_point_attempts = 0
        total_free_throw_attempts = 0
        total_offensive_rebounds = 0
        total_defensive_rebounds = 0
        total_assists = 0
        total_steals = 0
        total_blocks = 0
        total_turnovers = 0
        total_two_point_hit = 0
        total_three_point_hit = 0 
        total_free_throw_hit = 0
        
        insideScoring =     random.randint(45, 99)
        insideFinishing =   random.randint(55, 99)
        offensiveMovement = random.randint(55, 99)
        outsideScoring =    random.randint(55, 99)
        playmaking =        random.randint(25, 99)
        insideDefense =     random.randint(25, 99)
        exteriorDefense =   random.randint(35, 99)
        defensiveMovement = random.randint(25, 99)
        athletic =          random.randint(55, 99)
        ballMovement =      random.randint(45, 99)
        
        overall = round(100 * ((insideScoring / 100) * 0.2
                            + (insideFinishing / 100) * 0.2
                            + (offensiveMovement / 100) * 0.1
                            + (outsideScoring / 100) * 0.3
                            + (playmaking / 100) * 0.05 
                            + (insideDefense / 100) * 0.01
                            + (exteriorDefense / 100) * 0.05 
                            + (defensiveMovement / 100) * 0.05 
                            + (athletic / 100) * 0.05 
                            + (ballMovement / 100) * 0.1))
        
        for i in range(0, GP):
            three_point_attempts, two_point_attempts, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists, steals, blocks, turnovers = generateStats(
                MPG,
                random.uniform(0.0, (20.0 * (0.6 * (outsideScoring / 100) + 0.1 * (ballMovement / 100) + 0.3 * (offensiveMovement / 100)))),  # 3PA
                random.uniform(0.0, (100.0 * (0.4 * insideFinishing / 100) + 0.4 * (insideScoring / 100) + 0.1 * (offensiveMovement / 100) + 0.1 * (athletic * 0.1))),  # 2PA
                random.uniform(0.0, (25.0 * (outsideScoring / 100))),  # FTA
                random.uniform(0.0, (5.0 * (0.5 * (offensiveMovement / 100) + 0.5 * (athletic / 100)))),   # ORB
                random.uniform(0.0, (8.0 * (0.7 * (insideDefense / 100) +  0.1 * (athletic / 100) + 0.2 * (defensiveMovement / 100)))),   # DRB
                random.uniform(0.0, (10.0 * (0.6 * (playmaking / 100) + 0.3 * (offensiveMovement / 100) + 0.1 * (ballMovement / 100)))),  # AST
                random.uniform(0.0, (2.0 * ( 0.7 * (exteriorDefense / 100) + 0.2 * (defensiveMovement / 100) + 0.1 * (athletic / 100)))),   # STL
                random.uniform(0.0, (2.0 * (0.5 * insideDefense / 100) + 0.5 * (height / 100))),   # BLK
                random.uniform(0.0, (4.0 * (100 / ballMovement)))    # TOV
            )
            
            two_point_hit = round(random.uniform(0.25, 1.0) * ((0.05 * (height / 208) + 0.4 * (insideScoring / 100) + 0.4 * (insideFinishing / 100) + 0.05 * (athletic / 100) + 0.1 * (offensiveMovement / 100))) * two_point_attempts)
            three_point_hit = round(random.uniform(0.25, 1.0) * ((0.8 * (outsideScoring / 100) + (0.05 * (height / 208) + 0.15 * (offensiveMovement / 100)))) * three_point_attempts)
            free_throw_hit = round(random.uniform(0.95, ( 1 * (outsideScoring / 100))) * free_throw_attempts)
            
            total_three_point_attempts += three_point_attempts
            total_two_point_attempts += two_point_attempts
            total_free_throw_attempts += free_throw_attempts
            total_offensive_rebounds += offensive_rebounds
            total_defensive_rebounds += defensive_rebounds
            total_assists += assists
            total_steals += steals
            total_blocks += blocks
            total_turnovers += turnovers
            total_two_point_hit += two_point_hit
            total_three_point_hit += three_point_hit
            total_free_throw_hit += free_throw_hit
            
    if POS == "SF":
        height = random.randint(196, 211)
        weight = random.randint(78, 110)
        
        total_three_point_attempts = 0
        total_two_point_attempts = 0
        total_free_throw_attempts = 0
        total_offensive_rebounds = 0
        total_defensive_rebounds = 0
        total_assists = 0
        total_steals = 0
        total_blocks = 0
        total_turnovers = 0
        total_two_point_hit = 0
        total_three_point_hit = 0 
        total_free_throw_hit = 0
        
        insideScoring =     random.randint(45, 99)
        insideFinishing =   random.randint(55, 99)
        offensiveMovement = random.randint(45, 99)
        outsideScoring =    random.randint(45, 99)
        playmaking =        random.randint(25, 99)
        insideDefense =     random.randint(45, 99)
        exteriorDefense =   random.randint(45, 99)
        defensiveMovement = random.randint(55, 99)
        athletic =          random.randint(55, 99)
        ballMovement =      random.randint(25, 99)
        
        overall = round(100 * ((insideScoring / 100) * 0.2
                            + (insideFinishing / 100) * 0.25
                            + (offensiveMovement / 100) * 0.1
                            + (outsideScoring / 100) * 0.1
                            + (playmaking / 100) * 0.05 
                            + (insideDefense / 100) * 0.1
                            + (exteriorDefense / 100) * 0.1 
                            + (defensiveMovement / 100) * 0.05 
                            + (athletic / 100) * 0.15
                            + (ballMovement / 100) * 0.05))
        
        for i in range(0, GP):
            three_point_attempts, two_point_attempts, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists, steals, blocks, turnovers = generateStats(
                MPG,
                random.uniform(0.0, (15.0 * (0.6 * (outsideScoring / 100) + 0.1 * (ballMovement / 100) + 0.3 * (offensiveMovement / 100)))),  # 3PA
                random.uniform(0.0, (120.0 * (0.4 * insideFinishing / 100) + 0.4 * (insideScoring / 100) + 0.1 * (offensiveMovement / 100) + 0.1 * (athletic * 0.1))),  # 2PA
                random.uniform(0.0, (25.0 * (outsideScoring / 100))),  # FTA
                random.uniform(0.0, (15.0 * (0.5 * (offensiveMovement / 100) + 0.5 * (athletic / 100)))),   # ORB
                random.uniform(0.0, (15.0 * (0.7 * (insideDefense / 100) +  0.1 * (athletic / 100) + 0.2 * (defensiveMovement / 100)))),   # DRB
                random.uniform(0.0, (15.0 * (0.6 * (playmaking / 100) + 0.3 * (offensiveMovement / 100) + 0.1 * (ballMovement / 100)))),  # AST
                random.uniform(0.0, (4.0 * ( 0.7 * (exteriorDefense / 100) + 0.2 * (defensiveMovement / 100) + 0.1 * (athletic / 100)))),   # STL
                random.uniform(0.0, (2.0 * (0.5 * insideDefense / 100) + 0.5 * (height / 100))),   # BLK
                random.uniform(0.0, (4.0 * (100 / ballMovement)))    # TOV
            )
            
            two_point_hit = round(random.uniform(0.25, 1.0) * ((0.05 * (height / 211) + 0.4 * (insideScoring / 100) + 0.4 * (insideFinishing / 100) + 0.05 * (athletic / 100) + 0.1 * (offensiveMovement / 100))) * two_point_attempts)
            three_point_hit = round(random.uniform(0.25, 1.0) * ((0.8 * (outsideScoring / 100) + (0.05 * (height / 211) + 0.15 * (offensiveMovement / 100)))) * three_point_attempts)
            free_throw_hit = round(random.uniform(0.95, ( 1 * (outsideScoring / 100))) * free_throw_attempts)
        
            total_three_point_attempts += three_point_attempts
            total_two_point_attempts += two_point_attempts
            total_free_throw_attempts += free_throw_attempts
            total_offensive_rebounds += offensive_rebounds
            total_defensive_rebounds += defensive_rebounds
            total_assists += assists
            total_steals += steals
            total_blocks += blocks
            total_turnovers += turnovers
            total_two_point_hit += two_point_hit
            total_three_point_hit += three_point_hit
            total_free_throw_hit += free_throw_hit
            
    if POS == "PF":
        height = random.randint(203, 216)
        weight = random.randint(90, 120)
        
        total_three_point_attempts = 0
        total_two_point_attempts = 0
        total_free_throw_attempts = 0
        total_offensive_rebounds = 0
        total_defensive_rebounds = 0
        total_assists = 0
        total_steals = 0
        total_blocks = 0
        total_turnovers = 0
        total_two_point_hit = 0
        total_three_point_hit = 0 
        total_free_throw_hit = 0
        
        insideScoring =     random.randint(55, 99)
        insideFinishing =   random.randint(55, 99)
        offensiveMovement = random.randint(35, 99)
        outsideScoring =    random.randint(25, 99)
        playmaking =        random.randint(25, 99)
        insideDefense =     random.randint(55, 99)
        exteriorDefense =   random.randint(25, 99)
        defensiveMovement = random.randint(55, 99)
        athletic =          random.randint(55, 99)
        ballMovement =      random.randint(25, 99)
        
        overall = round(100 * ((insideScoring / 100)    * 0.2
                            + (insideFinishing / 100)   * 0.2
                            + (offensiveMovement / 100) * 0.1
                            + (outsideScoring / 100)    * 0.1
                            + (playmaking / 100)        * 0.05 
                            + (insideDefense / 100)     * 0.2
                            + (exteriorDefense / 100)   * 0.05 
                            + (defensiveMovement / 100) * 0.15 
                            + (athletic / 100)          * 0.05 
                            + (ballMovement / 100)      * 0.05))
        
        for i in range(0, GP):
            three_point_attempts, two_point_attempts, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists, steals, blocks, turnovers = generateStats(
                MPG,
                random.uniform(0.0, (10.0 * (0.6 * (outsideScoring / 100) + 0.1 * (ballMovement / 100) + 0.3 * (offensiveMovement / 100)))),  # 3PA
                random.uniform(0.0, (150.0 * (0.4 * insideFinishing / 100) + 0.4 * (insideScoring / 100) + 0.1 * (offensiveMovement / 100) + 0.1 * (athletic * 0.1))),  # 2PA
                random.uniform(0.0, (20.0 * (outsideScoring / 100))),  # FTA
                random.uniform(0.0, (15.0 * (0.5 * (offensiveMovement / 100) + 0.5 * (athletic / 100)))),   # ORB
                random.uniform(0.0, (15.0 * (0.7 * (insideDefense / 100) +  0.1 * (athletic / 100) + 0.2 * (defensiveMovement / 100)))),   # DRB
                random.uniform(0.0, (10.0 * (0.6 * (playmaking / 100) + 0.3 * (offensiveMovement / 100) + 0.1 * (ballMovement / 100)))),  # AST
                random.uniform(0.0, (2.0 * ( 0.7 * (exteriorDefense / 100) + 0.2 * (defensiveMovement / 100) + 0.1 * (athletic / 100)))),   # STL
                random.uniform(0.0, (2.0 * (0.5 * insideDefense / 100) + 0.5 * (height / 100))),   # BLK
                random.uniform(0.0, (4.0 * (100 / ballMovement)))    # TOV
                )
                
            two_point_hit = round(random.uniform(0.25, 1.0) * ((0.05 * (height / 216) + 0.4 * (insideScoring / 100) + 0.4 * (insideFinishing / 100) + 0.05 * (athletic / 100) + 0.1 * (offensiveMovement / 100))) * two_point_attempts)
            three_point_hit = round(random.uniform(0.25, 1.0) * ((0.8 * (outsideScoring / 100) + (0.05 * (height / 216) + 0.15 * (offensiveMovement / 100)))) * three_point_attempts)
            free_throw_hit = round(random.uniform(0.95, ( 1 * (outsideScoring / 100))) * free_throw_attempts)
            
            total_three_point_attempts += three_point_attempts
            total_two_point_attempts += two_point_attempts
            total_free_throw_attempts += free_throw_attempts
            total_offensive_rebounds += offensive_rebounds
            total_defensive_rebounds += defensive_rebounds
            total_assists += assists
            total_steals += steals
            total_blocks += blocks
            total_turnovers += turnovers
            total_two_point_hit += two_point_hit
            total_three_point_hit += three_point_hit
            total_free_throw_hit += free_throw_hit
            
    if POS == "C":
        height = random.randint(208, 229)
        weight = random.randint(95, 130)
        
        total_three_point_attempts = 0
        total_two_point_attempts = 0
        total_free_throw_attempts = 0
        total_offensive_rebounds = 0
        total_defensive_rebounds = 0
        total_assists = 0
        total_steals = 0
        total_blocks = 0
        total_turnovers = 0
        total_two_point_hit = 0
        total_three_point_hit = 0 
        total_free_throw_hit = 0
        
        insideScoring =     random.randint(75, 99)
        insideFinishing =   random.randint(35, 99)
        offensiveMovement = random.randint(35, 99)
        outsideScoring =    random.randint(25, 99)
        playmaking =        random.randint(25, 99)
        insideDefense =     random.randint(65, 99)
        exteriorDefense =   random.randint(25, 99)
        defensiveMovement = random.randint(55, 99)
        athletic =          random.randint(45, 99)
        ballMovement =      random.randint(25, 99)
        
        overall = round(100 * ((insideScoring / 100)    * 0.3
                            + (insideFinishing / 100)   * 0.1
                            + (offensiveMovement / 100) * 0.05
                            + (outsideScoring / 100)    * 0.1
                            + (playmaking / 100)        * 0.05 
                            + (insideDefense / 100)     * 0.25
                            + (exteriorDefense / 100)   * 0.05 
                            + (defensiveMovement / 100) * 0.1 
                            + (athletic / 100)          * 0.05 
                            + (ballMovement / 100)      * 0.05))
        
        for i in range(0, GP):
            three_point_attempts, two_point_attempts, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists, steals, blocks, turnovers = generateStats(
                MPG,
                random.uniform(0.0, (10.0 * (0.6 * (outsideScoring / 100) + 0.1 * (ballMovement / 100) + 0.3 * (offensiveMovement / 100)))),  # 3PA
                random.uniform(0.0, (150.0 * (0.4 * insideFinishing / 100) + 0.4 * (insideScoring / 100) + 0.1 * (offensiveMovement / 100) + 0.1 * (athletic * 0.1))),  # 2PA
                random.uniform(0.0, (20.0 * (outsideScoring / 100))),  # FTA
                random.uniform(0.0, (10.0 * (0.5 * (offensiveMovement / 100) + 0.5 * (athletic / 100)))),   # ORB
                random.uniform(0.0, (30.0 * (0.7 * (insideDefense / 100) +  0.1 * (athletic / 100) + 0.2 * (defensiveMovement / 100)))),   # DRB
                random.uniform(0.0, (10.0 * (0.6 * (playmaking / 100) + 0.3 * (offensiveMovement / 100) + 0.1 * (ballMovement / 100)))),  # AST
                random.uniform(0.0, (2.0 * ( 0.7 * (exteriorDefense / 100) + 0.2 * (defensiveMovement / 100) + 0.1 * (athletic / 100)))),   # STL
                random.uniform(0.0, (2.0 * (0.5 * insideDefense / 100) + 0.5 * (height / 100))),   # BLK
                random.uniform(0.0, (3.0 * (100 / ballMovement)))    # TOV
                )
                
            two_point_hit = round(random.uniform(0.25, 1.0) * ((0.05 * (height / 229) + 0.4 * (insideScoring / 100) + 0.4 * (insideFinishing / 100) + 0.05 * (athletic / 100) + 0.1 * (offensiveMovement / 100))) * two_point_attempts)
            three_point_hit = round(random.uniform(0.25, 1.0) * ((0.8 * (outsideScoring / 100) + (0.05 * (height / 229) + 0.15 * (offensiveMovement / 100)))) * three_point_attempts)
            free_throw_hit = round(random.uniform(0.95, ( 1 * (outsideScoring / 100))) * free_throw_attempts)
            
            total_three_point_attempts += three_point_attempts
            total_two_point_attempts += two_point_attempts
            total_free_throw_attempts += free_throw_attempts
            total_offensive_rebounds += offensive_rebounds
            total_defensive_rebounds += defensive_rebounds
            total_assists += assists
            total_steals += steals
            total_blocks += blocks
            total_turnovers += turnovers
            total_two_point_hit += two_point_hit
            total_three_point_hit += three_point_hit
            total_free_throw_hit += free_throw_hit
			
    total_three_point_attempts /= GP
    total_two_point_attempts /= GP
    total_free_throw_attempts /= GP
    total_offensive_rebounds /= GP
    total_defensive_rebounds /= GP
    total_assists /= GP
    total_steals /= GP
    total_blocks /= GP
    total_turnovers /= GP
    total_two_point_hit /= GP
    total_three_point_hit /= GP
    total_free_throw_hit /= GP
            
    # Calculate total rebounds
    total_rebounds = round(total_offensive_rebounds + total_defensive_rebounds, 1)
    
    # Calculate field goals (FG) and field goals attempted (FGA)
    FG = round((total_two_point_hit + total_three_point_hit), 1)
    FGA = round(total_two_point_attempts + total_three_point_attempts, 1)
    
    # Calculate field goal percentage (FG%)
    FG_percentage_hit = round((FG / FGA) * 100, 1) if FGA > 0 else 0.0

    # Calculate two-point percentage (2P%)
    two_point_percentage_hit = round((total_two_point_hit / total_two_point_attempts) * 100, 1) if total_two_point_attempts > 0 else 0.0
    
    # Calculate three-point percentage (3P%)
    three_point_percentage_hit = round((total_three_point_hit / total_three_point_attempts) * 100, 1) if total_three_point_attempts > 0 else 0.0
    
    # Calculate free throw percentage (FT%)
    free_throw_percentage_hit = round((total_free_throw_hit / total_free_throw_attempts) * 100, 1) if total_free_throw_attempts > 0 else 0.0

    # Calculate points per game (PPG)
    PPG = round((2 * total_two_point_hit + 3 * total_three_point_hit + total_free_throw_hit), 1)

    # Create and return the formatted string
    result_string = \
                f"Overall: {overall}\n" \
                f"POS: {POS}, Height: {height} cm, Weight: {weight} KG\nGP: {GP: <3}\nMPG: {MPG: <5}\n" \
                f"FG: {FG: <4} ({FGA: <4} FGA), FG%: {FG_percentage_hit: <5}\n" \
                f"2P: {round(total_two_point_hit, 1): <4} ({round(total_two_point_attempts, 1): <4} 2PA), " \
                f"2P%: {two_point_percentage_hit: <5}\n" \
                f"3P: {round(total_three_point_hit, 1): <4} ({round(total_three_point_attempts, 1): <4} 3PA), " \
                f"3P%: {three_point_percentage_hit: <5}\n" \
                f"FT: {round(total_free_throw_hit, 1): <4} ({round(total_free_throw_attempts, 1): <4} FTA), " \
                f"FT%: {free_throw_percentage_hit: <5}\n" \
                f"PPG: {PPG: <5}, " \
                f"AST: {round(assists, 1): <4}, " \
                f"TRB: {total_rebounds: <4}, STL: {round(steals, 1): <4}, " \
                f"BLK: {round(blocks, 1): <4}, TOV: {round(turnovers, 1): <4}, " \
                f"ORB: {round(total_offensive_rebounds, 1): <4}, DRB: {round(total_defensive_rebounds, 1): <4}\n"
    return result_string

# Example usage
generated_player = generatePlayer("PG", 31.0, 72)
print(generated_player)
generated_player = generatePlayer("SG", 31.0, 72)
print(generated_player)
generated_player = generatePlayer("SF", 31.0, 72)
print(generated_player)
generated_player = generatePlayer("PF", 31.0, 72)
print(generated_player)
generated_player = generatePlayer("C", 31.0, 72)
print(generated_player)
