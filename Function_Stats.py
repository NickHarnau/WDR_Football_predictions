import numpy as np

# If Game result is X - how often was it predicted
def right_prediction_per_outcome(df, result, outcome_close, outcome_far, FulltimeResults="FTR", PredictionResults="BR", detail = True):
    df_pre = df.loc[df[FulltimeResults]==result]
    if detail:
        return(len(df_pre.loc[df_pre[PredictionResults]== result])/len(df_pre)), len(df_pre.loc[df_pre[PredictionResults]== outcome_close])/len(df_pre),len(df_pre.loc[df_pre[PredictionResults]== outcome_far])/len(df_pre)
    else:
        return (len(df_pre.loc[df_pre[PredictionResults]== result])/len(df_pre))

# If the prediction is X - how often was the result like that
def right_outcome_per_prediction(df, result, outcome_close, outcome_far, FulltimeResults="FTR", PredictionResults="BR", detail=True):
    df_pre = df.loc[df[PredictionResults]==result]
    if detail:
        return(len(df_pre.loc[df_pre[FulltimeResults]== result])/len(df_pre)), len(df_pre.loc[df_pre[FulltimeResults]== outcome_close])/len(df_pre),len(df_pre.loc[df_pre[FulltimeResults]== outcome_far])/len(df_pre)
    else:
        return (len(df_pre.loc[df_pre[FulltimeResults] == result]) / len(df_pre))

# earnings
def earning(df, standard_bet=True , DoppelteChance=False ):
    if standard_bet:
        df.loc[(df["FTR"] == "H") & (df["BR"] == "H"), "Gewinne_right_pred"] = df["B365H"] - 1
        df.loc[(df["FTR"] == "D") & (df["BR"] == "D"), "Gewinne_right_pred"] = df["B365D"] - 1
        df.loc[(df["FTR"] == "A") & (df["BR"] == "A"), "Gewinne_right_pred"] = df["B365A"] - 1
        df["Gewinne_right_pred"].fillna(-1, inplace=True)

        return df["Gewinne_right_pred"].sum()
    elif DoppelteChance:
        df.loc[(df["percentage_bet_home"] > df["percentage_bet_away"]) & (df["FTR"] != "A"), "Gewinne_Doppelte"] = df["Quote 1x"] - 1
        df.loc[(df["percentage_bet_home"] < df["percentage_bet_away"]) & (df["FTR"] != "H"), "Gewinne_Doppelte"] = df["Quote x2"] - 1
        df["Gewinne_Doppelte"].fillna(-1, inplace=True)

        return df["Gewinne_Doppelte"].sum()

    else:
        # potenzieller Gewinn bei über unter 2,5
        df["Pred_25"] = np.where(df["predict_goals_home"] + df["predict_goals_away"] > 2, "Y", "N")
        df["Result_25"] = np.where(df["FTHG"] + df["FTAG"] > 2, "Y", "N")
        df.loc[(df["Result_25"] == "Y") & (df["Pred_25"] == "Y"), "Gewinne25_right_pred"] = df["B365>2.5"] - 1
        df.loc[(df["Result_25"] == "N") & (df["Pred_25"] == "N"), "Gewinne25_right_pred"] = df["B365<2.5"] - 1
        df["Gewinne25_right_pred"].fillna(-1, inplace=True)

        return df["Gewinne25_right_pred"].sum()








