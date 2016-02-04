from __future__ import print_function
import cobra as cobra

flux = -20.0

model           = cobra.io.read_sbml_model('../../../xml/iJO1366.xml')
glu   = model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_')
o2    = model.reactions.get_by_id('EX_o2_LPAREN_e_RPAREN_')
glu.lower_bound = 0.0
o2.lower_bound = -1000.0
ace  = model.reactions.get_by_id('EX_ac_LPAREN_e_RPAREN_')
ace.lower_bound = flux
model.optimize()
growth0 = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('acetate\t\t', growth0, '\t', growth1)

ace.lower_bound = 0.0
o2.lower_bound = -1000.0
acald  = model.reactions.get_by_id('EX_acald_LPAREN_e_RPAREN_')
acald.lower_bound = flux 
model.optimize()
growth0  = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('acetaldehyde\t', growth0, '\t', growth1)

acald.lower_bound = 0.0
o2.lower_bound = -1000.0
ethanol = model.reactions.get_by_id('EX_etoh_LPAREN_e_RPAREN_')
ethanol.lower_bound = flux 
model.optimize()
growth0  = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('ethanol\t\t', growth0, '\t', growth1)

ethanol.lower_bound = 0.0
o2.lower_bound = -1000.0
fru = model.reactions.get_by_id('EX_fru_LPAREN_e_RPAREN_')
fru.lower_bound = flux 
model.optimize()
growth0  = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('D-fructose\t', growth0, '\t\t', growth1)

fru.lower_bound = 0.0
o2.lower_bound = -1000.0
fum = model.reactions.get_by_id('EX_fum_LPAREN_e_RPAREN_')
fum.lower_bound = flux
model.optimize()
growth0  = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('fumarate\t', growth0, '\t', growth1)

fum.lower_bound = 0.0
o2.lower_bound = -1000.0
glu = model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_')
glu.lower_bound = flux
model.optimize()
growth0  = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('D-glucose\t', growth0, '\t\t', growth1)

glu.lower_bound = 0.0
o2.lower_bound = -1000.0
gln = model.reactions.get_by_id('EX_gln_DASH_L_LPAREN_e_RPAREN_')
gln.lower_bound = flux 
model.optimize()
growth0  = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('L-glutamine\t', growth0, '\t\t', growth1)

gln.lower_bound = 0.0
o2.lower_bound = -1000.0
gln = model.reactions.get_by_id('EX_glu_DASH_L_LPAREN_e_RPAREN_')
gln.lower_bound = flux
model.optimize()
growth0  = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('L-glutamate\t', growth0, '\t\t', growth1)

gln.lower_bound = 0.0
o2.lower_bound = -1000.0
lac = model.reactions.get_by_id('EX_lac_DASH_D_LPAREN_e_RPAREN_')
lac.lower_bound = flux
model.optimize()
growth0  = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('D-lactate\t', growth0, '\t', growth1)

lac.lower_bound = 0.0
o2.lower_bound = -1000.0
lac = model.reactions.get_by_id('EX_lac_DASH_L_LPAREN_e_RPAREN_')
lac.lower_bound = flux 
model.optimize()
growth0  = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('L-lactate\t', growth0, '\t', growth1)

lac.lower_bound = 0.0
o2.lower_bound = -1000.0
mal = model.reactions.get_by_id('EX_mal_DASH_L_LPAREN_e_RPAREN_')
mal.lower_bound = flux 
model.optimize()
growth0  = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('L-malate\t', growth0, '\t', growth1)

mal.lower_bound = 0.0
o2.lower_bound = -1000.0
pyr = model.reactions.get_by_id('EX_pyr_LPAREN_e_RPAREN_')
pyr.lower_bound = flux 
model.optimize()
growth0  = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('pyruvate\t', growth0, '\t\t', growth1)

pyr.lower_bound = 0.0
o2.lower_bound = -1000.0
suc = model.reactions.get_by_id('EX_succ_LPAREN_e_RPAREN_')
suc.lower_bound = flux
model.optimize()
growth0  = model.solution.f
o2.lower_bound = 0.0
model.optimize()
growth1  = model.solution.f
print('succinate\t', growth0, '\t', growth1)

