#!/usr/bin/env python3

"""Orthologous protein query"""

import argparse
import pandas as pd
import os
import sys

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("db",help="path to database file",type=str)
parser.add_argument("query1",help="first input accession id",type=str)
parser.add_argument("query2",help="second input accession id",type=str)
args = parser.parse_args()

if not os.path.exists(args.db):
    print(f'Error: database file {args.file} not found')
    sys.exit()

df = pd.read_csv(args.db, sep='\t')

hit1 = df.loc[(df['query'].str.contains(args.query1)) & (df['hit'].str.contains(args.query2))]
hit2 = df.loc[(df['query'].str.contains(args.query2)) & (df['hit'].str.contains(args.query1))]

if hit1.empty:
    print('No hits in database for', args.query1, 'against', args.query2, '\n')
else:
    print('Query:', hit1.iloc[0][0], 'Hit:', hit1.iloc[0][1], 'Evalue:', hit1.iloc[0][2])
    print(f'{hit1.iloc[0][0]} ({hit1.iloc[0][5]}) - {hit1.iloc[0][4]}\n')

if hit2.empty:
    print('No hits in database for', args.query2, 'against', args.query1, '\n')
else:
    print('Query:', hit2.iloc[0][0], 'Hit:', hit2.iloc[0][1], 'Evalue:', hit2.iloc[0][2])
    print(f'{hit2.iloc[0][0]} ({hit2.iloc[0][5]}) - {hit2.iloc[0][4]}\n')


if hit1.empty is False and hit2.empty is False:
    print('Orthologous proteins:', hit1.iloc[0][7] and hit2.iloc[0][7] == True)
