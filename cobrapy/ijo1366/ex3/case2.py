from __future__ import print_function
import cobra as cobra

model = cobra.io.read_sbml_model('../../../xml/iJO1366.xml')

fva0 = cobra.flux_analysis.flux_variability_analysis(model)

print('ME1', fva0['ME1'])
print('ME2', fva0['ME2'])
print('MDH', fva0['MDH'])
