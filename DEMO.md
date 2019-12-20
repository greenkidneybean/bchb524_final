# DEMO GUIDE:

Code review:
- 1_make_db.py        = Make Blast search database
- 2_blast.py          = Blast protein files
- 3_parse_blast.py    = Parse Blast xml files
- 4_combine_blast.py  = Construct final Blast database
- blast_pipe.py       = Pulls scripts 1-4 together

Demo database construction:
```
# raise script help prompt
python blast_pipe.py -h

# construct toy database
python blast_pipe.py drosoph.fasta yeast.fasta test_db
```

Code review: query.py
Demo query script
```
# raise script help prompt
python query.py -h

# try single argument
python query.py data.tsv cheese

# try two false arguments
python query.py data.tsv cheese please

# try non-orthologous proteins (PKR)
python query.py data.tsv NP_001129123	NP_013714

# try orthologous proteins (EIF2S1)
python query.py data.tsv NP_004085 NP_012540
```
