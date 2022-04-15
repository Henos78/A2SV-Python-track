def swap_case(s):
    return s.swapcase()
# I simply used the method swapcase() to convert the uppercase letters to lowercase and vice versa.
if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result