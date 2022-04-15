def mutate_string(string, position, character):
    # Here I simply used the approach given to me in the brief as an example first to slice it and then joining it
    return string[:position]+ character + string[(position+1):]


if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new