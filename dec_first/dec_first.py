import pandas as pd

# Path to Excel file
excel_path = 'dec_first/data/dec_first_input.xlsx'

# Read Excel file, and convert columns into seperate Pandas DataFrames
left_col_df = pd.read_excel(excel_path, usecols='left_col')
right_col_df = pd.read_excel(excel_path, usecols='right_col')

# Convert DataFrames into Lists
left_col_list = left_col_df.tolist()
right_col_list = right_col_df.tolist()

# Sort Lists by ascending order
left_col_list.sort()
right_col_list.sort()

## Print lists
print(left_col_list)
print(right_col_list)

