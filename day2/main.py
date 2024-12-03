#Red-Nosed reports

def main():
    data = convert_input_to_list("test.txt")
    safe_count = iteration(data)
    print(safe_count)

def convert_input_to_list(file_path):
    input_list = []
    with open(file_path, 'r') as file:
        for line in file:
            input_list.append([int(x) for x in line.split()])
    return input_list

def iteration(input_list):
    safe_count = 0
    for level in input_list:
        if check_up(level):
            if check_inc_dec(level):
                safe_count +=1
        elif check_down(level):
            if check_inc_dec(level):
                safe_count +=1
    return safe_count
        
        
def check_up(level):
    for i in range(0, len(level)-1):
        if level[i] > level[i+1]:
            return False
    return True

def check_down(level) :
    for i in range(0, len(level)-1):
        if level[i] < level[i+1]:
            return False
    return True   

def check_inc_dec(level):
    for i in range(0, len(level)-1):
        if abs(level[i] -level[i+1]) > 3 or abs(level[i] - level[i+1]) < 1:
            return False
    return True

            
    
            



main()
