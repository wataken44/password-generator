#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" password.py


"""

import sys
import getopt
import random
import hashlib
import codecs
import getpass

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
    show_secret = False

    opts, args = getopt.gnu_getopt(sys.argv[1:], 'l:g:s')
    for o,a in opts:
        if o == '-l':
            length = int(a)
        if o == '-s':
            show_secret = True

    if len(args) == 0:
        print('key required')
        sys.exit(1)
    
    secret = getpass.getpass('Secret: ')
    confirm = getpass.getpass('Secret(again): ')
    if secret != confirm:
        print('secret unmatch')
        sys.exit(1)
    
    key = str(length) + args[0] + secret

    generator = UniformGenerator(key) 
    
    for i in range(4):
        print(generator.generate(length))

    if show_secret:
        print('Used secret was %s'%secret)

if __name__ == "__main__":
    main()
