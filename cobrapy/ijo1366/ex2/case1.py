from __future__ import print_function
import cobra as cobra

model = cobra.io.read_sbml_model('../../../xml/iJO1366.xml')

glu   = model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_')
glu.lower_bound = -1.0
glu.upper_bound = -1.0

atpm  = model.reactions.get_by_id('ATPM')
atpm.lower_bound = 0.0
atpm.upper_bound = 0.0

nadh_drain = cobra.Reaction("NADH_drain")
nadh_drain.add_metabolites({model.metabolites.nadh_c: -1,
                            model.metabolites.nad_c: 1, model.metabolites.h_c: 1})
model.add_reaction(nadh_drain)
model.change_objective(nadh_drain)
model.optimize()
print('NADH', model.solution.f)
print('shadow price h[c]:', model.solution.y_dict['h_c'])
print('shadow price atp[c]:', model.solution.y_dict['atp_c'])

