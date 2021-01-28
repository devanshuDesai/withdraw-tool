import re
import pandas as pd

df = pd.read_csv('~/Downloads/DSC_40B_Winter_2021_grades.csv')
NUM_GRADED = 2  # TODO: Find a way to automate this

# Selecting correct columns
detail_cols = ['Name', 'Email']
late_cols = list(filter(lambda x: re.match(r'^[\w\d\s]+ - Lateness.*', x),
                        df.columns))[:NUM_GRADED]
score_cols = list(filter(lambda x: re.match(r'^[\w\d\s]+\d$', x),
                         df.columns))[:NUM_GRADED]
# Note that we're filtering the programming assignments

# Converting columns to timedelta objects
for col in late_cols:
    df[col] = pd.to_timedelta(df[col])

# 1. Counting slip days
late_df = df.loc[:, detail_cols+late_cols]
late_df.loc[:, late_cols] = late_df.loc[:, late_cols].apply(
    lambda col: col.dt.total_seconds() > 0, axis=1)
late_df['slip_days'] = late_df.loc[:, late_cols].apply(
    lambda row: row.sum(), axis=1)
late_df = late_df.loc[:, detail_cols+['slip_days']]
late_df = late_df.sort_values('slip_days', ascending=False)
late_df.to_csv(f'slip_days_{NUM_GRADED}.csv', index=False)

# 2. Consecutive assignments not turned in


def get_consecutive(arr):
    num_missing = 0
    for hw in arr[::-1]:
        if hw:
            num_missing += 1
        else:
            break
    return num_missing


missing_df = df.loc[:, detail_cols+score_cols]
missing_df.loc[:, score_cols] = missing_df.loc[:, score_cols].isnull()
missing_df['missed_assignments'] = missing_df.loc[:,
                                            score_cols].apply(get_consecutive, axis=1)
missing_df = missing_df.loc[:,detail_cols+['missed_assignments']]
missing_df = missing_df.sort_values('missed_assignments', ascending=False)
missing_df.to_csv(f'missing_{NUM_GRADED}.csv', index=False)
