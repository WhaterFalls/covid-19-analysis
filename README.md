Contains data, scripts, and Tableau workbook that I used for my analysis.

get_data.py gets the data from two sources:

Corona data scraper: https://coronadatascraper.com/#home
NY Times data by county: https://github.com/nytimes/covid-19-data

Corona data scraper has thorough data at each level: city, county, state/province, and country. It has population level data but we noticed it was missing deaths for many counties so we supplemented from the NY Times data.

The data gets saved in the data folder.

The Tableau workbook is a packaged workbook so should be able to open with Tableau Reader, which is free: https://www.tableau.com/products/reader. Any further anaylsis will require a Tableau Desktop license.