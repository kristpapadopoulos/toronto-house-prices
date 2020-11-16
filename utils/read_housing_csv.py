# convert csv from different pdfs from TREB
# pdf range is from 2020_October to 

import os
import calendar
import numpy as np
import pandas as pd

#path to csv files
housing_price_csv_dir = '/data/housing_price_csv'

# month map
month_map = {calendar.month_name[i]:str(i) for i in range(1,13)}

# housing price col names
value_names = ['SingleFamilyDetachedIndex','SingleFamilyDetachedReference',
                'SingleFamilyAttachedIndex','SingleFamilyAttachedReference',
                'TownHouseIndex','TownHouseReference','ApartmentIndex',
                'ApartmentReference']

# 2020 csv files
records_2020 = []

for file in os.listdir(housing_price_csv_dir):

    try:
    
        if file.split('_')[0] == '2020':
            
            year = file.split('_')[0]
            
            month = file.split('_')[1].split('.')[0]

            date = f'{year}-{month_map[month]}'
            
            df = pd.read_csv(f'{housing_price_csv_dir}/{file}', error_bad_lines=False, index_col=0)
            
            df = df.rename(columns={'Unnamed: 5':value_names[4],'Unnamed: 7':value_names[6]})
            
            record_2020 = {'Date':date, 
                          value_names[0]:df.loc['City of Toronto','Single Family Detached'].split(' ')[0],
                          value_names[1]:df.loc['City of Toronto','Single Family Detached'].split(' ')[1],
                          value_names[2]:df.loc['City of Toronto','Single Family Attached'].split(' ')[0],
                          value_names[3]:df.loc['City of Toronto','Single Family Attached'].split(' ')[1],
                          value_names[4]:df.loc['City of Toronto', value_names[4]],
                          value_names[5]:df.loc['City of Toronto','Townhouse'].split(' ')[0],
                          value_names[6]:df.loc['City of Toronto',value_names[6]],
                          value_names[7]:df.loc['City of Toronto','Apartment']
                           }
            
            records_2020.append(record_2020)

    except:

            value_list = [np.nan for i in range(len(value_names))]
            
            record_2020 = {'Date':date, **dict(zip(value_names, value_list))}
            
            records_2020.append(record_2020)
        
records_2020_df = pd.DataFrame(records_2020)


# records from 2019 to 2015 in different format
records_2019_2015 = []

for file in os.listdir(housing_price_csv_dir):
    
    if file.split('_')[0] != '2020':
        
        try:
        
            year = file.split('_')[0]
        
            month = file.split('_')[1].split('.')[0]

            date = f'{year}-{month_map[month]}'
        
            df = pd.read_csv(f'{housing_price_csv_dir}/{file}', 
                error_bad_lines=False, index_col=0).loc['City of Toronto',:]
            
            value_list = [x for x in df.tolist()[3:] if x.find('%') == -1]
            
            record_2019_2015 = {'Date':date, **dict(zip(value_names, value_list))}
            
            records_2019_2015.append(record_2019_2015)
            
        except:
            
            value_list = [np.nan for i in range(len(value_names))]
            
            record_2019_2015 = {'year':year, 'month':month, **dict(zip(value_names, value_list))}
            
            records_2019_2015.append(record_2019_2015)

records_2019_2015_df = pd.DataFrame(records_2019_2015).dropna()


# records 2015 and before in different format
records_before_2015 = []

for file in os.listdir(housing_price_csv_dir):
    
    if file.split('_')[0] in ['2015','2014','2013','2012']:
        
        try:
        
            year = file.split('_')[0]
        
            month = file.split('_')[1].split('.')[0]

            date = f'{year}-{month_map[month]}'
        
            df = pd.read_csv(f'{housing_price_csv_dir}/{file}', error_bad_lines=False, index_col=0)
            
            df = df.rename(columns={'Unnamed: 3':value_names[0], 'Unnamed: 5':value_names[2], 
                                    'Unnamed: 7':value_names[4],'Unnamed: 9':value_names[6]})
            
            record_before_2015 = {'Date':date, 
                                 value_names[0]:df.loc['City of Toronto',value_names[0]], 
                                 value_names[1]:df.loc['City of Toronto','Single-Family Detached'].split(' ')[0],
                                 value_names[2]:df.loc['City of Toronto',value_names[2]],
                                 value_names[3]:df.loc['City of Toronto','Single-Family Attached'].split(' ')[0],
                                 value_names[4]:df.loc['City of Toronto',value_names[4]],
                                 value_names[5]:df.loc['City of Toronto','Townhouse'].split(' ')[0],
                                 value_names[6]:df.loc['City of Toronto',value_names[6]],
                                 value_names[7]:df.loc['City of Toronto','Apartment'].split(' ')[0]}
            
            records_before_2015.append(record_before_2015)
            
        except:
            
            value_list = [np.nan for i in range(len(value_names))]
            
            record_before_2015 = {'year':year, 'month':month, **dict(zip(value_names, value_list))}
            
            records_before_2015.append(record_before_2015)

records_before_2015_df = pd.DataFrame(records_before_2015)

# need to drop 2015 records that were in different format
na_records_2015_to_drop = records_before_2015_df[(records_before_2015_df['year']=='2015') & 
                          (records_before_2015_df['SingleFamilyDetachedIndex'].isna())].index

records_before_2015_df = records_before_2015_df.drop(na_records_2015_to_drop, axis=0)

final_df = pd.concat([records_2020_df, records_2019_2015_df, records_before_2015_df])

final_df.to_csv('/data/treb_home_price_reference_master/TREB_Home_Price_Reference_2012Feb_2016Oct.csv',index=False)