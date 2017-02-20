# This function returns the MIMIC-III data as a dictionary of pandas data sets


import pandas as pd
import os.path


def load_MIMIC_to_pandas(CSV_Folder_Location = '/data/', CSV_List = None):
    MIMIC_df = {}


    # If the user doesn't tell us what tables to load, we load all the tables.
    # Note that some of the tables are very large, so you may need 50+ GB of memory to load them.
    if CSV_List is None:
        CSV_List = [    'ADMISSIONS', # 12 MB
                        'CALLOUT', # 6.1 MB
                        'CAREGIVERS', # 199 KB
                        'CHARTEVENTS', # 33 GB ------BIG!!!
                        'CPTEVENTS', # 56 MB
                        'DATETIMEEVENTS', # 502 MB
                        'DIAGNOSES_ICD', # 19 MB
                        'DRGCODES', # 11 MB
                        'D_CPT', # 14 KB
                        'D_ICD_DIAGNOSES', # 1.4 KB 
                        'D_ICD_PROCEDURES', # 305 KB
                        'D_ITEMS', # 933 KB
                        'D_LABITEMS', # 43 KB
                        'ICUSTAYS', # 6.1 MB
                        'INPUTEVENTS_CV', # 2.3 GB ------BIG!!!
                        'INPUTEVENTS_MV', # 931 MB
                        'LABEVENTS', # 1.8GB ------BIG!!!
                        'MICROBIOLOGYEVENTS', # 70 MB
                        'NOTEEVENTS', # 3.8 GB  ------BIG!!!
                        'OUTPUTEVENTS', # 379 MB
                        'PATIENTS', # 2.6 MB
                        'PRESCRIPTIONS', # 735 MB
                        'PROCEDUREEVENTS_MV', # 47 MB
                        'PROCEDURES_ICD', # 6.5 MB
                        'SERVICES', # 3.4 MB
                        'TRANSFERS', # 24 MB
                    ]


    for MyFile in CSV_List:
        try:
            MIMIC_df[MyFile] = pd.read_csv(os.path.join(CSV_Folder_Location, (MyFile+'.csv')), sep=',', index_col='ROW_ID') 
        except:
            print('Unable to load the file: ', MyFile)

    return MIMIC_df







if __name__ == '__main__':
    print(load_MIMIC_to_pandas('C:\\Users\\peep\\Desktop\\Udacity Videos\\MIMIC'))

