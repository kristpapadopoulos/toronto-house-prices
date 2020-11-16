# toronto-house-prices
A preliminary data driven study on Toronto house prices

install requirements.txt for packages used in the study

1) Toronto Real Estate Board Home Price data is extracted from pdf from Feb 2012 to Oct 2020

To scrap the pdfs from TREB website:
a) run utils/extract_housing_price.py

To extract home price data from pdfs:
b) run utils/convert_housing_pdf_csv.py (uses tabula-py package)
c) run utils/read_housing_csv.py -> creates csv file located in
/data/treb_home_price_reference_master/TREB_Home_Price_Reference_2012Feb_2016Oct.csv

2) Model uses Prophet package (fbprophet)
a) requires first pystan installed and configured
b) if issues are encountered installing Prophet see https://facebook.github.io/prophet/docs/installation.html#python
