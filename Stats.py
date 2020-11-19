from Main import *
from Function_Stats import *
import numpy as np

# first check types and convert them
merge_df.dtypes
merge_df = merge_df.astype({"predict_goals_home": int, "predict_goals_away": int})
# Games so far
len(merge_df)

# Number of right predicted games
len(merge_df.loc[merge_df["FTR"]== merge_df["BR"]])

# percentage of right predicted games
(len(merge_df.loc[merge_df["FTR"]== merge_df["BR"]])/len(merge_df))

# For a prediction of X - how often was the result like this
## BR = H
H_Prediction_H_Win,H_Prediction_D,H_Prediction_A_Win = right_outcome_per_prediction(df=merge_df,result="H", outcome_close="D", outcome_far="A")
## FTR = D
D_Prediciton_D,D_Prediction_H_Win,D_Prediction_A_Win = right_outcome_per_prediction(df=merge_df,result="D", outcome_close="H", outcome_far="A")
## FTR = A
A_Prediction_A_Win,A_Prediction_D,A_Prediction_H_Win = right_outcome_per_prediction(df=merge_df,result="A", outcome_close="D", outcome_far="H")

# If the result is X - how often was it predicted
## FTR = H
H_Win_H_Prediction,H_Win_D_Prediction,H_Win_A_Prediction = right_prediction_per_outcome(df=merge_df,result="H", outcome_close="D", outcome_far="A")
## FTR = D
D_D_Prediction,D_H_Prediction,D_A_Prediction = right_prediction_per_outcome(df=merge_df,result="D", outcome_close="H", outcome_far="A")
## FTR = A
A_Win_A_Prediction,A_win_D_Prediction,A_Win_H_Prediction = right_prediction_per_outcome(df=merge_df,result="A", outcome_close="D", outcome_far="H")

# Right goal prediction (only works if main was run)
len(merge_df.loc[merge_df["Pred_25"]== merge_df["Result_25"]])
(len(merge_df.loc[merge_df["Pred_25"]== merge_df["Result_25"]])/len(merge_df))

##>2.5 = Y
pred25_over25 = right_outcome_per_prediction(df=merge_df,result="Y", outcome_close="N",
                                                                   outcome_far="N", FulltimeResults="Result_25",
                                                                   PredictionResults="Pred_25", detail=False)
pred25_under25 = 1-pred25_over25

pred_under25_under25 = pred25_over25 = right_outcome_per_prediction(df=merge_df,result="N", outcome_close="Y",
                                                                   outcome_far="Y", FulltimeResults="Result_25",
                                                                   PredictionResults="Pred_25", detail=False)
pred_under25_over25 = 1-pred_under25_under25



