

# The If-Else question

# To solve this problem, I used the If-elif condition.
import math
import os
import random
import re
import sys

# The raw input is just a random input which is given in hackerrank.
if __name__ == '__main__':
    n = int(raw_input().strip())

    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird ")
    elif n % 2 == 0 and n > 5 and n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

    """ This one is the one I submitted on hacker rank (Basically it's almost the same but I was a bit confused at first
     about raw_input().strip() but now I get it. """
