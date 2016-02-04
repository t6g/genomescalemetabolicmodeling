from __future__ import print_function
import cobra as cobra
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

model           = cobra.io.read_sbml_model('../../../xml/iJO1366.xml')
dflux           = 1.0
o2              = model.reactions.get_by_id('EX_o2_LPAREN_e_RPAREN_')
o2_flux         = np.arange(0, 25.0, dflux)
glu             = model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_')
glu_flux        = np.arange(0, 25.0, dflux)
growth_rates    = np.zeros([len(o2_flux), len(glu_flux)])

i = 0
for o2_rate in o2_flux:
  o2.lower_bound = -1.0 * o2_rate
  o2.upper_bound = -1.0 * o2_rate
  j = 0
  print('O2 rate:', o2_rate)
  for glu_rate in glu_flux:
    glu.lower_bound = -1.0 * glu_rate
    glu.upper_bound = -1.0 * glu_rate
    print('Glucose rate:', glu_rate)
    model.optimize()
    growth_rates[i, j] = model.solution.f
    j = j + 1
  i = i + 1

x, y = np.meshgrid(o2_flux, glu_flux)

ax = fig.gca(projection='3d')
ax.plot_surface(x, y, growth_rates)
#plt.contourf(x, y, growth_rates)

#plt.plot(o2_flux, growth_rates, '-ob')
#plt.xlabel('O$_2$ uptake rate (mmol gDW$^{-1}$hour$^{-1}$)')
#plt.ylabel('Growth rate (hour$^{-1}$)')

fig = plt.gcf()
fig.set_size_inches(8, 6)
plt.savefig('case1.pdf')
plt.show()

