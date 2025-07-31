import pandas as pd
import glob

file_paths = glob.glob('data/daily_sales_data_*.csv')

dataframes = []
for file_path in file_paths:
    df = pd.read_csv(file_path)
    df = df[df['product'] == 'pink morsel']
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    df['sales'] = df['price'] * df['quantity']
    df = df[['sales', 'date', 'region']]

    dataframes.append(df)

# Concatenate all dataframes into a single dataframe
combine_df = pd.concat(dataframes, ignore_index=True)
combine_df.to_csv('data/output.csv', index=False)
print("successfully combined the file")