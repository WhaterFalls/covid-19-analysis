import pandas as pd

covid_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
covid_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')
covid_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')

id_variables = ['Province/State', 'Country/Region', 'Lat', 'Long']

covid_confirmed = covid_confirmed.melt(id_vars = id_variables,
                                       var_name = 'ReportDate',
                                       value_name = 'ConfirmedCases')
covid_recovered = covid_recovered.melt(id_vars = id_variables,
                                       var_name = 'ReportDate',
                                       value_name = 'Recoveries')
covid_deaths = covid_deaths.melt(id_vars = id_variables,
                                 var_name = 'ReportDate',
                                 value_name = 'Deaths')
del id_variables

join_variables = ['ReportDate', 'Country/Region', 'Province/State']

covid = pd.merge(left = covid_confirmed,
                 right = covid_recovered, 
                 how = 'left', 
                 on = join_variables, 
                 suffixes = ['', '_drop'])
covid = covid.loc[:, covid.columns[~covid.columns.str.endswith('_drop')]]
covid = pd.merge(left = covid,
                 right = covid_deaths,
                 how = 'left',
                 on = join_variables,
                 suffixes = ['', '_drop'])
covid = covid.loc[:, covid.columns[~covid.columns.str.endswith('_drop')]]

covid['Country/Region'].fillna('Unknown', inplace = True)
covid['Province/State'].fillna('Unknown', inplace = True)

del covid_confirmed, covid_recovered, covid_deaths

covid['Province/State'] = covid['Province/State'].str.strip()  # Fixes issue of extra space
covid.loc[:, 'US_State'] = covid['Province/State'].str[-2:]
covid.loc[(covid['Country/Region'] != 'US') | ([abbrev.upper() != abbrev for abbrev in covid['US_State']]), 'US_State'] = None
covid.loc[covid['US_State'] == 'C.', 'US_State'] = 'DC'

covid['ReportDate'] = covid['ReportDate'].astype('datetime64')

states_to_classify = covid.loc[covid['US_State'].isnull(), :]['Province/State'].unique().tolist()

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def get_state_abbrev(state_name):  
  for abbrev, state in states.items():
    if state == state_name:
      return abbrev
    
for state in states_to_classify:
  covid.loc[covid['Province/State'] == state, 'US_State'] = get_state_abbrev(state)
  
covid.to_csv('/Users/jhwa/Documents/jason/covid-19/data/test.csv')