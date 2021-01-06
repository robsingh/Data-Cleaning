import pandas as pd
df = pd.read_csv('../Data/survey_results_public.csv') #dataframe is 2-D data structure with columns of potentially diff types.
schema_df = pd.read_csv('../Data/survey_results_schema.csv')

df.shape #to get the shape of df
df.info() #gives complete description of df

pd.set_option('display.max_columns')
df.head() #gives only the first 5 rows

df.tail() #last 10 items of df, can pass a number as an argument to see specific number of items
df['Hobbyist'].value_counts()

df.loc[0]

countries = ['United States','India','United Kingdom','Germany','Canada']
filt = df['Country'].isin(countries)
df.loc[filt,'Country']
filt = df['LanguageWorkedWith'].str.contains('Python', na = False)
df.rename(columns={'ConvertedComp':'SalaryUSD'},inplace = True)

