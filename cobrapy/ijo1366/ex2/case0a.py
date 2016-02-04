from __future__ import print_function
import cobra as cobra

model = cobra.io.read_sbml_model('../../../xml/iJO1366.xml')
glu   = model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_')
glu.lower_bound = -1.0
glu.upper_bound = -1.0
atpm  = model.reactions.get_by_id('ATPM')
atpm.lower_bound = 0.0
o2    = model.reactions.get_by_id('EX_o2_LPAREN_e_RPAREN_')
o2.lower_bound = -0.0
model.change_objective(atpm)
model.optimize()
print('glucose = 1.0, ATPM optimal', model.solution.f)
print('shadow price h[c]:', model.solution.y_dict['h_c'])
print('shadow price atp[c]:', model.solution.y_dict['atp_c'])


