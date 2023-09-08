import pandas as pd

from InterpretHeaders import interpretHeaders

path = "C:\\Users\\karal\\OneDrive\\Υπολογιστής\\clinical-abbreviations-1.0.2\\clinical-abbreviations-1.0.2" \
       "\\metainventory\\Metainventory_Version1.0.0.csv"

inputDataset = "resources\\Data_test_Encrypt_Repaired.csv"

headers = pd.read_csv(inputDataset, delimiter=";").columns.to_list()

interpretHeaders(headers, path)

"""
md = MedicalDictionary(dictionaryCSVPath=path)
for h in headers:
       md.generateAllPossibleCandidates(h)
       print('\n=================================\n')
"""



