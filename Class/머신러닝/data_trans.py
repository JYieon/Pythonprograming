import pandas as pd
import numpy as np
import pickle
import sys

def data_trans(df):
    df.drop(['Customer ID', 'Name', 'Property ID'], axis=1, inplace=True)
    df = df.replace(-999, np.NaN)
    df.drop(('Gender'), axis=1, inplace=True)
    df = df.dropna(subset=['Income (USD)'])
    df['Type of Employment'] = df.apply(lambda x: 'Pensioner' if x['Profession']=='Pensioner' else x['Type of Employment'], axis=1)
    df['Type of Employment'] = df['Type of Employment'].fillna('Unknown')
    df['Income Stability'] = df['Type of Employment'].apply(lambda x: 'High' if x == 'Pensioner' else 'Low')

    pkl_in = open('./info_dict.pkl', 'rb')
    info_dict = pickle.load(pkl_in)

    df['Current Loan Expenses (USD)'] = df['Current Loan Expenses (USD)'].fillna(info_dict['Current Loan Expenses (USD)'])
    df['Dependents'] = df['Dependents'].fillna(info_dict['Dependents'])
    df['Credit Score'] = df['Credit Score'].fillna(info_dict['Credit Score'])

    df['Has Active Credit Card'] = df['Has Active Credit Card'].fillna('Unknown')
    df['Property Location'] = df['Property Location'].fillna('Unknown')
    df = df.dropna()

    df['Loan/Income'] = df['Loan Amount Request (USD)'] / df['Income (USD)']
    df['Loan/Price'] = df['Loan Amount Request (USD)'] / df['Property Price']

    df = df.replace({'N': 0, 'Y': 1})

    obj_list = []
    for i in df.columns:
        if df[i].dtype == 'object':
            obj_list.append(i)

    df = pd.get_dummies(df, columns = obj_list)

    base_df  = pd.DataFrame(columns = info_dict['cols'])
    df = pd.concat([df, base_df]).fillna(0)

    return df