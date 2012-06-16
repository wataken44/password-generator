#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" password.py


"""

import sys
import getopt
import random
import hashlib
import codecs

class UniformGenerator(object):
    def __init__(self, key):
        sha = hashlib.sha256()
        s = '%s uniform salt hoge chocolate zyxwvut %s' % (key, key)
        sha.update(s.encode('utf-8'))
        seed = int(sha.hexdigest(), 16)
        random.seed(seed)

    def generate(self, length):
        # without l, O
        alpha = "abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ"
        num = "0123456789"

        arr = []
        nnum = random.randint(1, 3)
        for i in range(nnum):
            arr.append(random.choice(num))
            
        for i in range(length - nnum):
            arr.append(random.choice(alpha))
        
        random.shuffle(arr)
        return "".join(arr)
                
def main():
    key = ""
    length = 8
    gen = "Uniform"

    opts, args = getopt.gnu_getopt(sys.argv[1:], 'l:g:')
    for o,a in opts:
        if o == 'l':
            length = int(a)
    
    key = args[0]

    generator = UniformGenerator(key) 
    
    for i in range(4):
        print(generator.generate(length))

if __name__ == "__main__":
    main()
