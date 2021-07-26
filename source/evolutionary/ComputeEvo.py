
import os
import numpy
from subprocess import Popen, PIPE
from default_config.global_vars import blast_bin, db_loc

'''
computePSSM.py - interfaces with NCBI PSI-BLAST to compute the PSSMs for a given sequence
Adithyan Unni

Created on Tue Jul 13 11:14:10 2021

'''

def computePSSM(seq_file, temp_file_base):
    
    #can't get it to work with Popen for some weird reason - have temporarily fixed this with os.system
    fields = temp_file_base.split("/")[0:-1]
    directory = "/".join(fields) + "/"
    name = seq_file.split('.')[0]
    curr_path = os.getcwd()
#     args = [
#         blast_bin,
#         "-query",
#         seq_file,
#         "-num_iterations 1",
#         "-db",
#         db_loc

#         ]
    
    os.chdir('/tmp')
    os.system(blast_bin + ' ' + '-query' + ' ' + seq_file + ' ' + '-num_iterations 5' + ' ' + '-db' + ' ' + db_loc + ' ' + '-out_ascii_pssm' + ' ' + name + '.out')
    os.chdir(curr_path)
#     p2 = Popen(args, stdout = PIPE, stderr = PIPE, cwd = directory)
#     stdout, stderr = p2.communicate()
    return db_loc
