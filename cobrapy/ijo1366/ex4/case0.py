from __future__ import print_function
import cobra as cobra
import numpy as np
import matplotlib.pyplot as plt

model           = cobra.io.read_sbml_model('../../../xml/iJO1366.xml')
o2              = model.reactions.get_by_id('EX_o2_LPAREN_e_RPAREN_')
o2.lower_bound  = -17.0
o2.upper_bound  = -17.0
glu             = model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_')
glu_flux        = np.arange(0, 20.0, 0.25)
growth_rates    = np.zeros_like(glu_flux)

i = 0
for take_rate in glu_flux:
  glu.lower_bound = -1.0 * take_rate
  model.optimize()
  growth_rates[i] = model.solution.f
  i = i + 1

plt.plot(glu_flux, growth_rates, '-ob')
plt.xlabel('Glucose uptake rate (mmol gDW$^{-1}$hour$^{-1}$)')
plt.ylabel('Growth rate (hour$^{-1}$)')

fig = plt.gcf()
fig.set_size_inches(8, 6)
plt.savefig('case0.pdf')
plt.show()

