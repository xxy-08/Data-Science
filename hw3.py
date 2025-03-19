# Solve the following problems.
# 1.⁠ ⁠Filter the data to include only weekdays (Monday to Friday) and plot a line graph showing the pedestrian counts for each day of the week.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Read the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)
# ----- Write your code below this after running above above code-----------
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['weekday'] = df['hour_beginning'].dt.weekday
df_weekdays = df[df['weekday'] < 5]
df_weekdays.info()
plt.figure(figsize=(12, 6))
plt.plot(df_weekdays['weekday'], df_weekdays['Pedestrians'], color='blue', linestyle='-', marker='o', markersize=3)
plt.title('Pedestrian Counts Over Time')
plt.xlabel('weekday')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.tight_layout()
plt.show()


# 2.⁠ ⁠Track pedestrian counts on the Brooklyn Bridge for the year 2019 and analyze how different weather conditions 
# influence pedestrian activity in that year. Sort the pedestrian count data by weather summary to identify any 
# correlations( with a correlation matrix) between weather patterns and pedestrian counts for the selected year.
# -This question requires you to show the relationship between a numerical feature(Pedestrians) and a non-numerical 
# feature(Weather Summary). In such instances we use Encoding. Each weather condition can be encoded as numbers( 0,1,2..). 
# This technique is called One-hot encoding.
# -Correlation matrices may not always be the most suitable visualization method for relationships involving categorical data 
# points, nonetheless this was given as a question to help you understand the concept better.
df['year'] = df['hour_beginning'].dt.year
df_2019 = df[df['year'] == 2019]
df_2019_encoded = pd.get_dummies(df_2019, columns=['weather_summary'])
df_2019_encoded = df_2019_encoded.select_dtypes(include=['number'])
corr_matrix = df_2019_encoded.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix of Weather and Pedestrian Counts (2019)')
plt.show()
# 3.⁠ ⁠Implement a custom function to categorize time of day into morning, afternoon, evening, and night, 
# and create a new column in the DataFrame to store these categories. Use this new column to analyze 
# pedestrian activity patterns throughout the day.
# -Students can also show plots analyzing activity.
df['hour'] = df['hour_beginning'].dt.hour
def categorize_time_of_day(hour):
    if 6 <= hour < 12:
        return 'morning'
    elif 12 <= hour < 17:
        return 'afternoon'
    elif 17 <= hour < 21:
        return 'evening'
    else:
        return 'night'
df['time_of_day'] = df['hour'].apply(categorize_time_of_day)
plt.figure(figsize=(10, 6))
df.groupby('time_of_day')['Pedestrians'].mean().plot(kind='bar', color=['skyblue', 'lightgreen', 'orange', 'lightcoral'])
plt.title('Average Pedestrian Counts by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Average Pedestrian Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
