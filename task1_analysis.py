import pandas as pd

# Step 1: Load your local dataset
df = pd.read_csv("C:/Users/lokes/OneDrive/Desktop/Python/BigDataAnalysys/netflix_titles.csv")

# Step 2: Show the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Show dataset info
print("\nDataset Info:")
print(df.info())

# Step 4: Count of Movies vs TV Shows
print("\nCount of content types (Movie vs TV Show):")
print(df['type'].value_counts())

# Step 5: Top 10 countries
print("\nTop 10 countries with most content:")
print(df['country'].value_counts().head(10))

# Step 6: Most common genres
print("\nTop 10 most common genres:")
print(df['listed_in'].value_counts().head(10))

# Step 7: Content added by year
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year
print("\nContent count by year:")
print(df['year_added'].value_counts().sort_index())
