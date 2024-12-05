# https://adventofcode.com/2024/day/5
import itertools
def split_rules_and_pages(file_name):
    file = open(file_name).read()
    return(file.split("\n\n"))
def update_rules_dict(key, value, rules_dict):
        if key in rules_dict:
            rules_dict[key].append(value)
        else:
            rules_dict[key] = [value]
            
def create_rules_dicts(rules):
    forward_rules_dict= {}
    backward_rules_dict = {}
    combined_rules_dicts = [forward_rules_dict,backward_rules_dict] #hold references of dicts
    rules_list = rules.split("\n")
    for rule in rules_list:
        rule_pair = rule.split("|")
        update_rules_dict(rule_pair[0], rule_pair[1], forward_rules_dict)
        update_rules_dict(rule_pair[1], rule_pair[0], backward_rules_dict)
    return [forward_rules_dict, backward_rules_dict]

def create_updates_list(updates_str):
    updates_str_list = updates_str.split("\n")
    updates_list_list = [update.split(",") for update in updates_str_list]
    return(updates_list_list)


def check_update_compliance(rules_dicts, update):
    for i in range(len(update)):
        current_page = update[i]
        if current_page in rules_dicts[0]:
            infront_pages = rules_dicts[0][current_page]
            for page in infront_pages:
                if page in update and update.index(page) < update.index(current_page):
                    return False
        elif current_page in rules_dicts[1]:
            behind_pages = rules_dicts[1][current_page]
            for page in behind_pages:            
                if page in update and update.index(page) > update.index(current_page):
                    return False         
    return True

def find_compliant_updates(rules_dicts, update_list):
    compliant_updates = []
    for update in update_list:
        if check_update_compliance(rules_dicts, update) == True:
            compliant_updates.append(update)
    return compliant_updates

def find_non_compliant_updates(rules_dicts, update_list):
    compliant_updates = []
    for update in update_list:
        if check_update_compliance(rules_dicts, update) == False:
            compliant_updates.append(update)
    return compliant_updates

def make_update_compliant(rules_dicts, update):
    for i in range(len(update)):
        current_page = update[i]
        if current_page in rules_dicts[0]:
            infront_pages = rules_dicts[0][current_page]
            for page in infront_pages:
                if page in update and update.index(page) < update.index(current_page):
                    update[update.index(current_page)] = "deleting"
                    update.insert(update.index(page),current_page)
                    update.remove("deleting")
        elif current_page in rules_dicts[1]:
            behind_pages = rules_dicts[1][current_page]
            for page in behind_pages:            
                if page in update and update.index(page) > update.index(current_page):
                    update[update.index(page)] = "deleting"
                    # print(update, current_page)
                    update.insert(update.index(current_page),page)
                    update.remove("deleting")

    return update
def brute_force_compliance(rules_dicts, update):
    all_possibilities =  list(itertools.permutations(update))
    print("permutations: ", len(all_possibilities))
    for possiblity in all_possibilities:
        if check_update_compliance(rules_dicts, possiblity):
            return(possiblity)
    print("what>")
    
def make_all_updates_compliant(rules_dicts, update_list):
    compliant_updates = []
    count = 0
    for update in update_list:
            compliant_updates.append(make_update_compliant(rules_dicts, update))
            # print(f"progress: ${count} of ${len(update_list)} ")
    return compliant_updates   
    
# file_name = "Day 5 sample inputs.txt"
file_name = "Day 5 inputs.txt"
split_file = split_rules_and_pages(file_name)
# print("split_file", split_file)
rules_dicts = create_rules_dicts(split_file[0])
print(rules_dicts)
updates_list_list = create_updates_list(split_file[1])
# print("update", updates_list_list)
compliant_updates = find_compliant_updates(rules_dicts, updates_list_list)
# print(compliant_updates)
sum_middle = sum([int(update[len(update)//2]) for update in compliant_updates if update[0] != ''])
print("final answer p1", sum_middle)

# part 2
non_compliant_updates = find_non_compliant_updates(rules_dicts, updates_list_list)
made_compliant_updates = make_all_updates_compliant(rules_dicts, non_compliant_updates)
print(made_compliant_updates)
print( find_compliant_updates(rules_dicts, made_compliant_updates))
sum_middle = sum([int(update[len(update)//2]) for update in made_compliant_updates if update[0] != ''])
print("final answer p2", sum_middle)
print()