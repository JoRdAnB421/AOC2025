with open("Inputs/day1.txt", "r") as f:
    data = []
    for line in f.readlines():
        data.append(line.strip())

count_zeros=0
pos=50 # Start pointing at 50 
for turn in data:
    # Check direction
    if turn[0]=="R":
        direction=1
    else:
        direction=-1

    # Check turn amount
    num = int(turn[1:])
    pos = (pos + direction*num) % 100

    if pos==0:
        count_zeros+=1

print(f"Part 1: Number of zeros = {count_zeros}")

## Part 2
count_zeros=0
pos=50
for turn in data:
    # Check direction
    if turn[0]=="R":
        direction=1
    else:
        direction=-1

    # Check turn amount
    num = int(turn[1:])
    new_pos = (pos + direction*num) % 100

    if (pos==0)&(num<100):
        # Avoid double counting when turning left
        pos=new_pos
        continue

    if direction==1:
        # right turn
        leftover_turn = num - (100-pos)
    else:
        # left turn
        leftover_turn = num - pos
    
    if leftover_turn>=0:
        count_zeros += 1 + leftover_turn//100
        if (pos==0)&(direction==-1):
            count_zeros-=1
    
    pos = new_pos


print(f"Part 2: Number of zeros = {count_zeros}")