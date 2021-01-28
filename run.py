import re
import argparse
import pandas as pd

GRADEBOOK_PATH = '~/Downloads/DSC_40B_Winter_2021_grades.csv'
parser = argparse.ArgumentParser()
parser.add_argument('--path', metavar='-p',
                    default=GRADEBOOK_PATH, help='Path to Gradebook')
# TODO: Find a way to automate this
parser.add_argument('--count', metavar='-c', type=int,
                    required=True, help='Number of HWs graded so far')
# TODO: Add functionality to automatically send out emails here
parser.add_argument('--email', action='store_true', help='Only output the emails of the students with non-zero missed assignments (default: output all emails)')
args = parser.parse_args()

df = pd.read_csv(args.path)

# Selecting correct columns
detail_cols = ['Name', 'Email']
late_cols = list(filter(lambda x: re.match(r'^[\w\d\s]+ - Lateness.*', x),
                        df.columns))[:args.count]
score_cols = list(filter(lambda x: re.match(r'^[\w\d\s]+\d$', x),
                         df.columns))[:args.count]
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

# Saving the results
if args.email:
    late_df = late_df[late_df.slip_days > 0]
late_df.to_csv(f'slip_days_{args.count}.csv', index=False)

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
missing_df = missing_df.loc[:, detail_cols+['missed_assignments']]
missing_df = missing_df.sort_values('missed_assignments', ascending=False)

# Saving the results
if args.email:
    missing_df = missing_df[missing_df.missed_assignments > 0]
missing_df.to_csv(f'missing_{args.count}.csv', index=False)
