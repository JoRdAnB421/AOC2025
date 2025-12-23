import csv
import math
from functools import reduce
from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra

def merge_sets(sets):
    uf = UnionFind()

    # Union all elements within each set
    for s in sets:
        it = iter(s)
        first = next(it, None)
        for x in it:
            uf.union(first, x)

    # Collect connected components
    merged = defaultdict(set)
    for s in sets:
        for x in s:
            merged[uf.find(x)].add(x)

    return list(merged.values())

def part_1(data):
    data = [tuple(map(int, row)) for row in data]
    
    dists = []
    coord_pairs = []
    for i, coord_1 in enumerate(data[:-1]):
        for coord_2 in data[i+1:]:
            dists.append(math.dist(coord_1, coord_2))
            coord_pairs.append(set({coord_1, coord_2}))


    # sort coordinate pairs by distance 
    coord_pairs_sorted = [x for _,x in sorted(zip(dists, coord_pairs))][:1000]

    circuits = merge_sets(coord_pairs_sorted)

    # sort the sets based on size
    circuit_size = sorted([len(cir) for cir in circuits])
    # print(circuit_size)
    return reduce(lambda x,y: x*y, circuit_size[-3:])

def part_2(data):
    data = [tuple(map(int, row)) for row in data]
    
    dists = []
    coord_pairs = []
    for i, coord_1 in enumerate(data[:-1]):
        for coord_2 in data[i+1:]:
            dists.append(math.dist(coord_1, coord_2))
            coord_pairs.append(set({coord_1, coord_2}))


    coord_pairs_sorted = [x for _,x in sorted(zip(dists, coord_pairs))]
    # sort coordinate pairs by distance
    all_incl=False
    size=1
    while not all_incl:
        size+=1
        part_coord_pairs_sorted = coord_pairs_sorted[:size]

        circuits = merge_sets(part_coord_pairs_sorted)

        if (len(circuits)==1)&(len(circuits[0])==len(data)):
            all_incl=True
    
    x_dist_vals = [i[0] for i in part_coord_pairs_sorted[-1]]
    return x_dist_vals[0]*x_dist_vals[1]

if __name__=="__main__":
    with open("Inputs/day8.csv") as f:
        reader = csv.reader(f, delimiter=",")
        data = [row for row in reader]

    answ1 = part_1(data)
    answ2 = part_2(data)

    print(f"Part 1 : {answ1}")
    print(f"Part 2 : {answ2}")