import pandas as pd

#Load a CSV file into a Pandas DataFrame:
df = pd.read_csv("100 Sales Records.csv")

# print(df.to_string()) # Prints complete dataFrame
# print(df) # Prints header, first 5 and last 5 rows with summary [100 rows x 14 columns]

# print(pd.options.display.max_rows) # value is 60

# print(df.head(10)) # header with first 10 rows or default 5

# print(df.tail(10)) # header with last 10 rows or default 5

print(df.info()) # Information about data, row count, column count, datatype of columns, non-null column value count, memory usage