import md5
import base64
import string

b64_str='./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
final_str=""

def b64_from_24bit(a, b ,c ,d):
    global final_str
    w = (ord(a)<<16)|(ord(b)<<8)|ord(c)
    for i in range(0, d):
        final_str+=b64_str[w & 0x3f]
        w = w >> 6

m=md5.new('chfT7jp2qc')
m_tem=m.digest()
m=md5.new('c$1$hfT7jp2q'+m_tem[0])
key='c'
length=len(key)
while(length>0):
    if(length &1 !=0):
        m.update('\0')
        print 1
    else:
        m.update(key[0])
        print 2

    length>>=1

m_alt=m.digest()
print base64.encodestring(m_alt)
for i in range(0, 1000):
    if( i&1 != 0):
        m=md5.new('c')
    else:
        m=md5.new(m_alt)

    if(i % 3 != 0):
        m.update('hfT7jp2q')

    if(i % 7 != 0):
        m.update('c')

    if(i & 1 !=0):
        m.update(m_alt)
    else:
        m.update('c')

    m_alt=m.digest()
    print base64.encodestring(m.digest())

b64_from_24bit(m_alt[0],m_alt[6],m_alt[12],4)
b64_from_24bit(m_alt[1],m_alt[7],m_alt[13],4)
b64_from_24bit(m_alt[2],m_alt[8],m_alt[14],4)
b64_from_24bit(m_alt[3],m_alt[9],m_alt[15],4)
b64_from_24bit(m_alt[4],m_alt[10],m_alt[5],4)
b64_from_24bit('0','0',m_alt[11],2)

