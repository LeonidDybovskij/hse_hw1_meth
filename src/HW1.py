import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
f1 = open('8_cell.deduplicated.bedGraph', "r")
f2 = open('icm.deduplicated.bedGraph', "r")
f3 = open('epiblast.deduplicated.bedGraph', "r")
eight_cell_list = []
icm_list = []
epiblast_list = []
eight_cell_dict = {}
icm_dict = {}
epiblast_dict = {}
for line in f1.readlines():
    if 'bedGraph' in line:
        pass
    else:
        string = line.split()
        eight_cell_list.append(round(float(string[-1]), 0))
for line in f2.readlines():
    if 'bedGraph' in line:
        pass
    else:
        string = line.split()
        icm_list.append(round(float(string[-1]), 0))
for line in f3.readlines():
    if 'bedGraph' in line:
        pass
    else:
        string = line.split()
        epiblast_list.append(round(float(string[-1]), 0))
eight_cell = pd.DataFrame({"eight_cell": eight_cell_list})
icm = pd.DataFrame({"icm": icm_list})
epiblast = pd.DataFrame({"epiblast": epiblast_list})
# sns.histplot(data=eight_cell, x='eight_cell', kde=True, palette="Oranges_r")
# sns.histplot(data=icm, x='icm', kde=True, palette="Oranges_r")
sns.histplot(data=epiblast, x='epiblast', kde=True, palette="Oranges_r")
plt.tight_layout()
plt.savefig('hw1_epiblast.png', dpi=300)
