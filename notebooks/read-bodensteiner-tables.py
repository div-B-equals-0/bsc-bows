# ---
# jupyter:
#   jupytext_format_version: '1.2'
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.3
# ---

import numpy as np
from astropy.table import Table
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


VIZIER = "http://cdsarc.u-strasbg.fr/ftp/J/A+A/618/A110"
tab01 = Table.read(f"{VIZIER}/tableb1.dat", readme=f"{VIZIER}/ReadMe", format="ascii.cds")

tab01

tab02 = Table.read(f"{VIZIER}/tableb2.dat", readme=f"{VIZIER}/ReadMe", format="ascii.cds")

tab02

# Select bows around B dwarfs

mask = np.array(['bs' in s for s in tab02['MClass']]) & np.array([s.startswith("B") for s in tab01['SpType']]) & np.array([not 'I' in s for s in tab01['SpType']])

mask.sum()

tab02[mask]

tab01[mask]

mask.sum()

tab02[mask].to_pandas()

tab01[mask].to_pandas()


