import random

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
                random.uniform(0.0, 14.0),  # 3PA
                random.uniform(0.0, 25.0),  # 2PA
                random.uniform(0.0, 15.0),  # FTA
                random.uniform(0.0, 3.0),   # ORB
                random.uniform(0.0, 7.0),   # DRB
                random.uniform(0.0, 20.0),  # AST
                random.uniform(0.0, 5.0),   # STL
                random.uniform(0.0, 1.5),   # BLK
                random.uniform(0.0, 6.0)    # TOV
            )
            two_point_hit = round(random.uniform(0.25, 0.65) * two_point_attempts)
            three_point_hit = round(random.uniform(0.15, 0.55) * three_point_attempts)
            free_throw_hit = round(random.uniform(0.65, 0.95) * free_throw_attempts)
            
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
                random.uniform(0.0, 25.0),  # 2PA
                random.uniform(0.0, 15.0),  # FTA
                random.uniform(0.0, 2.0),   # ORB
                random.uniform(0.0, 8.0),   # DRB
                random.uniform(0.0, 8.0),   # AST
                random.uniform(0.0, 3.0),   # STL
                random.uniform(0.0, 1.5),   # BLK
                random.uniform(0.0, 8.0)    # TOV
            )
            two_point_hit = random.uniform(0.3, 0.75) * two_point_attempts
            three_point_hit = random.uniform(0.2, 0.6) * three_point_attempts
            free_throw_hit = random.uniform(0.7, 1.0) * free_throw_attempts
            
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
                random.uniform(0.0, 11.0),  # 3PA
                random.uniform(0.0, 25.0),  # 2PA
                random.uniform(0.0, 15.0),  # FTA
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
                random.uniform(0.0, 8.0),   # 3PA
                random.uniform(0.0, 25.0),  # 2PA
                random.uniform(0.0, 12.0),  # FTA
                random.uniform(0.0, 8.0),   # ORB
                random.uniform(0.0, 12.0),  # DRB
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
                random.uniform(0.0, 8.0),   # 3PA
                random.uniform(0.0, 20.0),  # 2PA
                random.uniform(0.0, 12.0),  # FTA
                random.uniform(0.0, 7.0),   # ORB
                random.uniform(0.0, 13.0),  # DRB
                random.uniform(0.0, 11.0),  # AST
                random.uniform(0.0, 2.0),   # STL
                random.uniform(0.0, 4.0),   # BLK
                random.uniform(0.0, 4.0)    # TOV
            )
            two_point_hit = random.uniform(0.25, 0.7) * two_point_attempts
            three_point_hit = random.uniform(0.15, 0.5) * three_point_attempts
            free_throw_hit = random.uniform(0.3, 0.85) * free_throw_attempts
            
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
generated_player = generatePlayer("PG", 30.0, 70)
print(generated_player)
generated_player = generatePlayer("SG", 33.2, 66)
print(generated_player)
generated_player = generatePlayer("SF", 25.6, 50)
print(generated_player)
generated_player = generatePlayer("PF", 35.1, 78)
print(generated_player)
generated_player = generatePlayer("C", 38.0, 62)
print(generated_player)
