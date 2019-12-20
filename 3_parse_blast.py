#!/usr/bin/env python3

"""Parse BLAST Output"""

import argparse
from Bio.Blast import NCBIXML
import csv
import sys

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("file",help="blast.xml results file to be parsed",type=str)
parser.add_argument("out",help="output .tsv file name",type=str)
args = parser.parse_args()

if args.file == args.out:
    print('Error: input and output file names cannot be identical')
    sys.exit()

try:
    with open(args.file) as handle, open(args.out, 'w', newline='') as tsvout:
        writer = csv.writer(tsvout, delimiter='\t')
        for blast_result in NCBIXML.parse(handle):
            q = blast_result.query
            for desc in blast_result.descriptions:
                hit = desc.title
                e = desc.e
                score = desc.score
                writer.writerow([q, hit, e, score])
except IOError:
    print(f'Error: Input file "{args.file}" not found')
except ValueError:
    print('Error: Input file did not start with "<?xml"')
