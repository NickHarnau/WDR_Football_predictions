from ML_Versuche import *
from Scrap_current_Community_Bets import *
from Scrape_current_betquotes import *
from Main_function import *
from Function_Stats import *

df_crowd_prediction = scrape_current_community_bets(link="https://allegegenpistor.wdr2.de/tipptrend.php?spieltag=") # function from Scrap_current_Community_Bets
df_quotes_result = current_betquotes() # function from Scrape_current_betquotes

# bring both df together over Home and Away team

# get team names from df_quotes_result
Mannschaftsnamen_1 = df_quotes_result.HomeTeam.unique()
# unfortunatels th dfs are in different order - make a list manuel fitting to Mannschaftsname_1 to get the right order
Mannschaftsnamen_2 = ["FC Bayern München", "Eintracht Frankfurt", "1. FC Köln", "VfB Stuttgart"
                      , "1. FC Union Berlin", "Werder Bremen", "Borussia Dortmund", "RB Leipzig"
                      , "VfL Wolfsburg", "Hertha BSC", "FC Augsburg", "Arminia Bielefeld"
                      , "Bayer 04 Leverkusen", "1. FSV Mainz 05", "Borussia Mönchengladbach"
                      , "FC Schalke 04", "TSG 1899 Hoffenheim", "SC Freiburg"]

# fit team names in df_quotes_result
df_quotes_result = df_quotes_result.replace(dict(zip(Mannschaftsnamen_1, Mannschaftsnamen_2)))

# merge by HT and AT (the combination only once a season)
merge_df = pd.merge(df_crowd_prediction,df_quotes_result, how="left",
                    left_on=["home_team","away_team"], right_on=["HomeTeam", "AwayTeam"])

#fit syntax und types
merge_df = fix_syntax_and_types(merge_df) # function in Main_function

# potencial wins
earning_Predictions = earning(df=merge_df) # favorites
earning_Predictions25 = earning(df=merge_df, standard_bet=False) # over 2,5
earning_Predictions_Doppelte = earning(df=merge_df, standard_bet=False, DoppelteChance=True) # 1x / x2

## more Statistics in Stats

# ML
dict_wins = ML_try(df=merge_df, test_size=0.33, state=18112020, target="FTR", X=["percentage_bet_home", "percentage_bet_draw", "percentage_bet_away"])# more possibilities "B365H","B365D","B365A"


