import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("popular_people.csv")

# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())

# finding missing values

print(df.isnull().sum())

# drop duplicates

df.drop_duplicates(inplace=True)


df['gender'] = df['gender'].map({
    0: 'Not Specified',
    1: 'Female',
    2: 'Male'
})


print(df['gender'].value_counts())

print(df['known_for_department'].value_counts())

top10 = df.sort_values(by='popularity', ascending=False).head(10)

print(top10[['name', 'popularity']])


print(df.groupby('gender')['popularity'].mean())


print(df.groupby('known_for_department')['popularity'].mean())


# gender distrubution


df['gender'].value_counts().plot(kind='bar')

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.show()


# top dep

df['known_for_department'].value_counts().plot(kind='bar')

plt.title("Departments")
plt.show()



plt.hist(df['popularity'], bins=20)

plt.title("Popularity Distribution")
plt.xlabel("Popularity")

plt.show()