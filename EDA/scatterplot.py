import pandas as pd
import matplotlib.pyplot as plt

#Read the dataset. 
#You can download the dataset from (https://www.kaggle.com/competitions/titanic/overview)
df = pd.read_csv('titanic/train.csv')

# Filter out missing values in Age and Fare columns
filtered_df = df.dropna(subset=['Age', 'Fare'])

# Separate the data for males and females
male_data = filtered_df[filtered_df['Sex'] == 'male']
female_data = filtered_df[filtered_df['Sex'] == 'female']

# Create the scatter plot for males
plt.scatter(male_data['Age'], male_data['Fare'], color='blue', label='Male')

# Create the scatter plot for females
plt.scatter(female_data['Age'], female_data['Fare'], color='red', label='Female')

# Set the labels and title
plt.xlabel('Age',fontsize=20)
plt.ylabel('Fare',fontsize=20)
plt.title('Fare vs. Age Scatter Plot',fontsize=18)

# Increase the size of tick labels
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# Add a legend
plt.legend()

# Display the chart
plt.show()
