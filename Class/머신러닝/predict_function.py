import pandas as pd
import numpy as np
import lightgbm as lgbm
import pickle

def predict_func(df):
    pkl_in = open('./lgb_r.pkl', 'rb')
    lgb_r = pickle.load(pkl_in)

    pred_reg = lgb_r.predict(df)
    pred_reg = pd.Series(pred_reg, index = df.index).rename('reg')

    return pred_reg
