# File created by JT Wilcox 
# sources
# https://www.scaler.com/topics/pandas/how-to-install-pandas-in-python/
# https://automatetheboringstuff.com/
# https://www.activestate.com/blog/how-to-predict-nfl-winners-with-python/

# # import libraries
import os
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression


from sportsreference.nfl.boxscore import Boxscores, Boxscore
from sportsreference.nfl.teams import Teams
Boxscores(1,2022).games
season = 2022
master_array = []
season_team_list = Teams(str(season))
for team in season_team_list: 
            team_schedule = team.schedule
            for game in team_schedule:
               boxscore = game.boxscore_index
               master_array.append([str(season),team.name,boxscore])

# Week 1 
game_str = Boxscores(1,2022).games['1-2022'][0]['boxscore']
game_stats = Boxscore(game_str)
game_stats.dataframe


away_name = "New England Patriots"
away_abbr = "NE"
away_score = 7
home_name = "Miami Dolphins"
home_abbr = "MIA"
home_score = 20
winning_name = "Miami Dolphins"
winning_abbr = "MIA"
losing_name = "New England Patriots"
losing_abbr =  "NE"
    # {‘boxscore’: ‘20200913buf’,

# Week 2
away_name = "Miami Dolphins"
away_abbr = "MIA"
away_score = 42
home_name = "Baltimore Ravens"
home_abbr = "BAL"
home_score = 38
winning_name = "Miami Dolphins"
winning_abbr = "MIA"
losing_name = "Baltimore Ravens"
losing_abbr = "BAL"

# Week 3
away_name = "Buffalo Bills"
away_abbr = "BUF"
away_score = 19
home_name = "Miami Dolphins"
home_abbr = "MIA"
home_score = 21
winning_name = "Miami Dolphins"
winning_abbr = "MIA"
losing_name = "Buffalo Bills"
losing_abbr = "BUF"

# Week 4
away_name = "Miami Dolphins"
away_abbr = "MIA"
away_score = 15
home_name = "Cincinnati Bengals"
home_abbr = "CIN"
home_score = 27
winning_name = "Cincinnati Bengals"
winning_abbr ="CIN"
losing_name = "Miami Dolphins"
losing_abbr = "MIA"

# week 5
away_name = "Miami Dolphins"
away_abbr = "MIA"
away_score = 17
home_name = "New York Jets"
home_abbr = "NYJ"
home_score = 40
winning_name = "New York Jets"
winning_abbr ="NYJ"
losing_name = "Miami Dolphins"
losing_abbr = "MIA"

# week 6
home_name = "Miami Dolphins"
home_abbr = "MIA"
home_score = 16
away_name = "Minnesota Vikings"
away_abbr = "MIN"
away_score = 24
winning_name = "Minnesota Vikings"
winning_abbr ="MIN"
losing_name = "Miami Dolphins"
losing_abbr = "MIA"

# week 7
home_name = "Miami Dolphins"
home_abbr = "MIA"
home_score = 16
away_name = "Pittsburg Steelers"
away_abbr = "PIT"
away_score = 10
winning_name = "Miami Dolphins"
winning_abbr ="MIA"
losing_name = "Pittsburg Steelers"
losing_abbr = "PIT"

# week 8
away_name = "Miami Dolphins"
away_abbr = "MIA"
away_score = 31
home_name = "Detroit Lions"
home_abbr = "DET"
home_score = 27
winning_name = "Miami Dolphins"
winning_abbr ="MIA"
losing_name = "Detroit Lions"
losing_abbr = "DET"

# week 9
away_name = "Miami Dolphins"
away_abbr = "MIA"
away_score = 35
home_name = "Chicago Bears"
home_abbr = "CHI"
home_score = 32
winning_name = "Miami Dolphins"
winning_abbr ="MIA"
losing_name = "Chicago Bears"
losing_abbr = "CHI"

# week 10
home_name = "Miami Dolphins"
home_abbr = "MIA"
home_score = 39
away_name = "Cleveland Browns"
away_abbr = "CLE"
away_score = 17
winning_name = "Miami Dolphins"
winning_abbr ="MIA"
losing_name = "Cleveland Browns"
losing_abbr = "CLE"

# week 11
# bye

# week 12
home_name = "Miami Dolphins"
home_abbr = "MIA"
home_score = 30
away_name = "Houston Texans"
away_abbr = "HOU"
away_score = 15
winning_name = "Miami Dolphins"
winning_abbr ="MIA"
losing_name = "Houston Texans"
losing_abbr = "HOU"

# week 13
away_name = "Miami Dolphins"
away_abbr = "MIA"
away_score = 17
home_name = "San Francisco 49ers"
home_abbr = "SF"
home_score = 33
winning_name = "San Franciso 49ers"
winning_abbr ="SF"
losing_name = "Miami Dolphins"
losing_abbr = "MIA"

# week 14
away_name = "Miami Dolphins"
away_abbr = "MIA"
away_score = 17
home_name = "Los Angeles Chargers"
home_abbr = "LAC"
home_score = 23
winning_name = "Los Angeles Chargers"
winning_abbr ="LAC"
losing_name = "Miami Dolphins"
losing_abbr = "MIA"

# week 15
away_name = "Miami Dolphins"
away_abbr = "MIA"
away_score = 29
home_name = "Buffalo Bills"
home_abbr = "BUF"
home_score = 32
winning_name = "Buffalo Bills"
winning_abbr ="BUF"
losing_name = "Miami Dolphins"
losing_abbr = "MIA"

# week 16
home_name = "Miami Dolphins"
home_abbr = "MIA"
home_score = 20
away_name = "Green Bay Packers"
away_abbr = "GB"
away_score = 26
winning_name = "Green Bay Packers"
winning_abbr ="GB"
losing_name = "Miami Dolphins"
losing_abbr = "MIA"

# week 17
away_name = "Miami Dolphins"
away_abbr = "MIA"
away_score = 21
home_name = "New England Patriots"
home_abbr = "NE"
home_score = 23
winning_name = "New England Patriots"
winning_abbr ="NE"
losing_name = "Miami Dolphins"
losing_abbr = "MIA"

# week 18
home_name = "Miami Dolphins"
home_abbr = "MIA"
home_score = 11
away_name = "New York Jets"
away_abbr = "NYJ"
away_score = 6
winning_name = "Miami Dolphins"
winning_abbr ="MIA"
losing_name = "New York Jets"
losing_abbr = "NYJ"

# wild card round
away_name = "Miami Dolphins"
away_abbr = "MIA"
away_score = 31
home_name = "Buffalo Bills"
home_abbr = "BUF"
home_score = 34
winning_name = "Buffalo Bills"
winning_abbr ="BUF"
losing_name = "Miami Dolphins"
losing_abbr = "MIA"




def get_schedule(year):
    weeks = list(range(1,18))
    schedule_df = pd.DataFrame()
    for w in range(len(weeks)):
        date_string = str(weeks)

