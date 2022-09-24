# import modules
import os
import pandas as pd

import glob

skaterslist = glob.glob("./raw_data/skaters_*.csv")

print(skaterslist)


# assign path
#path, dirs, files = next(os.walk("./raw_data/skaters_*.csv"))

# create empty list
dataframes_list = []
 
# append datasets to the list
for skater in skaterslist:
    temp_df = pd.read_csv(skater)
    
    
    dataframes_list.append(temp_df)
     
# display datasets
for dataset in dataframes_list:
    print(dataset)
