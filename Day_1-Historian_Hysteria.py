#https://adventofcode.com/2024/day/1
location_list1 = []
location_list2 = []
with open('Day_1-inputs.txt') as f:
    # part 1
    for line in f:
        locations = line.split("   ")
        location_list1.append(int(locations[0]))
        location_list2.append(int(locations[1]))
        
    location_list1.sort()
    location_list2.sort()
    sum = 0
    for i in range(len(location_list1)):
       sum += abs(location_list1[i] - location_list2[i])
    print(sum)
    
    #https://adventofcode.com/2024/day/1#part2

def calculate_simularity_score(list1,list2):
    simularity_score = 0
    location_dict = {}
    
    # initialise locations dictionary
    for location in list1:
        location_dict[location] = 0
    # update occurances
    for location in list2:
        if location in location_dict:
            location_dict[location] += 1
    # calculate score
    
    for location in list1:
        simularity_score += location * location_dict[location]
    
    return simularity_score

print(calculate_simularity_score(location_list1,location_list2))