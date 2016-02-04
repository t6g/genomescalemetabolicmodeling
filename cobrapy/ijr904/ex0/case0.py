from __future__ import print_function
import cobra as cobra
import json as json

model           = cobra.io.read_sbml_model('../../../xml/iJR904.xml')

glu             = model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_')
glu.lower_bound = -18.5
model.optimize()
print('glucose >= -18.5, aerobic growth rate = ', model.solution.f, '1/hr')
print('glucose flux = ', model.solution.x_dict['EX_glc_LPAREN_e_RPAREN_'])
print('glucose shadow price = ', model.solution.y_dict['glc_DASH_D_e'])
print('O2 flux = ', model.solution.x_dict['EX_o2_LPAREN_e_RPAREN_'])
print('O2 shadow price  = ', model.solution.y_dict['o2_e'])
print('ATPM flux = ', model.solution.x_dict['ATPM'])
print('ATP flux ATPPRT = ', model.solution.x_dict['ATPPRT'])
print('ATP shadow price  = ', model.solution.y_dict['atp_c'])

with open('case0rxn.json', 'w') as f:
  json.dump(model.solution.x_dict, f)
