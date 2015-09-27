import string
import sys
import md5
import multiprocessing

#char1 = 'abcdefghijklmnopq'
char1 = 'abcdefghi'
char2 = 'klmnopqrs'
char3 = 'tuvwxyz01'
char4 = '23456789j'
#char2 = 'rstuvwxyz01234567'
#char3 = '89!"#\$%&\'()*+,-./'
#char4 = ':;<=>?@[\\]^_`{|}~'
#chars = string.ascii_lowercase + string.digits + string.punctuation
chars = string.ascii_lowercase + string.digits
salt = 'hfT7jp2q'
#hash = 'd6b4d8a2aadb433abcc06b2b9afbf5b5'
hash = 'd41d8cd98f00b204e9800998ecf8427e'

def compareMd5(password):
    m = md5.new(password+salt)
    if(m.hexdigest() == hash):
        print "crack password" + password
        sys.exit()

def recurse1(width, position, baseString):
    for char in char1:
        if(position < width -1):
            recurse(width, position + 1, baseString + char)
        compareMd5(baseString + char)

def recurse2(width, position, baseString):
    for char in char2:
        if(position < width -1):
            recurse(width, position + 1, baseString + char)
        compareMd5(baseString + char)

def recurse3(width, position, baseString):
    for char in char3:
        if(position < width -1):
            recurse(width, position + 1, baseString + char)
        compareMd5(baseString + char)

def recurse4(width, position, baseString):
    for char in char4:
        if(position < width -1):
            recurse(width, position + 1, baseString + char)
        compareMd5(baseString + char)

def recurse(width, position, baseString):
    if(width > 4 and position == 0):
        print "create processes"
        p1 = multiprocessing.Process(target=recurse1, args=(width, position, baseString))
        p1.start()
        p2 = multiprocessing.Process(target=recurse2, args=(width, position, baseString))
        p2.start()
        p3 = multiprocessing.Process(target=recurse3, args=(width, position, baseString))
        p3.start()
        p4 = multiprocessing.Process(target=recurse4, args=(width, position, baseString))
        p4.start()
    else:
        for char in chars:
            if(position < width -1):
                recurse(width, position + 1, baseString + char)
            compareMd5(baseString + char)

for baseWidth in range(1, 7):
    print "checking passwords width [" + `baseWidth` + "]"
    recurse(baseWidth, 0, "")

