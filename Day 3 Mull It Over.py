# https://adventofcode.com/2024/day/3
import re
text = open("Day 3 inputs.txt").read()
print(text)
pattern = r"({do|don\'t)mul\((\d{1,3},\d{1,3})\)"
matches = re.findall(pattern,text)
sum_mult = 0
for mult_pair in matches:
    pair = mult_pair.split(",")
    mult = int(pair[0]) * int(pair[1])
    sum_mult += mult
    
print(sum_mult)

#part 2
mult_pattern = r"mul\((\d{1,3},\d{1,3})\)"
condtional_pattern= r"(do|don't)\(\).*?"
mult_matches = list(re.finditer(mult_pattern,text))
conditional_matches = list(re.finditer(condtional_pattern,text))
# combine 2 list than sort
reformatted_sequence = mult_matches + conditional_matches
reformatted_sequence = [[match.start(),match.group(1)] for match in reformatted_sequence]
reformatted_sequence.sort()

#calculate
reject = False
sum_mult = 0
for instruction in reformatted_sequence:
    if instruction[1] == "don't":
        reject = True
    elif instruction[1] == "do":
        reject = False
    else:
        if reject == False:
            pair = instruction[1].split(",")
            mult = int(pair[0]) * int(pair[1])
            sum_mult +=  mult
print(sum_mult)