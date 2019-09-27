import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader

french_companies = pd.read_csv('/Users/tanguy/PycharmProjects/Pepites/csv/Sirene.csv')
print(french_companies.head(5))

# regroup companies to suppress
values_to_search_for = ['MINISTERE', 'SENAT', 'DIRECTION', 'ADMINISTRATION', 'SERVICE', 'POLE', 'UNIVERSITE', \
                        'INSTITUT', 'ECOLE', 'ETABLISSEMENT', 'CHAMBRE', 'CENTRE', 'PREFECTURE', 'COUR D\'APPEL', \
                        'CONSEIL D\'ETAT', 'AGENCE REGIONALE', 'AGENCE NATIONALE', 'DIR DEP', 'ACADEMIE', 'ADAPEI', \
                        'APEI', 'ASSOCIATION', 'CTRE COOP', 'CTRE D\'ACCUEIL', 'CTRE HOSP', 'DEPARTEMENT', 'ASS DEP', \
                        'ASS DEP', 'CAISSE D A', 'ALLOCATIONS FAMILIALES', 'CAISSE PRIMAIRE A', 'CENT H', \
                        'COLLECTIVITE', 'COMITE', 'COMMUNE', 'COMMUNAUTE', 'COMMISSARIAT', 'CAISSE REG', 'REGION', \
                        'GROUPE HOSPITALIER', 'HOPITAL', 'LYCEE', 'REGIE', 'BIBLIOTHEQUE', 'SECURITE SOCIALE', 'CHU', \
                        'UNIV', 'HOPITAUX', 'CLINIQUE', 'VILLE DE PARIS', 'HOSPITAL', 'ETS PUBLIC', 'FONDATION', \
                        'ASSURANCE MALADIE', 'UNION GEST', 'COuR D APPEL', 'CPAM', 'EPSM', 'HOSPICES', \
                        'PAPILLONS BLANCS', 'OFFICE NATIONAL']

pattern = '|'.join(values_to_search_for)
new_df2 = french_companies[~french_companies['denominationUniteLegale'].str.contains(pattern)]
new_df2_sort_by_name = new_df2.sort_values(by=['denominationUniteLegale'])
print(new_df2_sort_by_name)

# companies_name = french_companies.denominationUniteLegale
# print(companies_name.head(5))
# when i will need to create a dataframe with only names of companies

new_df2_sort_by_name.to_csv('/Users/tanguy/PycharmProjects/Pepites/csv/new_csv_file.csv')
# when I will need to save my data into a csv
