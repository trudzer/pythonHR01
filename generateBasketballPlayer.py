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
        
        insideScoring = random.randint(65, 90)
        insideFinishing = random.randint(75, 95)
        offensiveMovement = random.randint(75, 98)
        outsideScoring = random.randint(70, 95)
        playmaking = random.randint(70, 95)
        insideDefense = random.randint(35, 70)
        exteriorDefense = random.randint(55, 95)
        defensiveMovement = random.randint(45, 90)
        athletic = random.randint(65, 85)
        ballMovement = random.randint(65, 95)
        
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
                random.uniform(0.0, (10.0 * (0.7 * (insideDefense / 100) +  0.1 * (athletic / 100) + 0.2 * (defensiveMovement / 100)))),   # DRB
                random.uniform(0.0, (20.0 * (0.6 * (playmaking / 100) + 0.3 * (offensiveMovement / 100) + 0.1 * (ballMovement / 100)))),  # AST
                random.uniform(0.0, (8.0 * ( 0.7 * (exteriorDefense / 100) + 0.2 * (defensiveMovement / 100) + 0.1 * (athletic / 100)))),   # STL
                random.uniform(0.0, (5.0 * (insideDefense / 100))),   # BLK
                random.uniform(0.0, (4.0 * (100 / ballMovement)))    # TOV
            )
            
            two_point_hit = round(random.uniform(0.15, 0.65) * ((0.05 * (height / 203) + 0.4 * (insideScoring / 100) + 0.4 * (insideFinishing / 100) + 0.05 * (athletic / 100) + 0.1 * (offensiveMovement / 100))) * two_point_attempts)
            three_point_hit = round(random.uniform(0.25, 0.65) * ((0.8 * (outsideScoring / 100) + (0.05 * (height / 203) + 0.15 * (offensiveMovement / 100)))) * three_point_attempts)
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
            
        #print("------------------------------")
        #print(f"Height: {height}\nWeight: {weight}\n\nOutside scoring: {outsideScoring}\nInside scoring: {insideScoring}\nInside finishing: {insideFinishing}\nOffensive movement: {offensiveMovement}")
        #print(f"Inside defense: {insideDefense}\nPlaymaking: {playmaking}\nExterior defense: {exteriorDefense}\nBall movement: {ballMovement}\nAthletic: {athletic}")
        #print(f"Overall: {overall}")
        #print("")
        
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
        
        insideScoring = random.randint(75, 90)
        insideFinishing = random.randint(75, 90)
        offensiveMovement = random.randint(80, 95)
        outsideScoring = random.randint(75, 95)
        playmaking = random.randint(55, 80)
        insideDefense = random.randint(55, 70)
        exteriorDefense = random.randint(65, 95)
        defensiveMovement = random.randint(65, 90)
        athletic = random.randint(65, 85)
        ballMovement = random.randint(65, 95)
        
        overall = round(100 * ((insideScoring / 100) * 0.2 
                            + (insideFinishing / 100) * 0.2
                            + (offensiveMovement / 100) * 0.2 
                            + (outsideScoring / 100) * 0.2 
                            + (playmaking / 100) * 0.05 
                            + (insideDefense / 100) * 0.02 
                            + (exteriorDefense / 100) * 0.05 
                            + (defensiveMovement / 100) * 0.05 
                            + (athletic / 100) * 0.05 
                            + (ballMovement / 100) * 0.1))
        
        for i in range(0, GP):
            three_point_attempts, two_point_attempts, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists, steals, blocks, turnovers = generateStats(
                MPG,
                random.uniform(0.0, (15.0 * (0.6 * (outsideScoring / 100) + 0.1 * (ballMovement / 100) + 0.3 * (offensiveMovement / 100)))),  # 3PA
                random.uniform(0.0, (100.0 * (0.4 * insideFinishing / 100) + 0.4 * (insideScoring / 100) + 0.1 * (offensiveMovement / 100) + 0.1 * (athletic * 0.1))),  # 2PA
                random.uniform(0.0, (25.0 * (outsideScoring / 100))),  # FTA
                random.uniform(0.0, (5.0 * (0.5 * (offensiveMovement / 100) + 0.5 * (athletic / 100)))),   # ORB
                random.uniform(0.0, (10.0 * (0.7 * (insideDefense / 100) +  0.1 * (athletic / 100) + 0.2 * (defensiveMovement / 100)))),   # DRB
                random.uniform(0.0, (20.0 * (0.6 * (playmaking / 100) + 0.3 * (offensiveMovement / 100) + 0.1 * (ballMovement / 100)))),  # AST
                random.uniform(0.0, (8.0 * ( 0.7 * (exteriorDefense / 100) + 0.2 * (defensiveMovement / 100) + 0.1 * (athletic / 100)))),   # STL
                random.uniform(0.0, (5.0 * (insideDefense / 100))),   # BLK
                random.uniform(0.0, (4.0 * (100 / ballMovement)))    # TOV
            )
            
            two_point_hit = round(random.uniform(0.15, 0.65) * ((0.05 * (height / 208) + 0.4 * (insideScoring / 100) + 0.4 * (insideFinishing / 100) + 0.05 * (athletic / 100) + 0.1 * (offensiveMovement / 100))) * two_point_attempts)
            three_point_hit = round(random.uniform(0.25, 0.65) * ((0.8 * (outsideScoring / 100) + (0.05 * (height / 208) + 0.15 * (offensiveMovement / 100)))) * three_point_attempts)
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
        
        for i in range(0, GP):
            three_point_attempts, two_point_attempts, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists, steals, blocks, turnovers = generateStats(
                MPG,
                random.uniform(0.0, 15.0),  # 3PA
                random.uniform(0.0, 30.0),  # 2PA
                random.uniform(0.0, 20.0),  # FTA
                random.uniform(0.0, 5.0),   # ORB
                random.uniform(0.0, 10.0),  # DRB
                random.uniform(0.0, 11.0),  # AST
                random.uniform(0.0, 7.0),   # STL
                random.uniform(0.0, 3.0),   # BLK
                random.uniform(0.0, 6.0)    # TOV
            )
            two_point_hit = random.uniform(0.2, 0.7) * two_point_attempts
            three_point_hit = random.uniform(0.15, 0.55) * three_point_attempts
            free_throw_hit = random.uniform(0.55, 0.9) * free_throw_attempts
        
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
        
        for i in range(0, GP):
            three_point_attempts, two_point_attempts, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists, steals, blocks, turnovers = generateStats(
                MPG,
                random.uniform(0.0, 12.0),   # 3PA
                random.uniform(0.0, 30.0),  # 2PA
                random.uniform(0.0, 20.0),  # FTA
                random.uniform(0.0, 8.0),   # ORB
                random.uniform(0.0, 15.0),  # DRB
                random.uniform(0.0, 11.0),  # AST
                random.uniform(0.0, 4.0),   # STL
                random.uniform(0.0, 3.0),   # BLK
                random.uniform(0.0, 5.0)    # TOV
            )
            two_point_hit = random.uniform(0.3, 0.7) * two_point_attempts
            three_point_hit = random.uniform(0.15, 0.5) * three_point_attempts
            free_throw_hit = random.uniform(0.4, 0.85) * free_throw_attempts
            
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
        
        for i in range(0, GP):
            three_point_attempts, two_point_attempts, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists, steals, blocks, turnovers = generateStats(
                MPG,
                random.uniform(0.0, 10.0),   # 3PA
                random.uniform(0.0, 30.0),  # 2PA
                random.uniform(0.0, 20.0),  # FTA
                random.uniform(0.0, 10.0),  # ORB
                random.uniform(0.0, 25.0),  # DRB
                random.uniform(0.0, 15.0),  # AST
                random.uniform(0.0, 3.0),   # STL
                random.uniform(0.0, 6.0),   # BLK
                random.uniform(0.0, 6.0)    # TOV
            )
            two_point_hit = random.uniform(0.25, 0.85) * two_point_attempts
            three_point_hit = random.uniform(0.15, 0.55) * three_point_attempts
            free_throw_hit = random.uniform(0.5, 0.9) * free_throw_attempts
            
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
    result_string = f"POS: {POS: <5}\nGP: {GP: <3}\nMPG: {MPG: <5}\n" \
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
generated_player = generatePlayer("SG", 38.0, 82)
print(generated_player)
generated_player = generatePlayer("SG", 38.0, 82)
print(generated_player)
generated_player = generatePlayer("SG", 38.0, 82)
print(generated_player)
generated_player = generatePlayer("SG", 38.0, 82)
print(generated_player)
generated_player = generatePlayer("SG", 38.0, 82)
print(generated_player)
