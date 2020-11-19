import pandas as pd
from Function_Scrape_current_betquotes import *
""" https://www.football-data.co.uk/germanym.php
    link for bet quote scrape - results also inside
"""

def current_betquotes():

    df_quotes_result = pd.read_csv("https://www.football-data.co.uk/mmz4281/2021/D1.csv")
    # keep only relevant columns
    df_quotes_result = df_quotes_result[["HomeTeam", "AwayTeam"
                                         ,"FTHG", "FTAG", "FTR"
                                         ,"B365H", "B365D", "B365A"
                                         ,"B365>2.5", "B365<2.5"]]
    df_quotes_result = calculate_doubleChance("B365H", "B365D", "B365A", df_quotes_result)

    return df_quotes_result