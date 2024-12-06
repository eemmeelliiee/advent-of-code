values_list = []
with open("solutions/dec_02/data/demo_input.txt", 'r') as file_data: 
    for line in file_data: 
        data = line.split() 
        values_list.append(data)
        
for line in values_list:
    print(line)