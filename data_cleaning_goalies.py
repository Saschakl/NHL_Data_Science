import os
import glob
import pandas as pd

df_all = pd.read_csv("./raw_data/goalies_2021_240920221718.csv")

for column_headers in df_all.columns: 
    print(column_headers)
    
#df = df.drop(columns=['xRebounds', 'xGoals','unblocked_shot_attempts','flurryAdjustedxGoals', 'xFreeze', 'freeze', 'ongoal', 'xPlayStopped', 'playStopped', 'xPlayContinuedInZone', 'playContinuedInZone', 'xPlayContinuedOutsideZone', 'playContinuedOutsideZone', 'lowDangerxGoals', 'mediumDangerxGoals', 'highDangerxGoals', 'penalties', 'unblocked_shot_attempts', 'blocked_shot_attempts'])

df_goalies = df_all[['playerId','season', 'name', 'team', 'position', 'situation', 'games_played', 'icetime', 'goals', 'xGoals', 'rebounds', 'xRebounds', 'ongoal', 'xOnGoal', 'lowDangerShots', 'mediumDangerShots', 'highDangerShots', 'lowDangerxGoals', 'mediumDangerxGoals', 'highDangerxGoals', 'lowDangerGoals', 'mediumDangerGoals', 'highDangerGoals', 'penalityMinutes']]

result = df_goalies.head(10)
print(result)