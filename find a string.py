def count_substring(string, sub_string):

    """ so here simply I used the count method to keep track of the similar substrings and traverse it in a loop
    by using the startswith() method which will identify the substring and then increase the count and finally returns
    the substring."""
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print(count)