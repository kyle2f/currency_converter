# 20 january 2018

rates = {
    'USD':370,
    'GBP':500,
    'BTC':4551124.12,
    'GHS':78.51,
    'EUR': 440,
}

rates =[
    {
    'country':['USA'],
    'currency':'USD',
    'rate':360
},
{
    'country':['UK'],
    'currency':'GBP',
    'rate':360
}
,{
    'country':[''],
    'currency':'BITCOIN',
    'rate':360
},{
    'country':['GHANA'],
    'currency':'GHS',
    'rate':360
}
,{
    'country':['Austria',
'Belgium',
'Cyprus',
'Estonia',
'Finland',
'France',
'Germany',
'Greece',
'Ireland',
'Italy',
'Latvia',
'Lithuania',
'Luxembourg',
'Malta',
'Netherlands',
'Portugal',
'Spain',
'Slovenia',
'Slovakia'],
    'currency':'USD',
    'rate':360
}
]
print('Welcome to our python meetup python application')
print('We currently support only Naira nigeria currency')
currency_or_country = input('Please type a currency/country: ')

result = None
kind = None
for records in rates:
    if currency_or_country.lower() == records['currency'].lower():
        result = records['rate']
        kind = ['currency']
        break
    similar_case_countries =[]
    for country in records['country']:
        similar_case_countries.append(country.lower)
    if currency_or_country.lower() in similar_case_countries:
        result = record['rates']


print('The rate for %s which is a %s is %s'%(currency_or_country, kind , result))
