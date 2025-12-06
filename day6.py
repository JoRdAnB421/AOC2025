from functools import reduce
import operator

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def part_1(data):
    problems = []
    for row in data[:-1]:
        row = [int(i) for i in row.rstrip().split()]
        problems.append(row)

    # Transpose the problems
    problems_T = list(map(list, zip(*problems)))
    
    # Convert operators to functions
    operator_map = {"*": prod,
                    "+": sum}
    opers = data[-1].rstrip().split()    
    opers = [operator_map[i] for i in opers]

    res = [opers[i](problems_T[i]) for i in range(len(problems_T))]
    
    return sum(res)

def part_2(data):
    problems = []
    for row in data[:-1]:
        row = [list(i) for i in row.rstrip("\n").split(r"\s")]
        problems.extend(row)

    # Create map for operators
    operator_map = {"*": prod,
                    "+": sum}
    opers = data[-1].rstrip().split()    
    opers = [operator_map[i] for i in opers]
    
    num_cols = len(problems[0])
    groups=[]
    current_group=[]
    
    for col in range(num_cols):
        # Check if we are at a break point
        if all(row[col]==" " for row in problems):
            # End current group if it has values
            if current_group:
                groups.append(current_group)
                current_group=[]
            
        else:
            # Build the number of this column
            num_str = "".join(row[col] for row in problems if row[col]!=" ")
            current_group.append(int(num_str))
    
    if current_group:
        groups.append(current_group)
    
    res = [opers[i](groups[i]) for i in range(len(groups))]
    
    return sum(res)


if __name__=="__main__":
    with open("Inputs/day6.txt") as f:
        data = f.readlines()

    answ1 = part_1(data)
    answ2 = part_2(data)

    print(f"Part 1 : {answ1}")
    print(f"Part 2 : {answ2}")
