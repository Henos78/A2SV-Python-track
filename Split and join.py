def split_and_join(line):
    # I just used the replace method which will replace all the spaces with the hyphen mark
    return line.replace(" ","-")

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
