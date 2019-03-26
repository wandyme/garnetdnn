import os
from collections import Counter

import numpy as np
from monty.serialization import loadfn
from pymatgen import Composition
from pymatgen.core.periodic_table import get_el_sp

from garnetdnn.util import spe2form
from pymatgen import MPRester

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data") #(wandy) To find the path of this script
print(DATA_DIR)
