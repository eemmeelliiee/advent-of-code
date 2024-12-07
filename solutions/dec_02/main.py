# Splits .txt file into two lists
report_list = []
with open("solutions/dec_02/data/input.txt", 'r') as file_data: 
    for line in file_data: 
        data = line.split() 
        report_list.append(data)

# Calculates the difference between adjecent values and returns values as a List
def calculate_diff(report):
    i = 0
    diff_list = []
    for value in range(len(report)-1):
        diff = int(report[i+1])-int(report[i])
        diff_list.append(diff)
        i+=1
    return diff_list

def control_diff_consistancy(diff_list):
    increase_list = []
    decrease_list = []
    for diff in diff_list:
        if diff > 0:
            increase_list.append(diff)
        elif diff < 0:
            decrease_list.append(diff)
    if len(increase_list) == len(diff_list) or len(decrease_list) == len(diff_list): 
        consistant = True
    else:
        consistant = False
    return diff_list, consistant
        
def control_diff_amount(diff_list, consistant):
    if consistant:
        for diff in diff_list:
            if abs(diff) in[1,2,3]:
                safe = True
            else:
                safe = False
                break
    else:
        safe = False
    return safe

safe_list = []
unsafe_list = []
for report in report_list:
    try: 
        diff_list, consistant = control_diff_consistancy(calculate_diff(report))
        if control_diff_amount(diff_list, consistant):
            safe_list.append(report)
        else:
            unsafe_list.append(report)
    except: 
        print("Could't calculate safety for: ")
        print(report)

tot_safe = len(safe_list)
tot_unsafe = len(unsafe_list)

print(tot_safe)

