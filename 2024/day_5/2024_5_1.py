# Define the rules and updates based on the problem example
import os


input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.readlines()

    ## remove /n
lines = [line.replace("\n", "") for line in lines]

    ## first part
break_point = 0

for line in lines:
    if line == "":
        break
    break_point += 1

rules_raw = lines[:break_point]
updates_raw = lines[break_point + 1 :]

# Parse rules into tuples of integers
rules = [tuple(map(int, rule.split('|'))) for rule in rules_raw]

# Parse updates into lists of integers
updates = [list(map(int, update.split(','))) for update in updates_raw]

# Helper function to validate an update against the rules
def is_valid_update(update, rules):
    index_map = {page: idx for idx, page in enumerate(update)}  # Map page numbers to their indices
    for x, y in rules:
        if x in index_map and y in index_map:  # Only consider rules for pages in the update
            if index_map[x] >= index_map[y]:  # Check if x comes before y
                return False
    return True

# Process updates
valid_middle_pages = []

for update in updates:
    if is_valid_update(update, rules):
        middle_page = update[len(update) // 2]  # Find the middle page
        valid_middle_pages.append(middle_page)

# Calculate the sum of valid middle pages
sum_of_middle_pages = sum(valid_middle_pages)
sum_of_middle_pages
print(sum_of_middle_pages)