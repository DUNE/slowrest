# this script takes time indexed conditions data and splits it into one payload for each run number
# it associates all data points that fall into the periods between beginning and ending of each run
# to that run, as well as the last value before the run started and the first value after the run ended

import pandas as pd
import sys


def get_run_time_data_df():
    fn = '/Users/linogerlach/Projects/DUNE/ConditionsHandling/data/runNum-Start-end.csv'
    df = pd.read_csv(fn, sep=';', index_col=0, usecols=[0, 1, 2], names=['runnumber', 'begin', 'end'], header=None, parse_dates=[1,2])
    df = df.sort_index()
    return df
    
def get_time_indexed_conditions_df():
    fn = '/Users/linogerlach/Projects/DUNE/ConditionsHandling/data/database/lifetime/v1.0/new_prm_efieldcorrection.csv'
    df = pd.read_csv(fn, sep=',', index_col=0, usecols=[1, 2, 3, 4], header=0)
    df['timestamp'] = pd.to_datetime(df.index.astype(int) * 1000000000).tz_localize(None)
    return df

df_rn = get_run_time_data_df()
df_lt = get_time_indexed_conditions_df()
df = pd.DataFrame()


for row in df_rn.itertuples():
    run_number = row.Index
    begin = row.begin.tz_localize(None)
    end = row.end.tz_localize(None)
    df_during = df_lt[(df_lt["timestamp"].values > begin)*(df_lt["timestamp"].values < end)]
    df_before = df_lt[df_lt["timestamp"].values < begin].iloc[-1:]
    df_after = df_lt[df_lt["timestamp"].values > end].iloc[:1]
    df = pd.concat([df_before, df_during, df_after])
    print(f'df =\n{df}')

    
print(f'df_lt =\n{df_lt}')
print(f'df_rn =\n{df_rn}')
print(f'df =\n{df}')
