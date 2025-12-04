from collections import Counter

def part_1(data):
    mymap = dict()
    for y, row in enumerate(data):
        row = row.rstrip()
        for x, ch in enumerate(row):
            mymap[x+1j*y] = ch
    # print(mymap)

    # All allowed movement
    movement = [(-1-1j), (-0-1j), (1-1j), -1, 1, (-1+1j), 1j, (1+1j)]
    count=0
    for pos, val in mymap.items():
        if val!="@":
            continue
        
        around = Counter(map(mymap.get, [move+pos for move in movement]))
        num_ats = around.get("@", 0)

        if num_ats<4:
            count+=1
    
    return count

def part_2(data):
    mymap = dict()
    for y, row in enumerate(data):
        row = row.rstrip()
        for x, ch in enumerate(row):
            mymap[x+1j*y] = ch
    
    movable=True

    # All allowed movement
    movement = [(-1-1j), (-0-1j), (1-1j), -1, 1, (-1+1j), 1j, (1+1j)]
    count=0
    
    # make a copy of the map
    while movable:
        newmap = mymap.copy()
        oldcount=count       
        for pos, val in mymap.items():
            if val!="@":
                continue
            
            # Check how many @'s are around you
            around = Counter(map(mymap.get, [move+pos for move in movement]))
            num_ats = around.get("@", 0)

            if num_ats<4:
                count+=1
                newmap[pos]="."
        
        mymap = newmap
        if oldcount==count:
            movable=False
    return count



if __name__=="__main__":
    with open("Inputs/day4.txt") as f:
        rows = f.readlines()
    
    answ1 = part_1(rows)
    answ2 = part_2(rows)

    print(f"part_1: {answ1}")
    print(f"part_2: {answ2}")