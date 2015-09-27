import string
import sys
import md5
import multiprocessing

# list all possible chars 
chars = string.ascii_lowercase + string.digits
# distribute all possible chars to four processes to crack simultaneounsly 
char1 = 'abcdefghi'
char2 = 'klmnopqrs'
char3 = 'tuvwxyz01'
char4 = '23456789j'
#char1 = 'abcdefghijklmnopq'
#char2 = 'rstuvwxyz01234567'
#char3 = '89!"#\$%&\'()*+,-./'
#char4 = ':;<=>?@[\\]^_`{|}~'
#chars = string.ascii_lowercase + string.digits + string.punctuation
# slat string
salt = 'hfT7jp2q'
# given hash value, original from is base64 (22 bits), convert it to 32 bits hex on this website http://cryptii.com/base64/md5
hash = 'd41d8cd98f00b204e9800998ecf8427e'

# compare hash value of guessing passsword with given one 
def compareMd5(password):
    m = md5.new(password+salt)
    if(m.hexdigest() == hash):
        print "crack password" + password
        sys.exit()

# recurse funtion, if password length is larger than 5, then create four processes to speed the cracking, else use one process
# to handle it cuz it won't cost much time
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

# main loop function to guessing password from length 1 to 6.
for baseWidth in range(1, 7):
    print "checking passwords width [" + `baseWidth` + "]"
    recurse(baseWidth, 0, "")

