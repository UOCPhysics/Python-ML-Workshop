import pandas as pd
import matplotlib.pyplot as plt

#Read the dataset. 
#You can download the dataset from (https://www.kaggle.com/competitions/titanic/overview)
df = pd.read_csv('titanic/train.csv')

# Filter out missing values in Age and Fare columns
filtered_df = df.dropna(subset=['Age'])

# Calculate the maximum, minimum, Q1, Q2 (median), and Q3 for Fare
fare_max = filtered_df['Age'].max()
fare_min = filtered_df['Age'].min()
fare_q1 = filtered_df['Age'].quantile(0.25)
fare_median = filtered_df['Age'].median()
fare_q3 = filtered_df['Age'].quantile(0.75)

iqr = fare_q3 - fare_q1
lower_bound = fare_q1 - 1.5 * iqr
upper_bound = fare_q3 + 1.5 * iqr


# Create a boxplot of Fare
plt.figure(figsize=(10, 2))
#plt.boxplot(filtered_df['Age'], vert=False)
# Create a horizontal boxplot with whiskers in blue and outliers in red
boxplot = plt.boxplot(filtered_df['Age'], vert=False, patch_artist=True,
                     boxprops=dict(facecolor='lightgreen'),
                     whiskerprops=dict(color='blue'),
                     capprops=dict(color='blue'),
                     flierprops=dict(marker='o', markerfacecolor='red', markersize=5))

# Add markers for maximum, minimum, Q1, Q2, and Q3
plt.scatter([fare_q1, fare_median, fare_q3], [1, 1, 1], c='blue', marker='o')
plt.scatter([lower_bound, upper_bound], [1, 1], c='green', s=1000, marker='|')

# Add labels for maximum, minimum, Q1, Q2, and Q3
#plt.text(fare_max, 1.1, f"Max: {fare_max}", ha='right', va='bottom',fontsize=16)
#plt.text(fare_min, 1.1, f"Min: {fare_min}", ha='left', va='bottom',fontsize=16)
plt.text(fare_q1, 0.9, f"Q1: {fare_q1}", ha='right', va='top',fontsize=14)
plt.text(fare_median, 1.1, f"Q2 (Median): {fare_median}", ha='center', va='bottom',fontsize=14)
plt.text(fare_q3, 0.9, f"Q3: {fare_q3}", ha='left', va='top',fontsize=14)
plt.text(lower_bound, 0.8, f'Q1 - 1.5*IQR', ha='center',fontsize=14)
plt.text(upper_bound, 0.8, f'Q3 + 1.5*IQR', ha='center',fontsize=14)



# Set the x-axis label
plt.xlabel('Fare',fontsize=16)

# Increase the size of tick labels
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Set the plot title
plt.title('Boxplot: Fare Distribution',fontsize=16)

# Display the plot
plt.show()
