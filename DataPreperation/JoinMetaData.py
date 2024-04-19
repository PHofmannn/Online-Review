import sys
print(sys.executable)

# Matching Data with Metadata according to the Parent Asin

import pandas as pd
import numpy as np

# Import the Review data
file_path1 = '/Users/paulahofmann/Library/CloudStorage/OneDrive-Persönlich/Uni/2. Lernpools Master/Masterarbeit/Coding/Online-Review/Data Preperation/data_utilitarian_filter.csv'
data_utilitarian = pd.read_csv(file_path1)


# Importing Meta Data
file_path2 = '/Users/paulahofmann/Library/CloudStorage/OneDrive-Persönlich/Uni/2. Lernpools Master/Masterarbeit/Coding/Online-Review/Selecting Data/Appliance/top_200_products_Appliances.'

# Columns to import
columns_to_import = ['main_category', 'title', 'average_rating', 'rating_number', 'features', 'price', 'parent_asin']

# Import data with specific columns
data_meta = pd.read_csv(file_path2, usecols=columns_to_import)


# Merge the data based on parent_asin
meta_data_Utilitarian_Filter = pd.merge(data_utilitarian, data_meta, on='parent_asin', how='left')

# Display the merg