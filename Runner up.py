
# The runner up question
if __name__ == '__main__':
    n = int(raw_input())
    list1 = list(map(int, raw_input().split()))
    # First I sorted the list using the sort method
    list1.sort()
    # Then I assigned a variable last1 to represent the last element in the list
    last1 = list1[-1]
    # I used the method .sort(reverse= True) to sort the values in a descending order
    list1.sort(reverse=True)
    # I used a for loop to itterate through the list and find the second highest value
    for i in list1:
        if i != last1:
            print(i)
            break



