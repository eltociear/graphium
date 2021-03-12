import os
import pandas as pd
from rdkit import Chem

import goli

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(goli.__file__)))
PERIODIC_TABLE_PATH = os.path.join(BASE_PATH, 'data/periodic_table.csv')
PERIODIC_TABLE = pd.read_csv(PERIODIC_TABLE_PATH)
PERIODIC_TABLE = PERIODIC_TABLE.set_index('AtomicNumber')

ATOM_LIST = [
    "C",
    "N",
    "O",
    "S",
    "F",
    "Si",
    "P",
    "Cl",
    "Br",
    "Mg",
    "Na",
    "Ca",
    "Fe",
    "As",
    "Al",
    "I",
    "B",
    "V",
    "K",
    "Tl",
    "Yb",
    "Sb",
    "Sn",
    "Ag",
    "Pd",
    "Co",
    "Se",
    "Ti",
    "Zn",
    "H",
    "Li",
    "Ge",
    "Cu",
    "Au",
    "Ni",
    "Cd",
    "In",
    "Mn",
    "Zr",
    "Cr",
    "Pt",
    "Hg",
    "Pb",
]

ATOM_NUM_H = [0, 1, 2, 3, 4]
VALENCE = [0, 1, 2, 3, 4, 5, 6]
CHARGE_LIST = [-3, -2, -1, 0, 1, 2, 3]
RADICAL_E_LIST = [0, 1, 2]
ATOM_DEGREE_LIST = [0, 1, 2, 3, 4]

HYBRIDIZATION_LIST = [
    Chem.rdchem.HybridizationType.names[k]
    for k in sorted(Chem.rdchem.HybridizationType.names.keys(), reverse=True)
    if k != "OTHER"
]


CHIRALITY_LIST = ["R"]  # alternative is just S


BOND_TYPES = [
    Chem.rdchem.BondType.SINGLE,
    Chem.rdchem.BondType.DOUBLE,
    Chem.rdchem.BondType.TRIPLE,
    Chem.rdchem.BondType.AROMATIC,
]

BOND_STEREO = [Chem.rdchem.BondStereo.STEREONONE,
                Chem.rdchem.BondStereo.STEREOANY,
                Chem.rdchem.BondStereo.STEREOZ,
                Chem.rdchem.BondStereo.STEREOE,
                Chem.rdchem.BondStereo.STEREOCIS,
                Chem.rdchem.BondStereo.STEREOTRANS]
