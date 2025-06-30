import pandas as pd
from matplotlib import pyplot as plt

#Load a CSV file into a Pandas DataFrame:
df = pd.read_csv("100 Sales Records.csv")

# Group by 'Region' and sum 'Total Revenue'
regional_sales = df.groupby('Region')['Total Revenue'].sum()

# Plot the results
regional_sales.plot(kind='bar', figsize=(8, 6))
plt.title('Total Sales Amount by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45) # Rotate x-axis labels if they overlap
plt.tight_layout() # Adjust layout to prevent labels from being cut off
plt.show()