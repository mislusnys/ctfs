# Global vars 
v1 = 0
v2 = 0
v3 = 9
v4 = 0

#word_40A140
final_key = [0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0, 0]
key = [0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0, 0]

def reset_():
    global key, v1, v2, v3, v4
    v1 = 0
    v2 = 0
    v3 = 9
    v4 = 0
    key = list(final_key)

rawdump = [
  0x00, 0x00, 0x21, 0x00, 0x02, 0x00, 0x00, 0x00, 0x91, 0x00, 
  0x08, 0x00, 0x00, 0x00, 0x16, 0x00, 0x00, 0x00, 0x0C, 0x00, 
  0x09, 0x00, 0x0A, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x0C, 0x00, 0x02, 0x00, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x1D, 0x00, 0x0A, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x63, 0x00, 0x02, 0x00, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x18, 0x00, 0x06, 0x00, 0x00, 0x00, 0x54, 0x00, 0x08, 0x00, 
  0x00, 0x00, 0x33, 0x00, 0x00, 0x00, 0x29, 0x00, 0x09, 0x00, 
  0x0A, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2C, 0x00, 
  0x02, 0x00, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3D, 0x00, 
  0x0A, 0x00, 0x00, 0x00, 0x0E, 0x00, 0x01, 0x00, 0x0B, 0x00, 
  0x00, 0x00, 0x00, 0x00, 0x59, 0x00, 0x02, 0x00, 0x0C, 0x00, 
  0x00, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x0C, 0x00, 0x01, 0x00, 0x00, 0x00, 0x09, 0x00, 0x0C, 0x00, 
  0x00, 0x00, 0x0B, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x00, 
  0x02, 0x00, 0x0C, 0x00, 0x01, 0x00, 0x0B, 0x00, 0x00, 0x00, 
  0x00, 0x00, 0x01, 0x00, 0x03, 0x00, 0x0C, 0x00, 0x00, 0x00, 
  0x0B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 
  0x00, 0x00, 0x47, 0x00, 0x00, 0x00, 0x60, 0x00, 0x09, 0x00, 
  0x0A, 0x00, 0x0C, 0x00, 0x00, 0x00, 0x0B, 0x00, 0x01, 0x00, 
  0x03, 0x00, 0x00, 0x00, 0x5D, 0x00, 0x08, 0x00, 0x00, 0x00, 
  0x7C, 0x00, 0x00, 0x00, 0x6E, 0x00, 0x09, 0x00, 0x0A, 0x00, 
  0x0B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x00, 0x03, 0x00, 
  0x0C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5B, 0x00, 0x0C, 0x00, 
  0x01, 0x00, 0x00, 0x00, 0x87, 0x00, 0x0A, 0x00, 0x00, 0x00, 
  0x36, 0x00, 0x0C, 0x00, 0x01, 0x00, 0x0B, 0x00, 0x00, 0x00, 
  0x0B, 0x00, 0x01, 0x00, 0x02, 0x00, 0x0C, 0x00, 0x01, 0x00, 
  0x0B, 0x00, 0x01, 0x00, 0x00, 0x00, 0x58, 0x00, 0x02, 0x00, 
  0x06, 0x00, 0x00, 0x00, 0xF9, 0x00, 0x08, 0x00, 0x00, 0x00, 
  0xA0, 0x00, 0x00, 0x00, 0x96, 0x00, 0x09, 0x00, 0x0A, 0x00, 
  0x0B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x4D, 0x00, 0x06, 0x00, 
  0x0C, 0x00, 0x00, 0x00, 0x00, 0x00, 0xAE, 0x00, 0x0A, 0x00, 
  0x00, 0x00, 0x23, 0x03, 0x00, 0x00, 0x2B, 0x01, 0x03, 0x00, 
  0x0C, 0x00, 0x01, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x0B, 0x00, 
  0x01, 0x00, 0x02, 0x00, 0x0C, 0x00, 0x01, 0x00, 0x0C, 0x00, 
  0x01, 0x00, 0x0B, 0x00, 0x01, 0x00, 0x0B, 0x00, 0x01, 0x00, 
  0x00, 0x00, 0x01, 0x00, 0x03, 0x00, 0x0C, 0x00, 0x01, 0x00, 
  0x00, 0x00, 0x03, 0x00, 0x02, 0x00, 0x0B, 0x00, 0x01, 0x00, 
  0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0xB2, 0x00, 
  0x00, 0x00, 0xC7, 0x00, 0x09, 0x00, 0x0A, 0x00, 0x07, 0x00, 
  0x00, 0x00, 0x77, 0xFE, 0x08, 0x00, 0x00, 0x00, 0xD8, 0x00, 
  0x00, 0x00, 0xD1, 0x00, 0x09, 0x00, 0x0A, 0x00, 0x0B, 0x00, 
  0x00, 0x00, 0x00, 0x00, 0x58, 0x00, 0x02, 0x00, 0x0C, 0x00, 
  0x00, 0x00, 0x00, 0x00, 0x03, 0x00, 0x04, 0x00, 0x00, 0x00, 
  0x8C, 0x00, 0x02, 0x00, 0x00, 0x00, 0x94, 0x60, 0x08, 0x00, 
  0x00, 0x00, 0xEE, 0x00, 0x00, 0x00, 0xE7, 0x00, 0x09, 0x00, 
  0x0A, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x00, 0x00, 0xE7, 0x00, 
  0x02, 0x00, 0x0C, 0x00, 0x00, 0x00, 0x0B, 0x00, 0x01, 0x00, 
  0x02, 0x00, 0x00, 0x00, 0x0C, 0x00, 0x06, 0x00, 0x00, 0x00, 
  0x74, 0x00, 0x08, 0x00, 0x00, 0x00, 0x07, 0x01, 0x00, 0x00, 
  0xFD, 0x00, 0x09, 0x00, 0x0A, 0x00, 0x0B, 0x00, 0x00, 0x00, 
  0x00, 0x00, 0x09, 0x00, 0x03, 0x00, 0x0C, 0x00, 0x00, 0x00, 
  0x00, 0x00, 0x1D, 0x01, 0x0A, 0x00, 0x00, 0x00, 0x0A, 0x00, 
  0x0C, 0x00, 0x01, 0x00, 0x0B, 0x00, 0x01, 0x00, 0x00, 0x00, 
  0x01, 0x00, 0x03, 0x00, 0x0C, 0x00, 0x01, 0x00, 0x0B, 0x00, 
  0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 
  0x0B, 0x01, 0x00, 0x00, 0x1D, 0x01, 0x09, 0x00, 0x0A, 0x00, 
  0x00, 0x00, 0x06, 0x00, 0x05, 0x00, 0x00, 0x00, 0xC0, 0x1D, 
  0x08, 0x00, 0x00, 0x00, 0x33, 0x01, 0x00, 0x00, 0x29, 0x01, 
  0x09, 0x00, 0x0A, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x71, 0x00, 0x02, 0x00, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x3D, 0x01, 0x0A, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x77, 0x00, 0x02, 0x00, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x3D, 0x01, 0x0A, 0x00, 0x00, 0x00, 0x16, 0x00, 0x02, 0x00, 
  0x00, 0x00, 0x0E, 0x00, 0x03, 0x00, 0x00, 0x00, 0x61, 0x00, 
  0x08, 0x00, 0x00, 0x00, 0x53, 0x01, 0x00, 0x00, 0x4C, 0x01, 
  0x09, 0x00, 0x0A, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x2C, 0x00, 0x03, 0x00, 0x0C, 0x00, 0x00, 0x00, 0x0C, 0x00, 
  0x01, 0x00, 0x0B, 0x00, 0x01, 0x00, 0x00, 0x00, 0x2C, 0x21, 
  0x0B, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x03, 0x00, 
  0x0C, 0x00, 0x01, 0x00, 0x00, 0x00, 0x07, 0x00, 0x03, 0x00, 
  0x0B, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 
  0x00, 0x00, 0x59, 0x01, 0x00, 0x00, 0x6E, 0x01, 0x09, 0x00, 
  0x0A, 0x00, 0x00, 0x00, 0xCA, 0x01, 0x06, 0x00, 0x00, 0x00, 
  0xF5, 0x1F, 0x08, 0x00, 0x00, 0x00, 0x81, 0x01, 0x00, 0x00, 
  0x7A, 0x01, 0x09, 0x00, 0x0A, 0x00, 0x0B, 0x00, 0x00, 0x00, 
  0x00, 0x00, 0x12, 0x00, 0x02, 0x00, 0x0C, 0x00, 0x00, 0x00, 
  0x0D, 0x00, 0x0A, 0x25, 0x73, 0x0A, 0x00, 0x00, 0x00, 0x00, 
  0x30, 0xE1, 0x40, 0x00, 0x88, 0xE1, 0x40, 0x00, 0x28, 0x00, 
  0x6E, 0x00, 0x75, 0x00, 0x6C, 0x00, 0x6C, 0x00, 0x29, 0x00, 
  0x00, 0x00, 0x00, 0x00, 0x28, 0x6E, 0x75, 0x6C, 0x6C, 0x29, 
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 
  0x00, 0x01, 0x00, 0x00, 0x10, 0x00, 0x03, 0x06, 0x00, 0x06, 
  0x02, 0x10, 0x04, 0x45, 0x45, 0x45, 0x05, 0x05, 0x05, 0x05, 
  0x05, 0x35, 0x30, 0x00, 0x50, 0x00, 0x00, 0x00, 0x00, 0x28, 
  0x20, 0x38, 0x50, 0x58, 0x07, 0x08, 0x00, 0x37, 0x30, 0x30, 
  0x57, 0x50, 0x07, 0x00, 0x00, 0x20, 0x20, 0x08, 0x00, 0x00, 
  0x00, 0x00, 0x08, 0x60, 0x68, 0x60, 0x60, 0x60, 0x60, 0x00, 
  0x00, 0x78, 0x70, 0x78, 0x78, 0x78, 0x78, 0x08, 0x07, 0x08, 
  0x00, 0x00, 0x07, 0x00, 0x08]

mem = [ rawdump[i] + rawdump[i+1] * 0x100 for i in xrange(0, 0x37a, 2)]

def dbg():
    print hex(v1), hex(v2), hex(v3), hex(v4)

def sub_401000(char):
    global v3
    global key
    v3 += 1
    key[v3] = char
    return v3 + 1

def sub_401080():
    global v3
    r = key[v3]
    v3 -= 1
    return r

## Functions f1-f14

def f1():
    global v4
    v4 +=1
    r = sub_401000(mem[v4])
    v4 +=1
    return r

def f2():
    global v4
    v4 += 1
    return sub_401080()

def f3():
    global v4
    v0 = sub_401080()
    v1 = sub_401080()
    sub_401000(v1 + v0)
    v4 += 1
    return v4 + 1

def f4():
    global v4
    v0 = sub_401080()
    v1 = sub_401080()
    sub_401000(v1 - v0)
    v4 += 1
    return v4 + 1

def f5():
    global v4
    v0 = sub_401080()
    v1 = sub_401080()
    sub_401000(((v1 << (16 - v0)) | (v1 >> v0)) & 0xFFFF)
    v4 += 1
    return v4 + 1

def f6():
    global v4
    v0 = sub_401080()
    v1 = sub_401080()
    sub_401000(((v1 >> (16 - v0)) | (v1 << v0)) & 0xFFFF)
    v4 += 1
    return v4 + 1

def f7():
    global v4
    v0 = sub_401080()
    v1 = sub_401080()
    sub_401000(v1 ^ v0)
    v4 += 1
    return v4 + 1

def f8():
    global v4
    v0 = sub_401080()
    r = sub_401000(~v0 & 0xFFFF)
    v4 += 1
    return r

def f9():
    global v4
    v0 = sub_401080()
    if v0 == sub_401080():
        r = sub_401000(1)
    else:
        r = sub_401000(0)
    v4 += 1
    return r


def f10():
    global v4
    v2 = sub_401080()
    v1 = sub_401080()
    if sub_401080() == 1:
        sub_401000(v2)
    else:
        sub_401000(v1)
    v4 += 1
    return v4 + 1

def f11():
    global v4
    r = sub_401080()
    v4 = r
    return r

def f12():
    global v1, v2, v3, v4
    v4 += 1
    if mem[v4] == 0:
        r = sub_401000(v1)
    elif mem[v4] == 1:
        r = sub_401000(v2)
    elif mem[v4] == 2:
        r = sub_401000(v3)
    else:
        r = sub_401000(v4)
    v4 += 1
    return r


def f13():
    global v1, v2, v3, v4    
    v4 += 1
    temp = mem[v4]
    new = sub_401080()
    if temp == 0:
        v1 = new
    elif temp == 1:
        v2 = new
    elif temp == 2:
        v3 = new
    elif temp == 3:
        v4 = new
    else:
        v4 += 1
        return v4 + 1
    v4 += 1
    return v4 + 1

def f14():
    global v4
    v4 += 1
    return v4 + 1

# Function list

func = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14]

def sub_401540():
    global v4
    v0 = mem[v4]
    return func[v0]()

def sub_401610():
    global v1, v2, v3, v4
    while (v4 < 0x182):
        sub_401540()
    return v1

## Key calculation
arg = ''
for i in reversed(xrange(10)):
    reset_()
    first = sub_401610()
    for ch in xrange(0x21, 0x7f):
        reset_()
        key[i] = ch
        r = sub_401610()
        if r != first:
            arg += chr(ch)
            final_key[i] = ch
            break

print arg[::-1]
