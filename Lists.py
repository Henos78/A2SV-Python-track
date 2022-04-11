if __name__ == '__main__':
    # Created an empty list to store the values
    list1 = []
    N = int(raw_input())
    for i in range(N):
        # oprn stands for operations (more like the type of methods it will use within the program)
        oprn = list(raw_input().split())
        # I will use the if- elif condition to execute the required prompts

        # This will add elements into the list
        if oprn[0] == "insert":
            a, b = map(int, (oprn[1], oprn[2]))
            list1.insert(a, b)

        # This will print the elements in the list
        elif oprn[0] == "print":
            print(list1)

        # This will remove elements from the list
        elif oprn[0] == "remove":
            list1.remove(int(oprn[1]))

        # This will add new elements to the list
        # The difference between insert and append is that the insert method will help us to add values
        # with a preferred position

        elif oprn[0] == "append":
            list1.append(int(oprn[1]))

        # This will sort our list
        elif oprn[0] == "sort":
            list1.sort()

        # deletes elements from our list
        # The difference between pop and remove is that pop uses the index as a parameter to remove
        # the element whereas remove uses the value as a parameter
        elif oprn[0] == "pop":
            list1.pop()

        # This will reverse the order of our elements in our list
        elif oprn[0] == "reverse":
            list1.reverse()


