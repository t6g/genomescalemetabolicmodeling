from __future__ import print_function
import cobra as cobra
import matplotlib.pyplot as plt

"""
simulate gene knockouts: double gene deletion
"""

model = cobra.io.read_sbml_model('../../../xml/iJO1366.xml')
res   = cobra.flux_analysis.double_deletion(model, element_type='reaction')

cs = plt.contourf(res['data'])
cb = plt.colorbar(cs)
plt.xlabel('Reaction knockout 1')
plt.ylabel('Reaction knockout 2')

fig = plt.gcf()
fig.set_size_inches(8, 6)
plt.savefig('case3.pdf')
plt.show()

