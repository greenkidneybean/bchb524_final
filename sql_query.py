#!/usr/bin/env python3

"""Orthologous protein query"""

import argparse
import csv
import os
import sys
import sqlite3

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("db",help="path to database file",type=str)
parser.add_argument("query1",help="first input accession id",type=str)
parser.add_argument("query2",help="second input accession id",type=str)
args = parser.parse_args()

if not os.path.exists(args.db):
    print(f'Error: database file {args.file} not found')
    sys.exit()

conn = sqlite3.connect(args.db)
c = conn.cursor()

hit1 = None
hit2 = None

try:
    hit1 = c.execute(f'SELECT * FROM DATA WHERE query LIKE "{args.query1}%" AND hit LIKE "{args.query2}%"').fetchall()[0]
    print('Query:', hit1[0], 'Hit:', hit1[1], 'Evalue:', hit1[2])
    print(f'{hit1[0]} ({hit1[5]}) - {hit1[4]}\n')
except IndexError:
    print('No hits in database for', args.query1, 'against', args.query2, '\n')
try:
    hit2 = c.execute(f'SELECT * FROM DATA WHERE query LIKE "{args.query2}%" AND hit LIKE "{args.query1}%"').fetchall()[0]
    print('Query:', hit2[0], 'Hit:', hit2[1], 'Evalue:', hit2[2])
    print(f'{hit2[0]} ({hit2[5]}) - {hit2[4]}\n')
except IndexError:
    print('No hits in database for', args.query2, 'against', args.query1, '\n')

if hit1 and hit2 != None:
    print('Orthologous proteins:', hit1[7] == 1 and hit2[7] == 1)
