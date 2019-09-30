import pandas as pd

french_companies = pd.read_csv('/Users/tanguy/PycharmProjects/Pepites/csv/Sirene.csv')
print(french_companies.head(5))

# regroup companies to suppress
values_to_search_for = ['MINISTERE', 'SENAT', 'DIRECTION', 'ADMINISTRATION', 'SERVICE', 'POLE', 'UNIVERSITE',
                        'INSTITUT', 'ECOLE', 'ETABLISSEMENT', 'CHAMBRE', 'CENTRE', 'PREFECTURE', 'COUR D\'APPEL',
                        'CONSEIL D\'ETAT', 'AGENCE REGIONALE', 'AGENCE NATIONALE', 'DIR DEP', 'ACADEMIE', 'ADAPEI',
                        'APEI', 'ASSOCIATION', 'CTRE COOP', 'CTRE D\'ACCUEIL', 'CTRE HOSP', 'DEPARTEMENT', 'ASS DEP',
                        'ASS DEP', 'CAISSE D A', 'ALLOCATIONS FAMILIALES', 'CAISSE PRIMAIRE A', 'CENT H',
                        'COLLECTIVITE', 'COMITE', 'COMMUNE', 'COMMUNAUTE', 'COMMISSARIAT', 'CAISSE REG', 'REGION',
                        'GROUPE HOSPITALIER', 'HOPITAL', 'LYCEE', 'REGIE', 'BIBLIOTHEQUE', 'SECURITE SOCIALE', 'CHU',
                        'UNIV', 'HOPITAUX', 'CLINIQUE', 'VILLE DE PARIS', 'HOSPITAL', 'ETS PUBLIC', 'FONDATION',
                        'ASSURANCE MALADIE', 'UNION GEST', 'COuR D APPEL', 'CPAM', 'EPSM', 'HOSPICES',
                        'PAPILLONS BLANCS', 'OFFICE NATIONAL', 'ADULTES', 'PERSONNES AGEES', 'CESAME', 'COUR D APPEL',
                        'GROUPEMENT D', 'MUTUALITE FRANCAISE', 'URSSAF', 'ASS DE', 'ASS EN', 'ASS IN', 'ASS MONSIEUR',
                        'ASS POUR', 'ASS REG', 'CH AGGLO', 'CH GENEVIEVE', 'CHS DE', 'LA VIE ACTIVE',
                        'OFFICE FRANCAIS', 'OFFICE HYGIENE', 'TRANSPORTS COMMUNS', 'U R S S A F', 'UNION DES',
                        'VOIES NAVIGABLES', 'CROIX ROUGE', 'GROUPE SOS', 'MAISON DE SANTE']

pattern = '|'.join(values_to_search_for)
new_df2 = french_companies[~french_companies['denominationUniteLegale'].str.contains(pattern)]
new_df2_sort_by_name = new_df2.sort_values(by=['denominationUniteLegale'])
new_df2_sort_by_name.columns = ['SIREN', 'Tranche Effectifs', 'Nom']

print(new_df2_sort_by_name)

# Overwriting column with replaced names
new_df2_sort_by_name['Nom'] = new_df2_sort_by_name['Nom'].replace(regex={'^THALES.+': 'THALES', '^AIRBU.+': 'AIRBUS',
                                                                         '^ALLIANZ.+': 'ALLIANZ', '^ALSTOM.+': 'ALSTOM',
                                                                         '^ALTEN.+': 'ALTEN', '^APAVE.+': 'APAVE',
                                                                         '^ATALIAN.+': 'ATALIAN', '^AUCHAN.+': 'AUCHAN',
                                                                         '^AXA.+': 'AXA', '^BANQUE CIC.+': 'BANQUE CIC',
                                                                         '^BANQUE POP.+': 'BANQUE POPULAIRE',
                                                                         '^BNP.+': 'BNP PARIBAS',
                                                                         '^BOUYGUES BAT.+': 'BOUYGUES BATIMENT',
                                                                         '^BPCE.+': 'BPCE',
                                                                         '^BUREAU VER.+': 'BUREAU VERITAS',
                                                                         '^CA .+': 'CREDIT AGRICOLE',
                                                                         '^CAISSE D\'E.+': 'CAISSE D\'EPARGNE',
                                                                         '^CAISSE EP.+': 'CAISSE D\'EPARGNE',
                                                                         '^CAISSE FED.+': 'CREDIT MUTUEL',
                                                                         '^CARREFOUR.+': 'CARREFOUR',
                                                                         '^COLAS.+': 'COLAS',
                                                                         '^CRCAM.+': 'CREDIT AGRICOLE',
                                                                         '(CREDIT AGRICOLE)': 'CREDIT AGRICOLE',
                                                                         'CRED.+ AGRIC.+': 'CREDIT AGRICOLE',
                                                                         '^CR CREDIT AG.+': 'CREDIT AGRICOLE',
                                                                         '^DERICHEBOURG.+': 'DERICHEBOURG',
                                                                         '^EIFFAGE.+': 'EIFFAGE',
                                                                         '^EURIAL.+': 'EURIAL', '^FEDEX.+': 'FEDEX',
                                                                         '^FEDERAL EXPRESS.+': 'FEDEX', '^GFi.+': 'GFI',
                                                                         '^GIE.+': 'GIE', '^GROUPAMA.+': 'GROUPAMA',
                                                                         '^GSF.+': 'GSF', '^IDEMIA.+': 'IDEMIA',
                                                                         '^KEOLIS.+': 'KEOLIS',
                                                                         '^KUENE.+': 'KUENE NAGEL',
                                                                         '^LAFARGEHOLCIM.+': 'LAFARGE',
                                                                         '^NESTLE.+': 'NESTLE', '^ONET.+': 'ONET',
                                                                         '^PRICEWATER.+': 'PWC',
                                                                         '^RENAULT.+': 'RENAULT',
                                                                         '^SAFRAN.+': 'SAFRAN',
                                                                         '^SAINT GOB.+': 'SAINT GOBAIN',
                                                                         '^SAMSIC.+': 'SAMSIC', '^SANOFI.+': 'SANOFI',
                                                                         '^SCHNEIDER ELEC.+': 'SCHNEIDER ELECTRIC',
                                                                         '^SECURITAS.+': 'SECURITAS',
                                                                         '^SEGULA.+': 'SEGULA', '^SFR.+': 'SFR',
                                                                         '^SNCF.+': 'SFR', '^SODEXO.+': 'SODEXO',
                                                                         '^SPIE.+': 'SPIE',
                                                                         '^STMICRO.+': 'STMICROELECTRONICS',
                                                                         '^TOTAL.+': 'TOTAL', '^UGECAM.+': 'UGECAM',
                                                                         '^VALEO.+': 'VALEO', '^VEOLIA.+': 'VEOLIA',
                                                                         '^ZODIAC.+': 'ZODIAC'})

# Create a dataframe with only names of companies
companies_name = new_df2_sort_by_name.drop(['SIREN', 'Tranche Effectifs'], axis=1)
companies_name = companies_name.drop_duplicates()
print(companies_name.head(5))

# new_df2_sort_by_name.to_csv('/Users/tanguy/PycharmProjects/Pepites/csv/new_csv_file.csv')
# when I will need to save my data but d a into a csv

companies_name.to_csv('/Users/tanguy/PycharmProjects/Pepites/csv/companies.csv')