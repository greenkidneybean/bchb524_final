#!/usr/bin/env python3

"""Make local Blast database"""

import argparse
import os
import sys

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("file", help="input protein fasta file for BLAST database", type=str)
parser.add_argument("out", help="output directory name", type=str)
args = parser.parse_args()

if not os.path.exists(args.file):
    print(f'Error: input file {args.file} not found')
    sys.exit()

os.system(f'mkdir {args.out}')
os.system(f'cp {args.file} {args.out}/')
os.system(f'makeblastdb -in {args.out}/{args.file} -dbtype prot')
