#Red-Nosed reports

def main():
    data = convert_input_to_list("input_text.txt")
    print(data)

def convert_input_to_list(file_path):
    input_list = []
    with open(file_path, 'r') as file:
        for line in file:
            input_list.append([int(x) for x in line.split()])
    return input_list

def check_safe_unsafe(input_list):
    count = 0
    increasing = True
    decreaseing = True
    report_num = 0
    for level in input_list:
        for report in level:
            
            report_num += 1

            

    return count



main()
