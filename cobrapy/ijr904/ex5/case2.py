from __future__ import print_function
import cobra as cobra
import numpy as np
import matplotlib.pyplot as plt
from cobra.flux_analysis.phenotype_phase_plane import calculate_phenotype_phase_plane
#import pickle as pickle

model   = cobra.io.read_sbml_model('../../../xml/iJR904.xml')
results = cobra.flux_analysis.phenotype_phase_plane.calculate_phenotype_phase_plane(model, 'EX_o2_LPAREN_e_RPAREN_', 'EX_glc_LPAREN_e_RPAREN_', n_processes=12)

results.plot()

#outfile = open('case2.pickle', 'w')
#pickle.dump(results, outfile)

fig = plt.gcf()
fig.set_size_inches(8, 6)
plt.savefig('case2.pdf')
plt.show()

