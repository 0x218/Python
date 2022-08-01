## Reads an excel using Pandas, filter a field and creates new excel for each filtered group.

import pandas as pd

## wdiexcel.xlsx was downloaded from http://databank.worldbank.org/data/download/WDI_excel.zip
## deleted all tabs except one for this exercise
## the remained tab has 690201 records
## This program filters "CountryCode", create new excel for unique CountryCode.

## run: python filter.py

data = pd.read_excel("wdiexcel.xlsx") ## place the file in current directory
countrycode=data["CountryCode"].unique() ## using "CountryCode" for my filtering

for i in countrycode:
    a = data[data["CountryCode"].str.contains(i)]
    a.to_excel(i+".xlsx") ##writes new excel


