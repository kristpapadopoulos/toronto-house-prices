import os
import tabula

housing_price_pdf_dir = '/data/housing_price_pdf'

housing_price_csv_dir = '/data/housing_price_csv'

for file in os.listdir(housing_price_pdf_dir):
    file_name = file.split('.')[0]
    print('Converted pdf to csv ...\n')
    try:
        tabula.convert_into(f'{housing_price_pdf_dir}/{file}', 
            f"{housing_price_csv_dir}/{file_name}.csv", 
            output_format="csv", pages=3)
    except:
        print(file, 'not converted')