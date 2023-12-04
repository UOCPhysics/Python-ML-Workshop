import pandas as pd
import matplotlib.pyplot as plt

#Read the dataset. 
#You can mention the path to the dataset in your computer.
df = pd.read_csv('house-prices/train.csv')

# Select the relevant columns
square_footage = df['GrLivArea']
num_bedrooms = df['BedroomAbvGr']
sale_price = df['SalePrice']
BsmtUnfSF=df['BsmtUnfSF'] #The total unfinished square footage
BsmtFinSF1=df['BsmtFinSF1'] #Basement Finished Square Feet 

# Calculate the Pearson's correlation coefficients
correlation_sqft_price = square_footage.corr(sale_price)
correlation_bedrooms_price = num_bedrooms.corr(sale_price)
correlation_basement_total = BsmtFinSF1.corr(BsmtUnfSF)

# Create a scatter plot of Square footage vs Sale price
plt.scatter(square_footage, sale_price, alpha=0.5)
plt.xlabel('Square Footage', fontsize=16)
plt.ylabel('Sale Price', fontsize=16)
plt.title('Square Footage vs Sale Price', fontsize=16)

# Increase the size of tick labels
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Add correlation coefficient to the plot
plt.text(100, 700000, f'Correlation: {correlation_sqft_price:.2f}', fontsize=16)

# Display the plot
plt.show()

# Create a scatter plot of Number of bedrooms vs Sale price
plt.scatter(num_bedrooms, sale_price, alpha=0.5)
plt.xlabel('Number of Bedrooms', fontsize=16)
plt.ylabel('Sale Price', fontsize=16)
plt.title('Number of Bedrooms vs Sale Price', fontsize=16)

# Add correlation coefficient to the plot
plt.text(0, 700000, f'Correlation: {correlation_bedrooms_price:.2f}', fontsize=16)

# Increase the size of tick labels
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)


# Display the plot
plt.show()

# Create a scatter plot of Number of bedrooms vs Sale price
plt.scatter(BsmtUnfSF, BsmtFinSF1, alpha=0.5)
plt.xlabel('Basement Finished Square Feet ', fontsize=16)
plt.ylabel('Unfinished Square Footage', fontsize=16)
plt.title('Year Built vs Size of Porch', fontsize=16)

# Add correlation coefficient to the plot
plt.text(0, 5000, f'Correlation: {correlation_basement_total:.2f}', fontsize=16)

# Increase the size of tick labels
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)


# Display the plot
plt.show()
