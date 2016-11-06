import idc

def xor(size, key, buff):
    for i in xrange(size):
        addr = buff + i
        temp = idc.Byte(addr) ^ key
        idc.PatchByte(addr, temp)

st = idc.SelStart()
end = idc.SelEnd()

xor(end - st, 0x7a, st)

