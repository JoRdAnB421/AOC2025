import re

def part_1(data):
    count=0
    for line in data:
        line = line.strip()

        # Find max number
        max_num = max(line[:-1])

        # find the first position of the max_num and search the latter part
        pos = re.search(rf"{max_num}", line).span()[0]    
        
        next_max = max(line[pos+1:])

        val = int(max_num+next_max)
        count+=val

    return count


def part_2(data):
    count=0
    for line in data:
        line = line.strip()
        # Find max number
        max_num = max(line[:-11]) # Requires a 12 digit number
        val = max_num
        last_pos=0
        
        for i in range(11,0,-1):
            # find the first position of the max_num and search the latter part
            # up to the latest in the string it could be
            pos = re.search(rf"{max_num}", line[last_pos:-i]).span()[0]    
            last_pos+=pos+1
            if -i+1!=0:
                next_max = max(line[last_pos:-i+1])
            else:
                next_max = max(line[last_pos:])

            val += next_max
            max_num=next_max

        val = int(val)
        count+=val

    return count

if __name__=="__main__":
    with open("Inputs/day3.txt") as f:
        lines = f.readlines()

        data = [line.strip() for line in lines]

    answ1 = part_1(data)
    answ2 = part_2(data)

    print(f"part_1 : {answ1}")
    print(f"part_2 : {answ2}")
