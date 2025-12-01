def part_1(data):
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
    return count_zeros


def part_2(data):
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
            # Avoid double counting when turning left from 0
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
    return count_zeros


if __name__=="__main__":
    with open("Inputs/day1.txt", "r") as f:
        data = []
        for line in f.readlines():
            data.append(line.strip())

    res_1 = part_1(data)
    print(f"Part 1 answer = {res_1}")

    res_2 = part_2(data)
    print(f"Part 2 answer = {res_2}")