import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


df = pd.read_csv("netflix_titles.csv")


# print(df.head())

# print(df.tail())

# print(df.columns)

#                                   Check missing values 

print(df.isnull().sum())

# Fill the values in the county 

df['country'] = df['country'].fillna("Unknown")

# Fill missing director
df['director'] = df['director'].fillna("Not Available")

# drop row with missing data
df.dropna(subset=['date_added'],inplace=True)

# Check duplicates
df.duplicated().sum()

# remove duplicates
df.drop_duplicates(inplace=True)


df['date_added'] = df['date_added'].str.strip()


# convert date 
df['date_added'] = pd.to_datetime(df['date_added'])

df['year_added'] = df['date_added'].dt.year

df['month_added'] = df['date_added'].dt.month

sns.set_style("whitegrid")

sns.countplot(x='type',data=df)
# plt.figure(figsize=(10,5))
plt.title("movies VS Tv shows on Netflix ")
plt.xlabel("content type ")
plt.ylabel("count")

plt.show()

top_country = df['country'].value_counts().head(10)

top_country.plot(kind='bar')

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Shows")

plt.xticks(rotation=40)

plt.show()


df['year_added'] =df['date_added'].dt.year

df['year_added'].value_counts().sort_index().plot(kind='line')
plt.title("Netflix content addded  over  years")
plt.xlabel("year")
plt.ylabel("Number of titles")

plt.show()


sns.countplot(
    y='rating',
    data=df,
    order=df['rating'].value_counts().index
)

plt.title("Ratings Distribution")

plt.show()


top_genres = df['listed_in'].value_counts().head(10)

top_genres.plot(kind='barh')

plt.title("top Genrs on  Netflix ")
plt.xlabel("count")

plt.show()


df['release_year'].value_counts().sort_index().tail(20).plot(kind='line')

plt.title("Movie Release Trend")
plt.xlabel("Year")
plt.ylabel("Count")

plt.show()


type_counts = df['type'].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    type_counts,
    labels=type_counts.index,
    autopct='%1.1f%%'
)

plt.title("Movies vs tv shows")

plt.show()

top_ratings = df['rating'].value_counts().head(5)

plt.figure(figsize=(8,5))

sns.barplot(
    x=top_ratings.index,
    y=top_ratings.values
)

plt.title("Top 5 Netflix Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.show()

top_years = df['release_year'].value_counts().head(15)

plt.figure(figsize=(12,5))

sns.barplot(
    x=top_years.index,
    y=top_years.values
)

plt.title("Top 15 Release Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.show()










