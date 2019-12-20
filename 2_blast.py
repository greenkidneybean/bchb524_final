#!/usr/bin/env python3

"""Blast Search"""

import argparse
import os
import sys

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("query",help="query protein fasta file for Blast",type=str)
parser.add_argument("db",help="path to index fasta file for Blast database",type=str)
parser.add_argument("out",help="output .xml file name",type=str)
args = parser.parse_args()

if args.query == args.out:
    print('Error: input and output file names cannot be identical')
    sys.exit()

if not os.path.exists(args.query):
    print(f'Error: input file {args.query} not found')
    sys.exit()

if not os.path.exists(args.db):
    print(f'Error: Blast index file {args.file} not found')
    sys.exit()

os.system(f' \
    blastp -db {args.db} \
    -query {args.query} \
    -outfmt 5 \
    -out {args.out} \
')
