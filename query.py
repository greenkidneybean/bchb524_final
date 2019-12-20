#!/usr/bin/env python3

"""Orthologous protein query"""

import argparse
import csv
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

hit1 = None
hit2 = None

with open(args.db) as tsv:
    for line in csv.reader(tsv, delimiter="\t"):
        if args.query1 in line[0] and args.query2 in line[1]:
            hit1 = line
        elif args.query2 in line[0] and args.query1 in line[1]:
            hit2 = line

try:
    print('Query:', hit1[0], 'Hit:', hit1[1], 'Evalue:', hit1[2])
    print(f'{hit1[0]} ({hit1[5]}) - {hit1[4]}\n')
except TypeError:
    print('No hits in database for', args.query1, 'against', args.query2, '\n')

try:
    print('Query:', hit2[0], 'Hit:', hit2[1], 'Evalue:', hit1[2])
    print(f'{hit2[0]} ({hit2[5]}) - {hit2[4]}\n')
except TypeError:
    print('No hits in database for', args.query2, 'against', args.query1, '\n')

if hit1 and hit2 != None:
    print('Orthologous proteins:', hit1[7] and hit2[7] == 'True')
