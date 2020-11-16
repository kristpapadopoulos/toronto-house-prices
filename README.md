# Toronto House Price Study
A preliminary data driven study on Toronto house prices

### 1) Install requirements.txt for python packages used in the study

### 2) Toronto Real Estate Board Home Price data is extracted from pdf from Feb 2012 to Oct 2020

To scrap the pdfs from TREB website:
- run utils/extract_housing_price.py

To extract home price data from pdfs:
- first run utils/convert_housing_pdf_csv.py (uses tabula-py package)
- then run utils/read_housing_csv.py -> creates csv file located in /data/treb_home_price_reference_master/TREB_Home_Price_Reference_2012Feb_2016Oct.csv
- Analysis notebook toronto-house-prices.ipynb is run referencing csv files in data folder
- web scraping and pdf->csv generation do not need to be run but source files are provided in /data for reference and utils scripts are provided in /utils
- sources of data in /data are provided in toronto_house_price_study.pdf

### 3) Model uses Prophet package (fbprophet)
- requires first pystan installed and configured
- if issues are encountered installing Prophet see https://facebook.github.io/prophet/docs/installation.html#python
