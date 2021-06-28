#!/usr/bin/python
import Bio
from Bio.PDB import * 
import importlib
import os, sys

from default_config.masif_opts import masif_opts
# Local includes
from input_output.protonate import protonate

if len(sys.argv) <= 1: 
    print("Usage: "+sys.argv[0]+" PDBID_A_B")
    print("A or B are the chains to include in this pdb.")
    sys.exit(1)

if not os.path.exists(masif_opts['raw_pdb_dir']):
    os.makedirs(masif_opts['raw_pdb_dir'])

if not os.path.exists(masif_opts['tmp_dir']):
    os.mkdir(masif_opts['tmp_dir'])

# Download pdb
if sys.argv[1] in ['-f', '--file', '-file']:
    pdb_filename = sys.argv[2]
    pdb_id, _ = os.path.splitext(pdb_filename.split('/')[-1])
else:
    in_fields = sys.argv[1].split('_')
    pdb_id = in_fields[0]

    pdbl = PDBList(server='http://ftp.wwpdb.org')
    pdb_filename = pdbl.retrieve_pdb_file(pdb_id, pdir=masif_opts['tmp_dir'],file_format='pdb')

##### Protonate with reduce, if hydrogens included.
# - Always protonate as this is useful for charges. If necessary ignore hydrogens later.
protonated_file = masif_opts['raw_pdb_dir']+"/"+pdb_id+".pdb"
protonate(pdb_filename, protonated_file)
print('hecho')
pdb_filename = protonated_file

