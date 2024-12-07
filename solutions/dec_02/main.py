line_list = []
with open("solutions/dec_02/data/demo_input.txt", 'r') as file_data: 
    for line in file_data: 
        data = line.split() 
        line_list.append(data)

#for value_list in line_list:
#    print(value_list)

def consistant_check(value_list):
    i = 0
    consistant = False
    diff_list = []
    for value in range(len(value_list)-1):
        diff = int(value_list[i+1])-int(value_list[i])
        diff_list.append(diff)
        i+=1
    print(diff_list)

for value_list in line_list:
    consistant_check(value_list)
    #difference_check(value_list)

