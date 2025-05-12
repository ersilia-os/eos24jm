# imports
import os
import csv
import sys
import pickle
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs
import numpy as np

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model

def mol2fp(mol, radius = 3):
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius = radius)
    array = np.zeros((1,))
    DataStructs.ConvertToNumpyArray(fp, array)
    return array

def compute_ECFP6(smiles):
    mols = [Chem.MolFromSmiles(i) for i in smiles]
    arr = np.empty((0,2048), int).astype(int)
    for i in mols:
        fp = mol2fp(i)
        arr = np.vstack((arr, fp))
    return arr

def build_model(smiles): 
    input_data=compute_ECFP6(smiles)
    load_model = pickle.load(open(os.path.join(root,"../..", "checkpoints", 'app.pkl'), 'rb'))
    prediction = load_model.predict(input_data)
    return prediction

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = build_model(smiles_list)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["class"])  # header
    for o in outputs:
        writer.writerow([int(o)])