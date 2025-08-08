import pandas as pd
import glob

# 1. find and combine data
all_files = glob.glob("data/*.csv")

df_list = []
df_list = [pd.read_csv(file) for file in all_files]

df = pd.concat(df_list, ignore_index=True)

# 2. filter data
df_filtered = df[df['product'] == 'pink morsel'].copy()                      #filter for 'pink morsel'
df_filtered['price'] = df_filtered['price'].str.replace('$', '').astype(float)        #convert price data from string to float

# 3. calculate sales
df_filtered['sales'] = df_filtered['quantity']*df_filtered['price']

# 4. save to csv
df_final = df_filtered[['sales', 'date', 'region','product']]

output_path = 'pink_morsel_sales.csv'
df_final.to_csv(output_path, index=False)

print(f"Processing complete. Formatted data is saved into '{output_path}'.")