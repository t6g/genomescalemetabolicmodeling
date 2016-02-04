from __future__ import print_function
import cobra as cobra

"""
simulate gene knockouts: single gene deletion
"""

model                = cobra.io.read_sbml_model('../../../xml/iJO1366.xml')
growth_rates, status = cobra.flux_analysis.single_deletion(model)

for i in growth_rates.iteritems():
  print(i)
