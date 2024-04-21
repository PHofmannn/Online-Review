# Matching Data with Metadata according to the Parent Asin

import pandas as pd
import numpy as np

# Import the Review data
file_path1 = '/Volumes/Paula_SSD/Data/JsonLine/filtered_Mouse.json'
data_review= pd.read_csv(file_path1)


# Importing Meta Data
file_path2 = 'Online-Review/SelectingData/VideoGames/top_200_products_VideoGames.csv'

# Columns to import
columns_to_import = ['main_category', 'title', 'average_rating', 'rating_number', 'features', 'price', 'parent_asin']

# Import data with specific columns
data_meta = pd.read_csv(file_path2, usecols=columns_to_import)


# Merge the data based on parent_asin
meta_data_Review = pd.merge(data_review, data_meta, on='parent_asin', how='left')

# Display the merged Data
print (meta_data_Review.head(3))

# Save the data, please modify the name of the file
meta_data_Review.to_csv('/Users/paulahofmann/Documents/Coding/Online-Review/DataPreperation/Meta_Mouse.csv', index=False)