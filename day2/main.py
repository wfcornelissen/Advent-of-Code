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
    safe_count = 0
    unsafe_count = 0
    increasing = True
    decreasing = True
    for level in input_list:
        if level[0] < level[1]:
            decreasing = False
        else:
            increasing = False
        for i in range(0, len(level-1)):
            difference = level[i] - level[i+1]
            if abs(difference) < 1 or abs(difference) > 3:
                break
            if increasing == True and decreasing == False and difference < 0:
                break
                    

            else:
                break
            
                
            

            

    return count



main()
