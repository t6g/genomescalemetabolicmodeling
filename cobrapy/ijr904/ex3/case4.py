from __future__ import print_function
import cobra as cobra
from cobra.flux_analysis.parsimonious import optimize_minimal_flux

model           = cobra.io.read_sbml_model('../../../xml/iJR904.xml')

glu             = model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_')
glu.lower_bound = 0.0 
suc = model.reactions.get_by_id('EX_succ_LPAREN_e_RPAREN_')
suc.lower_bound = -20.0
model.optimize()
growth = model.solution.f
print('growth rate = ', growth)

#pFBA_solution = cobra.flux_analysis.optimize_minimal_flux(model)
pFBA_solution = cobra.flux_analysis.parsimonious.optimize_minimal_flux(model)
print('pFBA growth rate = ', pFBA_solution.f)


