import pandas as pd

excel_path = 'dec_first/data/dec_first_input.xlsx'

left_col_df = pd.read_excel(excel_path)
right_col_df = pd.read_excel(excel_path)

left_col_name = 'left_col'
right_col_name = 'right_col'

left_col = left_col_df[left_col_name]
right_col = right_col_df[right_col_name]

left_col_list = left_col.tolist()
right_col_list = right_col.tolist()

print(left_col_list)
print(right_col_list)

