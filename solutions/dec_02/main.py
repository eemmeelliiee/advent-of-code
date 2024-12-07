# Splits .txt file into a list of reports
reports = []
with open("solutions/dec_02/data/input.txt", 'r') as file_data: 
    for line in file_data: 
        data = line.split() 
        reports.append(data)

# Calculates the difference between all adjacent elements for a report, then returns values as a 'diff_list'
def calculate_diff(report):
    i = 0
    diff_list = []
    for element in range(len(report)-1):
        diff = int(report[i+1])-int(report[i])
        diff_list.append(diff)
        i+=1
    return diff_list

# Controls if values in 'diff_list' are consistant, then returns it with determined consistancy boolean
def control_diff_consistancy(diff_list):
    increase_list = []
    decrease_list = []
    for diff in diff_list:
        if diff > 0:
            increase_list.append(diff)
        elif diff < 0:
            decrease_list.append(diff)
    if len(increase_list) == len(diff_list) or len(decrease_list) == len(diff_list): # Controls if all values in list are consistant; either all increasing or all decreasing
        consistant = True
    else:
        consistant = False
    return diff_list,consistant

# Sets diff_lists where values are both 'consistant' and within accepted range as 'safe', and inconsistent and out-of-range as not safe.
def control_diff_amount(diff_list, consistant):
    if consistant:
        for diff in diff_list:
            if abs(diff) in[1,2,3]: # Accepted range
                safe = True
            else:
                safe = False
                break
    else:
        safe = False
    return safe

# Saves safe and unsafe reports into seperate lists
safe_reports = []
unsafe_reports = []
for report in reports:
    diff_list = calculate_diff(report) # Get 'diff_list' for report
    diff_list, consistant = control_diff_consistancy(diff_list) # Get corresponding consistency boolean for 'diff_list'
    safe = control_diff_amount(diff_list, consistant) # Get concluded safety info

    if safe:
        safe_reports.append(report)
    else:
        unsafe_reports.append(report)

# Calculates tot amount of safe and unsafe reports
tot_safe = len(safe_reports)
tot_unsafe = len(unsafe_reports)

# Prints tot amount of safe reports
print("Tot safe reports: ")
print(tot_safe)