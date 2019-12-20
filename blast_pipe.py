#!/usr/bin/env python3

"""BLAST Pipeline"""

import argparse
import os
import time
import sys

# parse for correct input arguments
parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument(
    "file_1",
    help="first fasta input file",
    type=str
)
parser.add_argument(
    "file_2",
    help="second fasta input file",
    type=str
)
parser.add_argument(
    "out_dir",
    help="output directory",
    type=str
)
args = parser.parse_args()

# setup project directory
if os.path.isdir(args.out_dir):
    print(f'Error: Output directory {args.out_dir} already exists')
    sys.exit()

os.system(f'mkdir {args.out_dir}')

f1 = f'{args.out_dir}/{args.file_1.rsplit(".",1)[0]}'
f2 = f'{args.out_dir}/{args.file_2.rsplit(".",1)[0]}'

# 1. make blast database
ts1=time.time()
print('1. Constructing BLAST database...')
os.system(f'python 1_make_db.py {args.file_1} {f1}')
os.system(f'python 1_make_db.py {args.file_2} {f2}')
print(f'\n   COMPLETE: {time.time() - ts1} seconds elapsed\n')

# 2. blast
ts=time.time()
print('2. BLAST Search...')
os.system(f'python 2_blast.py {args.file_1} {f2}/{args.file_2} {f1}.xml')
os.system(f'python 2_blast.py {args.file_2} {f1}/{args.file_1} {f2}.xml')
print(f'   COMPLETE: {time.time() - ts} seconds elapsed\n')

# 3. parse blast
ts=time.time()
print('3. Parse BLAST Results...')
os.system(f'python 3_parse_blast.py {f1}.xml {f1}.tsv')
os.system(f'python 3_parse_blast.py {f2}.xml {f2}.tsv')
print(f'   COMPLETE: {time.time() - ts} seconds elapsed\n')

# 4 . combine blast
ts=time.time()
print('4. Create BLAST Results Database...')
os.system(f'python 4_combine_blast.py {f1}.tsv {f2}.tsv {args.out_dir}/data.tsv')
print(f'   COMPLETE: {time.time() - ts} seconds elapsed\n')

print(f'Total time elapsed: {time.time() - ts1} seconds')
