
def part_1(data):
    mymap = dict()
    for y, row in enumerate(data):
        row = row.rstrip()
        for x, ch in enumerate(row):
            mymap[x+1j*y] = ch
            if ch=="S":
                # Record the start point
                start=x+1j*y
    
    positions = [start]
    splits=0
    for row in range(1, len(data)):
        new_positions = []
        for pos in positions:
            new_pos = pos+1j
            if mymap.get(new_pos)==".":
                new_positions.append(new_pos)

            elif mymap.get(new_pos)=="^":
                splits+=1
                new_pos = [new_pos-1, new_pos+1]
                new_positions.extend(new_pos)

        positions = list(set(new_positions))
    return splits

def part_2_a(data):
    mymap = dict()
    for y, row in enumerate(data):
        row = row.rstrip()
        for x, ch in enumerate(row):
            mymap[x+1j*y] = ch
            if ch=="S":
                # Record the start point
                start=x+1j*y
    
    pos_dict = dict.fromkeys(mymap.keys(), 0)
    pos_dict[start]=1
    positions = [start]
    for row in range(1, len(data)):
        new_positions = []
        for pos in positions:
            new_pos = pos+1j
            if mymap.get(new_pos)==".":
                new_positions.append(new_pos)
                pos_dict[new_pos] += pos_dict[pos]

            elif mymap.get(new_pos)=="^":
                new_pos = [new_pos-1, new_pos+1]
                new_positions.extend(new_pos)

                for p in new_pos:
                    if pos_dict.get(p)==0:
                        pos_dict[p] = pos_dict[pos]
                    else:
                        pos_dict[p] += pos_dict[pos]


        positions = list(set(new_positions))

    unis = [pos_dict[val] for val in positions]
    return sum(unis)


def part_2(data):
    # Get starting position
    start = data[0].rstrip().find("S")
    beams = [0] * len(data[0])
    beams[start] = 1
    
    # Run through data
    for line in data[1:]:
        for i, char in enumerate(line):
            if char != "^":
                continue
                
            beams[i + 1] += beams[i]
            beams[i - 1] += beams[i]
            beams[i] = 0
    
    return sum(beams)

if __name__=="__main__":
    with open("Inputs/day7.txt") as f:
        rows = f.readlines()

    answ1 = part_1(rows)
    answ2 = part_2(rows)
    answ2a = part_2_a(rows)

    print(f"part 1 : {answ1}")
    print(f"part 2 : {answ2}")
    print(f"part 2a : {answ2a}")