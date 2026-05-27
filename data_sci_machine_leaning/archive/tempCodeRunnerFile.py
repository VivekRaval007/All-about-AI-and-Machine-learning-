
df.drop_duplicates(inplace=True)

# convert date 
df['date_added'] = pd.to_datetime(df['date_added'])

# df['year_added'] = df['date_added'].dt.year

# df['month_added'] = df['date_added'].dt.month

