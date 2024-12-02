# Day1
# Psuedocode
# Accept two lists
# Order lists
# Find difference (distance) between two lists
# return total distance
def main():
    file_path = "input.txt"
    first_s, second_s, counter = split_and_sort_data(file_path)
    tot_distance = calculate_distance(first_s, second_s, counter)
    print(f"Total distance between two lists: {tot_distance}") 
    sim_score = similarity_score(first_s, second_s, counter)
    print(f"Similarity score between two lists: {sim_score}")

def split_and_sort_data(file_path):
    first = []
    second = []
    counter = 0
    with open(file_path, 'r') as file:
        for line in file:
            first.append(int(line.split()[0]))
            second.append(int(line.split()[1]))
            counter += 1
    first_s = sorted(first)
    second_s = sorted(second)
    return first_s, second_s, counter

def calculate_distance(first_s, second_s, counter):
    total_distance = 0
    for i in range(counter):
        total_distance += (max(first_s[i], second_s[i]))-(min(first_s[i], second_s[i]))
    return total_distance
            
def similarity_score(first_s, second_s, counter):
    sim_counter = 0
    score = 0
    for num in first_s:
        sim_counter = 0
        for num2 in second_s:
            if num == num2:
                sim_counter += 1
        score += (num*sim_counter)
    return score

    

main()
    
    
    
    

