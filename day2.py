import re

def part_1(data):
    # Split into the ranges and explode each
    data = data[0].split(",")

    # Find all values in the ranges and convert to one list of strings
    string_split = "-"
    string_list = []
    for i in data:
        low, high = i.split("-")
        val_range = range(int(low), int(high)+1)
        
        for val in val_range:
            string_list.append(str(val))

    string_vals = string_split.join(string_list)
    
    # Match cases of number blocks repeated exactly twice
    pattern = re.compile(r"(?:^|-)((\d+)\2(?!\2))(?:$|-)")
    matches = re.findall(pattern, string_vals)

    # Count the resulting invalid ids
    count = 0
    for m in matches:
        count+=int(m[0])
    
    return count

def part_2(data):
    # Split into the ranges and explode each
    data = data[0].split(",")

    # Find all values in the ranges and convert to one list of strings
    string_split = "-"
    string_list = []
    for i in data:
        low, high = i.split("-")
        val_range = range(int(low), int(high)+1)
        
        for val in val_range:
            string_list.append(str(val))

    string_vals = string_split.join(string_list)
    
    # Match cases of number blocks repeated exactly twice
    pattern = re.compile(r"(?:^|-)((\d+)\2+)(?:$|-)")
    matches = re.findall(pattern, string_vals)

    # Count the resulting invalid ids
    count = 0
    for m in matches:
        count+=int(m[0])
    
    return count

if __name__=="__main__":
    with open("Inputs/day2.txt") as f:
        data = f.readlines()

    count = part_1(data)    
    print(f"Part 1 : {count}")


    count = part_2(data)    
    print(f"Part 2 : {count}")