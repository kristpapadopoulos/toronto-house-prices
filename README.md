# Toronto House Price Study
A preliminary data driven study on Toronto house prices

### 1) Install requirements.txt for packages used in the study

### 2) Toronto Real Estate Board Home Price data is extracted from pdf from Feb 2012 to Oct 2020

To scrap the pdfs from TREB website:
- run utils/extract_housing_price.py

To extract home price data from pdfs:
- run utils/convert_housing_pdf_csv.py (uses tabula-py package)
- run utils/read_housing_csv.py -> creates csv file located in
/data/treb_home_price_reference_master/TREB_Home_Price_Reference_2012Feb_2016Oct.csv
- Analysis notebook toronot-house-prices.ipynb is run referencing csv files in data folder
- scraping and csv generation do not need to be run but are provided for reference
- dataset references are provided in Toronto House Price Study.pdf

### 3) Model uses Prophet package (fbprophet)
- requires first pystan installed and configured
- if issues are encountered installing Prophet see https://facebook.github.io/prophet/docs/installation.html#python
