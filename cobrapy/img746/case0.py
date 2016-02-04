from __future__ import print_function
import cobra as cobra
import json as json

model = cobra.io.read_sbml_model('../../xml/iMG746.xml')

model.optimize()

print(model.solution.f)

cobra.io.save_json_model(model, "iMG746.json")

with open('case0rxn.json', 'w') as f:
  json.dump(model.solution.x_dict, f)

rxnrates = model.solution.x_dict

for rxn in rxnrates:
  if rxnrates[rxn] < 0.0:
    rxnrates[rxn] = abs(rxnrates[rxn])

with open('case0rxnabs.json', 'w') as f:
  json.dump(rxnrates, f)

ex_rxns = model.reactions.query('EX')
for rxn in ex_rxns:
  if abs(rxn.x) > 1.0e-10:
    print(rxn, '\t\t', rxn.name, '\t\t', rxn.lower_bound, '\t\t', rxn.upper_bound, '\t\t', rxn.x)
