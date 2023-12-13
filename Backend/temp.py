import pandas as pd
import numpy as np

inv = pd.read_csv('final_data/inv.csv')
pnrb = pd.read_csv('final_data/pnrb.csv')
sch = pd.read_csv('final_data/sch.csv')


def remove_last_two_chars(s):
    return s[:-2]
inv['Dep_Key'] = inv['Dep_Key'].astype(str)
inv['Dep_Key'] = inv['Dep_Key'].apply(remove_last_two_chars)

print(len(pnrb[~pnrb['DEP_KEY'].isin(inv['Dep_Key'])]))