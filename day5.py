import itertools

def part_1(data):
    fresh_range = []
    food_check = []
    count=0
    for row in data:
        row = row.rstrip().split("-")
        if row==[""]:
            # Always happens in the middle so construct the chain of ranges
            fresh_chain = list(itertools.chain(fresh_range))
            continue

        elif len(row)==2:
            fresh_range.append(range(int(row[0]), int(row[1])+1))
        
        elif len(row)==1:
            food_check.append(int(row[0]))
            for check in fresh_chain:
                if int(row[0]) in check:
                    count+=1
                    break

    return count
    
def part_2(data):
    fresh_range = []
    for row in data:
        row = row.rstrip().split("-")
        if row==[""]:
            break
        
        fresh_range.append(range(int(row[0]), int(row[1])+1))
    
    # sort based start of the range
    fresh_range_sorted = sorted(fresh_range, key=lambda r: r.start)

    val = 0
    last_max=0
    for r in fresh_range_sorted:
        if last_max>r.stop:
            # Already covered this range
            continue
        val+=r.stop-max(r.start, last_max)
        last_max=r.stop
    return val


if __name__=="__main__":
    with open("Inputs/day5.txt") as f:
        data = f.readlines()
    
    answ1 = part_1(data)
    answ2 = part_2(data)
    print(f"Part 1: {answ1}")
    print(f"Part 2: {answ2}")