
# Symmetric difference

# (This one is for python 2)
# Here I created to two sets of integer N and M
N= int(raw_input())
set1 = set(map(int, raw_input().split()))
M = int(raw_input())
set2 = set(map(int, raw_input().split()))

for i in sorted(set1.union(set2)):
    if i is not in set1.intersection(set2):
        print(i)



