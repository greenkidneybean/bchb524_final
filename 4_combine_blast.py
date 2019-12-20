#!/usr/bin/env python3

"""Combine parsed BLAST output into database"""

import argparse
import os
import pandas as pd
import sys

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("file_1",help="first input file",type=str)
parser.add_argument("file_2",help="second input file",type=str)
parser.add_argument("out",help="output .tsv database file name",type=str)
args = parser.parse_args()

if not os.path.exists(args.file_1):
    print(f'Error: input file {args.file_1} not found')
    sys.exit()
if not os.path.exists(args.file_2):
    print(f'Error: input file {args.file_2} not found')
    sys.exit()

files = [args.file_1, args.file_2]
dfs = [
    pd.read_csv(
    f,
    sep='\t',
    names=['query','hit','evalue', 'score']) for f in files
]
df = pd.concat(dfs)

df['q_desc'] = df['query'].str.split('[').str[0].str.split(' ', 1).str[1]
df['organism'] = df['query'].str.rsplit("[",1).str[1].str[:-1]
df['query'] = df['query'].str.split(' ').str[0]
df['h_desc'] = df['hit'].str.split('[').str[0].str.split(' ',2).str[2]
df['hit'] = df['hit'].str.split(' ').str[1]

mins_df = pd.DataFrame(df.groupby('query')['evalue'].min())
mins_df['min'] = True
df = df.merge(
    mins_df,
    how='left',
    left_on=['query','evalue'],
    right_on=['query','evalue']
)
df.fillna(False, inplace=True)

df = df.sort_values(by=['organism','query','evalue'])
df.reset_index(drop=True, inplace=True)

df.to_csv(args.out, sep='\t', index=False)
