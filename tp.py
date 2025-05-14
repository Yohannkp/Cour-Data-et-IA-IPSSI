import pandas as pd
# Load the first file into a dataset
marketing = pd.read_csv('Marketing.csv')

# Load the second file into a dataset
ca = pd.read_csv('CA.csv')

# Display the first few rows of each dataset
print("Marketing Dataset:")
print(marketing.head())