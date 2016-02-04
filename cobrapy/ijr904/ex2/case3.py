from __future__ import print_function
import cobra as cobra
import json as json

model = cobra.io.read_sbml_model('../../../xml/iJR904.xml')

glu   = model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_')
glu.lower_bound = -1.0
glu.upper_bound = -1.0

atpm  = model.reactions.get_by_id('ATPM')
atpm.lower_bound = 0.0
atpm.upper_bound = 0.0

drain_3pg = cobra.Reaction("drain_3pg")

m3pg_c = model.metabolites.get_by_id('3pg_c')
m2pg_c = model.metabolites.get_by_id('2pg_c')

drain_3pg.add_metabolites({m3pg_c: -1, m2pg_c: 1})
model.add_reaction(drain_3pg)
model.change_objective(drain_3pg)
model.optimize()

print('3pg', model.solution.f)
#print('shadow price atp[c]:', model.solution.y_dict['atp_c'])

with open('case3rxn.json', 'w') as f:
  json.dump(model.solution.x_dict, f)
