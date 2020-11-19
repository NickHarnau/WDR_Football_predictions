
def fix_syntax_and_types(df):
    df = df.replace({'%': ''}, regex=True)
    df = df.replace({'-': "0"}, regex=True)  # if 0% have bet on a team "-" -> change to 0

    df = df.astype({"predict_goals_home": int, "predict_goals_away": int,"percentage_bet_home": int, "percentage_bet_draw": int, "percentage_bet_away": int})

    return df