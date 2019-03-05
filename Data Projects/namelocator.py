import nltk
import numpy as np
import pandas as pd
import os

# Import the list of names by state
fpath = os.getcwd() + "/Data Projects/namesbystate/"
nameFiles = os.listdir(fpath)

stateDFs = []
for nf in nameFiles:
    state = nf.split(".")[0]
    with open(fpath + nf) as namesFile:
        stateDFs.append(pd.read_table(namesFile, sep=",", names=["State","Gender","Year","Name","Count"]))

names = pd.concat(stateDFs)

print(names.size)
    