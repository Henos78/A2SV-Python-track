# Nested Lists Question

# Created an empty list for the records and grades
records = []
grades = []

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    # This is increases the count (It is more like doing the same thing as append method)
    records += [[name, score]]
    grades += [score]

""" Assigned a variable 'b' to the sorted values with reads the second element by changing to a set and 
then returning it back to list."""
b = sorted(list(set(grades)))[1]
# Sorted the records and iterated it using a for loop
for a, c in sorted(records):
    if c == b:
        print(a)
