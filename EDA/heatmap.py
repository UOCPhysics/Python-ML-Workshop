import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Read the dataset. 
#You can download the dataset from (https://www.kaggle.com/competitions/titanic/overview)
df = pd.read_csv('titanic/train.csv')

# Filter out missing values
filtered_df = df.dropna(subset=['Age', 'Sex','Survived'])

# Group the data by gender and age and calculate the survival rate
survival_rates = filtered_df.groupby(['Sex', pd.cut(filtered_df['Age'], bins=np.arange(0, 100, 10))])['Survived'].mean().unstack()

# Create the heatmap using Matplotlib
fig, ax = plt.subplots()
im = ax.imshow(survival_rates, cmap='YlGn')

# Set x and y axis labels
ax.set_xticks(np.arange(len(survival_rates.columns)))
ax.set_yticks(np.arange(len(survival_rates.index)))
ax.set_xticklabels(survival_rates.columns, rotation=45, ha='right')
ax.set_yticklabels(survival_rates.index)


# Set colorbar
cbar = ax.figure.colorbar(im)
cbar.set_label('Survival Rate', fontsize=12)  #Add color bar label

# Set the title
ax.set_title('Survival Rate by Gender and Age')
plt.xlabel('Age')
plt.ylabel('Gender')

# Save the figure with high resolution
plt.savefig('heatmap.png', dpi=300)

# Show the heatmap
plt.show()
