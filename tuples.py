if __name__ == '__main__':
    # I used the tuple method to create a tuple and printed the value using the hash() function to display the hash value
    # It will only work for immutable objects such as tuple but wont work for mutable objects
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print(hash(integer_list))