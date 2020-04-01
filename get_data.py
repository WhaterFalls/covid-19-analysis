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
        cases_with_pop.loc[(cases_with_pop['state']=='NY') & (cases_with_pop['city']=='New York City') & (cases_with_pop['date'] == dt), 'deaths'] = deaths

    to_fill.apply(fill_in, axis=1)
    cases_with_pop.loc[(cases_with_pop['state']=='NY') & (cases_with_pop['city']=='New York City')]

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
            'left_state': 'NY',
            'left_county': 'Suffolk County',
            'right_state': 'New York',
            'right_county': 'Suffolk'
        },
        {
            'left_state': 'NY',
            'left_county': 'Westchester County',
            'right_state': 'New York',
            'right_county': 'Westchester'
        },
        {
            'left_state': 'NY',
            'left_county': 'Nassau County',
            'right_state': 'New York',
            'right_county': 'Nassau'
        },
        {
            'left_state': 'NY',
            'left_county': 'Rockland County',
            'right_state': 'New York',
            'right_county': 'Rockland'
        },
        {
            'left_state': 'GA',
            'left_county': 'Cobb County',
            'right_state': 'Georgia',
            'right_county': 'Cobb'
        },
        {
            'left_state': 'GA',
            'left_county': 'DeKalb County',
            'right_state': 'Georgia',
            'right_county': 'DeKalb'
        },
        {
            'left_state': 'GA',
            'left_county': 'Fulton County',
            'right_state': 'Georgia',
            'right_county': 'Fulton'
        },
        {
            'left_state': 'GA',
            'left_county': 'Gwinnett County',
            'right_state': 'Georgia',
            'right_county': 'Gwinnett'
        },
        {
            'left_state': 'MA',
            'left_county': 'Bristol County',
            'right_state': 'Massachusetts',
            'right_county': 'Bristol'
        },
        {
            'left_state': 'MA',
            'left_county': 'Essex County',
            'right_state': 'Massachusetts',
            'right_county': 'Essex'
        },
        {
            'left_state': 'MA',
            'left_county': 'Middlesex County',
            'right_state': 'Massachusetts',
            'right_county': 'Middlesex'
        },
        {
            'left_state': 'MA',
            'left_county': 'Norfolk County',
            'right_state': 'Massachusetts',
            'right_county': 'Norfolk'
        },
        {
            'left_state': 'MA',
            'left_county': 'Plymouth County',
            'right_state': 'Massachusetts',
            'right_county': 'Plymouth'
        },
        {
            'left_state': 'MA',
            'left_county': 'Suffolk County',
            'right_state': 'Massachusetts',
            'right_county': 'Suffolk'
        },
        {
            'left_state': 'MA',
            'left_county': 'Worcester County',
            'right_state': 'Massachusetts',
            'right_county': 'Worcester'
        },
                {
            'left_state': 'NJ',
            'left_county': 'Bergen County',
            'right_state': 'New Jersey',
            'right_county': 'Bergen'
        },
        {
            'left_state': 'NJ',
            'left_county': 'Essex County',
            'right_state': 'New Jersey',
            'right_county': 'Essex'
        },
        {
            'left_state': 'NJ',
            'left_county': 'Hudson County',
            'right_state': 'New Jersey',
            'right_county': 'Hudson'
        },
        {
            'left_state': 'NJ',
            'left_county': 'Middlesex County',
            'right_state': 'New Jersey',
            'right_county': 'Middlesex'
        },
        {
            'left_state': 'NJ',
            'left_county': 'Monmouth County',
            'right_state': 'New Jersey',
            'right_county': 'Monmouth'
        },
        {
            'left_state': 'NJ',
            'left_county': 'Union County',
            'right_state': 'New Jersey',
            'right_county': 'Union'
        },
        {
            'left_state': 'LA',
            'left_county': 'Jefferson County',
            'right_state': 'Louisiana',
            'right_county': 'Jefferson'
        },
        {
            'left_state': 'LA',
            'left_county': 'Orleans County',
            'right_state': 'Louisiana',
            'right_county': 'Orleans'
        },
        {
            'left_state': 'LA',
            'left_county': 'St. Tammany Parish',
            'right_state': 'Louisiana',
            'right_county': 'St. Tammany'
        }
    ]

main()