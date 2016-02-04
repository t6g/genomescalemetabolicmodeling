from __future__ import print_function
import cobra as cobra

model = cobra.io.read_sbml_model('../../../xml/iJO1366.xml')

glu   = model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_')
glu.lower_bound = 0.0 
suc = model.reactions.get_by_id('EX_succ_LPAREN_e_RPAREN_')
suc.lower_bound = -20.0
model.optimize()
growth = model.solution.f
print('growth rate = ', growth)

obj1 = model.reactions.get_by_id('Ec_biomass_iJO1366_core_53p95M')
obj2 = model.reactions.get_by_id('Ec_biomass_iJO1366_WT_53p95M')

obj1.lower_bound = growth
obj1.upper_bound = growth

me1 = model.reactions.get_by_id('ME1')
model.change_objective(me1)

model.optimize()
maximum = model.solution.f
print('maximum ME1 = ', maximum)

model.optimize(objective_sense='minimize')
minimum = model.solution.f
print('minimum ME1 = ', minimum)

