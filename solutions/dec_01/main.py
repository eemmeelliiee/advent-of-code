
import pandas as pd

# Path to Excel file
excel_path = 'solutions/dec_01/data/input.xlsx'

# Read Excel file, and convert columns into seperate Pandas DataFrames
left_col_df = pd.read_excel(excel_path)['left_col']     # ", usecols='left_col')" would not work...
right_col_df = pd.read_excel(excel_path)['right_col']   # ", usecols='right_col')" would not work...

# Convert Pandas DataFrames into Lists
left_col_list = left_col_df.tolist()
right_col_list = right_col_df.tolist()

# Sort Lists by ascending order
left_col_list.sort()
right_col_list.sort()

# For each element in left_col_list, calculate the distance to corresponding element in right_col_list
all_distances_list = []
for i in range(len(left_col_list)):
             distance = abs(left_col_list[i]-right_col_list[i])
             all_distances_list.append(distance)

# Sum all distances
sum_all_distances = sum(all_distances_list)

# Print result 
print("Sum of all distances:")
print(sum_all_distances)