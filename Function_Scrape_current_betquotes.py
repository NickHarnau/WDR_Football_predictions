import numpy as np

def calculate_doubleChance(homequote, drawquote, awayquote, df):
    # calculate double chance https://www.reddit.com/r/SoccerBetting/comments/90fd4d/how_to_calculate_double_chance/

    df["Quote 1x"] = 1 / (1 / df[homequote] + 1 / df[drawquote])
    df["Quote x2"] = 1 / (1 / df[awayquote] + 1 / df[drawquote])
    df["Quote 12"] = 1 / (1 / df[awayquote] + 1 / df[homequote])
    df["Quote 1x"] = np.where(df["Quote 1x"] < 1, 1, df["Quote 1x"])
    df["Quote x2"] = np.where(df["Quote x2"] < 1, 1, df["Quote x2"])
    df["Quote 12"] = np.where(df["Quote 12"] < 1, 1, df["Quote 12"])

    return df