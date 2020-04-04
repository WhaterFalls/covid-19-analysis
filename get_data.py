import pandas as pd


def main():
    cases_with_pop = pd.read_csv('https://coronadatascraper.com/timeseries.csv')
    supplement = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')

    print(sorted(list(supplement[(supplement['state']=='Louisiana')]['county'].unique())))

    # add in NYC data
    to_fill = supplement[(supplement['state']=='New York') & (supplement['county']=='New York City')]
    def fill_in(row):
        dt = row['date']
        deaths = row['deaths']
        cases_with_pop.loc[(cases_with_pop['state']=='New York') & (cases_with_pop['county']=='New York County') & (cases_with_pop['date'] == dt), 'deaths'] = deaths

    to_fill.apply(fill_in, axis=1)

    # fill in counties
    for c in get_configs():
        to_fill = supplement[(supplement['state']==c['right_state']) & (supplement['county']==c['right_county'])]
        def fill_in_county(row):
            dt = row['date']
            deaths = row['deaths']
            cases_with_pop.loc[(cases_with_pop['state']==c['left_state']) & (cases_with_pop['county']==c['left_county']) & (cases_with_pop['date'] == dt), 'deaths'] = deaths

        to_fill.apply(fill_in_county, axis=1)
        cases_with_pop.loc[(cases_with_pop['state']==c['left_state']) & (cases_with_pop['county']==c['left_county'])]

    cases_with_pop.to_csv('data/cases_with_pop.csv')


def get_configs():
    return [
        {
            'left_state': 'Louisiana',
            'left_county': 'Jefferson Parish',
            'right_state': 'Louisiana',
            'right_county': 'Jefferson'
        }
    ]

main()