#!/usr/bin/python3

import sys

def check_letter(q): # rewrites letters to get to the beginnig of the ascii
    o_rd = ord(q)
    if (o_rd > 57):
        o_rd -= 55
    else:
        o_rd -= 48
    return(o_rd)

def print_things(a): # divides strings and makes AXXXX-AXXXX-AXXXX-AXXXX "Code"
    str = ''
    while (a > 0):
        b = a//26
        c = a - b*26
        d = c + 65
        str += (chr(int(d)))
        a = b
    str += 'A'
    return(str[::-1])

def main_thing(string): # packs the string to the 8 byte code
    substr = {}
    subs = {}
    i=0
    retn =[]
    chars = ''
    while i < len(string):
        upper = (string[0+i:2+i])[0:1]
        lower = (string[0+i:2+i])[1]
        upper_ord = check_letter(upper)
        if (lower == ''):
            pair_or = upper_ord << 4 
        else:
            lower_ord = check_letter(lower)
            pair_or = upper_ord << 4 | lower_ord
        substr[i] = pair_or & 0xff
        retn.append(substr[i])
        i +=2
    return(retn) # returns list of dec numbers

def string_to_bytes(st): # reverts the "Code"
    i=0
    prev_letter = 0
    for letter in st:
        i = i*26 + ord(letter) - 65
    return(hex(i))

def reverse_string(st): # reverts the "Code" given to the 8 bytes code
    for s in st.split('-'):
        print(string_to_bytes(s))

def v5_1(v5):
    v5=1
    return(v5)

def v5_2(v5):
    v5 = v5 | 0x2
    return(v5)

def v5_3(v5):
    v5 = v5 | 0x4
    return(v5)

def v5_4(v5):
    v5 = v5 | 0x8
    return(v5)

def v5_5(v5):
    v5 = v5 | 0x10
    return(v5)

def v5_6(v5):
    v5 = v5 | 0x20
    return(v5)

def v5_7(v5):
    v5 = v5 | 0x40
    return(v5)

def v5_8(v5):
    v5 = v5 | 0x80
    return(v5)

def checksum2(st,v3): # takes '0xXXXXX' string as an input and 0x40 or 0x80
    m_v5={}
    i=0
    do_v = { 0:v5_1, 1:v5_2, 2:v5_3, 3:v5_4, 4:v5_5, 5:v5_6, 6:v5_7, 7:v5_8 }
    while v3:
        v5 = 0
        for c,letter in enumerate(st[::-1]):
            if (ord(letter) & v3):
                v5 = do_v[c](v5)
        m_v5[i]=v5
        i+=1
        v3 = v3 >> 2
    return(m_v5) # returns dictionary of dec numbers

def checksum_2(st,v3): # takes hex number as an input
    m_v5={}
    i=0
    do_v = { 0:v5_1, 1:v5_2, 2:v5_3, 3:v5_4, 4:v5_5, 5:v5_6, 6:v5_7, 7:v5_8 }
    while v3:
        v5 = 0
        for c,s in enumerate(reversed(st)):
            if (int(s,16) & v3):
                v5 = do_v[c](v5)
        m_v5[i]=v5
        i+=1
        v3 = v3 >> 2
    return(m_v5)

def checksum_2a(st,v3): # takes dec numbers as an input
    m_v5={}
    i=0
    do_v = { 0:v5_1, 1:v5_2, 2:v5_3, 3:v5_4, 4:v5_5, 5:v5_6, 6:v5_7, 7:v5_8 }
    while v3:
        v5 = 0
        for c,s in enumerate(reversed(st)):
            if (s & v3):
                v5 = do_v[c](v5)
        m_v5[i]=v5
        i+=1
        v3 = v3 >> 2
    return(m_v5)

# takes dec number as an input
def sub_4dcf20(st:int) -> int: 
    eax=0x80000000
    v3=0
    m_v4 = {}
    while (v3 < 8):
        v4=0
        v5=32
        while v5:
            if (eax & st):
                v4 = v4 | v5
            eax = eax << 1
            if eax > 0x80000000:
                eax = 0x1
            v5 = v5 >> 1
        eax = eax >>2
        v3 +=1
        m_v4[v3] = v4
    return(m_v4) # returns dict of decs

const_548fb8 = {} # first bin mask
const_548fb8 = [0x0,0x10,0x0,0x0,0x20,0x0,0x0,0x0,0x0,0x0,0x1,0x0,0x0,0x0,0x80,0x0,0x0,0x0,0x0,0x80,0x0,0x1,0x0,0x0,0x0,0x0,0x0,0x1,0x0,0x0,0x8,0x0,0x8,0x0,0x0,0x0,0x0,0x20,0x0,0x0,0x0,0x0,0x20,0x0,0x0,0x0,0x0,0x4,0x80,0x0,0x0,0x0,0x0,0x0,0x4,0x0,0x0,0x0,0x0,0x20,0x0,0x4,0x0,0x0,0x4,0x0,0x0,0x0,0x10,0x0,0x0,0x0,0x0,0x0,0x10,0x0,0x0,0x40,0x0,0x0,0x0,0x0,0x0,0x10,0x0,0x0,0x0,0x2,0x2,0x0,0x0,0x0,0x0,0x8,0x0,0x0,0x0,0x0,0x2,0x0,0x0,0x80,0x0,0x0,0x0,0x0,0x0,0x40,0x40,0x0,0x0,0x0,0x0,0x0,0x40,0x0,0x0,0x2,0x0,0x0,0x1,0x0,0x0,0x0]

def loc_4dd082(st:int): # takes dec as an input
    eax = 0
    i = 0
    edx = 1
    while edx < 0x80000000:
        ecx = '0x{}{}{}{}'.format("{0:#0{1}x}".format(const_548fb8[i],4)[2:],"{0:#0{1}x}".format(const_548fb8[i+1],4)[2:],"{0:#0{1}x}".format(const_548fb8[i+2],4)[2:],"{0:#0{1}x}".format(const_548fb8[i+3],4)[2:])
        i_ecx = int(ecx,16)
        if ( i_ecx & st):
            eax = eax | edx
        i += 4
        edx = edx << 1
    return(eax) # returns dec numbers

const_548c70 = {}
const_548c70 = [0x58,0xBA,0x52,0x8,0x5,0xED,0x15,0x80,0x6D,0x7C,0x53,0x83,0xB3,0xBA,0x4F,0xA9,0x12,0x20,0xC4,0xA1,0xFD,0xEC,0x1C,0x1B,0x6D,0xB4,0x7C,0x14,0xC9,0x91,0xB3,0x9,0xD5,0xB6,0xD5,0x9,0xD,0x3C,0xCF,0xF6,0x65,0x93,0x0F,0x3F,0x67,0xC4,0xCA,0xAD,0x0,0x8F,0xA,0xCD,0xA9,0xCF,0x7E,0x6C,0x4A,0x3C,0xAA,0x99,0xF9, 0x94, 0xE7, 0xDB,0x33, 0x4d, 0xa8, 0xdd, 0x00]

const_548cf8 = {}
const_548cf8 = [0x0E,0x00,0x4,0x0F,0x0D,0x7,0x1,0x4,0x2,0x0E,0x0F,0x2,0x0B,0x0D,0x8,0x1,0x3,0x0A,0x0A,0x6,0x6,0x0C,0x0C,0x0B,0x5,0x9,0x9,0x5,0x0,0x3,0x7,0x8,0x4,0x0F,0x1,0x0C,0x0E,0x8,0x8,0x2,0x0D,0x4,0x6,0x9,0x2,0x1,0x0B,0x7,0x0F,0x5,0x0C,0x0B,0x9,0x3,0x7,0x0E,0x3,0x0A,0x0A,0x0,0x5,0x6,0x0,0x0D]

const_548d38 = {}
const_548d38 = [0x0F0,0x30,0x10,0x0D0,0x80,0x40,0x0E0,0x70,0x60,0x0F0,0x0B0,0x20,0x30,0x80,0x40,0x0E0,0x90,0x0C0,0x70,0x0,0x20,0x10,0x0D0,0x0A0,0x0C0,0x60,0x0,0x90,0x50,0x0B0,0x0A0,0x50,0x0,0x0D0,0x0E0,0x80,0x70,0x0A0,0x0B0,0x10,0x0A0,0x30,0x40,0x0F0,0x0D0,0x40,0x10,0x20,0x50,0x0B0,0x80,0x60,0x0C0,0x70,0x60,0x0C0,0x90,0x0,0x30,0x50,0x20,0x0E0,0x0F0,0x90]

const_548d78 = {}
const_548d78 = [0x0A,0x0D,0x0,0x7,0x9,0x0,0x0E,0x9,0x6,0x3,0x3,0x4,0x0F,0x6,0x5,0x0A,0x1,0x2,0x0D,0x8,0x0C,0x5,0x7,0x0E,0x0B,0x0C,0x4,0x0B,0x2,0x0F,0x8,0x1,0x0D,0x1,0x6,0x0A,0x4,0x0D,0x9,0x0,0x8,0x6,0x0F,0x9,0x3,0x8,0x0,0x7,0x0B,0x4,0x1,0x0F,0x2,0x0E,0x0C,0x3,0x5,0x0B,0x0A,0x5,0x0E,0x2,0x7,0x0C]

const_548db8 = {}
const_548db8 = [0x70,0xd0,0xd0,0x80,0xe0,0xb0,0x30,0x50,0x00,0x60,0x60,0x0F0,0x90,0x0,0x0A0,0x30,0x10,0x40,0x20,0x70,0x80,0x20,0x50,0x0C0,0x0B0,0x10,0x0C0,0x0A0,0x40,0x0E0,0x0F0,0x90,0x0A0,0x30,0x60,0x0F0,0x90,0x0,0x0,0x60,0x0C0,0x0A0,0x0B0,0x10,0x70,0x0D0,0x0D0,0x80,0x0F0,0x90,0x10,0x40,0x30,0x50,0x0E0,0x0B0,0x50,0x0C0,0x20,0x70,0x80,0x20,0x40,0x0E0]

const_548df8 = {}
const_548df8 = [0x2,0x0E,0x0C,0x0B,0x4,0x2,0x1,0x0C,0x7,0x4,0x0A,0x7,0x0B,0x0D,0x6,0x1,0x8,0x5,0x5,0x0,0x3,0x0F,0x0F,0x0A,0x0D,0x3,0x0,0x9,0x0E,0x8,0x9,0x6,0x4,0x0B,0x2,0x8,0x1,0x0C,0x0B,0x7,0x0A,0x1,0x0D,0x0E,0x7,0x2,0x8,0x0D,0x0F,0x6,0x9,0x0F,0x0C,0x0,0x5,0x9,0x6,0x0A,0x3,0x4,0x0,0x5,0x0E,0x3]

const_548e38 = {}
const_548e38 = [0x0C0,0x0A0,0x10,0x0F0,0x0A0,0x40,0x0F0,0x20,0x90,0x70,0x20,0x0C0,0x60,0x90,0x80,0x50,0x0,0x60,0x0D0,0x10,0x30,0x0D0,0x40,0x0E0,0x0E0,0x0,0x70,0x0B0,0x50,0x30,0x0B0,0x80,0x90,0x40,0x0E0,0x30,0x0F0,0x20,0x50,0x0C0,0x20,0x90,0x80,0x50,0x0C0,0x0F0,0x30,0x0A0,0x70,0x0B0,0x0,0x0E0,0x40,0x10,0x0A0,0x70,0x10,0x60,0x0D0,0x0,0x0B0,0x80,0x60,0x0D0]

const_548e78 = {}
const_548e78 = [0x4,0x0D,0x0B,0x0,0x2,0x0B,0x0E,0x7,0x0F,0x4,0x0,0x9,0x8,0x1,0x0D,0x0A,0x3,0x0E,0x0C,0x3,0x9,0x5,0x7,0x0C,0x5,0x2,0x0A,0x0F,0x6,0x8,0x1,0x6,0x1,0x6,0x4,0x0B,0x0B,0x0D,0x0D,0x8,0x0C,0x1,0x3,0x4,0x7,0x0A,0x0E,0x7,0x0A,0x9,0x0F,0x5,0x6,0x0,0x8,0x0F,0x0,0x0E,0x5,0x2,0x9,0x3,0x2,0x0C]

const_548eb8 = {}
const_548eb8 = [0x0D0,0x10,0x20,0x0F0,0x80,0x0D0,0x40,0x80,0x60,0x0A0,0x0F0,0x30,0x0B0,0x70,0x10,0x40,0x0A0,0x0C0,0x90,0x50,0x30,0x60,0x0E0,0x0B0,0x50,0x0,0x0,0x0E0,0x0C0,0x90,0x70,0x20,0x70,0x20,0x0B0,0x10,0x40,0x0E0,0x10,0x70,0x90,0x40,0x0C0,0x0A0,0x0E0,0x80,0x20,0x0D0,0x0,0x0F0,0x60,0x0C0,0x0A0,0x90,0x0D0,0x0,0x0F0,0x30,0x30,0x50,0x50,0x60,0x80,0x0B0]

def loc_4dd0e0(eax,edi): # dec nums 
    i = 0
    retn = {}
    a3mi = '0x334da8dd'
    esi = '0x{}{}{}{}'.format("{0:#0{1}x}".format(const_548c70[i],4)[2:],"{0:#0{1}x}".format(const_548c70[i+1],4)[2:],"{0:#0{1}x}".format(const_548c70[i+2],4)[2:],"{0:#0{1}x}".format(const_548c70[i+3],4)[2:])
    while esi != a3mi:
        ebx=edi
        edi=eax
        stcf20 = list(sub_4dcf20(eax).values()) # dec num as an input, values - decs as well
        v2={}
        v2[3] = const_548e78[stcf20[6] ^ const_548c70[6+i] & 0x3f] | const_548eb8[stcf20[7] ^ const_548c70[7+i] & 0x3f]
        v2[2] = const_548df8[stcf20[4] ^ const_548c70[4+i] & 0x3f] | const_548e38[stcf20[5] ^ const_548c70[5+i] & 0x3f]
        v2[1] = const_548d78[stcf20[2] ^ const_548c70[2+i] & 0x3f] | const_548db8[stcf20[3] ^ const_548c70[3+i] & 0x3f]
        v2[0] = const_548cf8[stcf20[0] ^ const_548c70[0+i] & 0x3f] | const_548d38[stcf20[1] ^ const_548c70[1+i] & 0x3f]
        h_v2 = '0x{}{}{}{}'.format("{0:#0{1}x}".format(v2[0],4)[2:],"{0:#0{1}x}".format(v2[1],4)[2:],"{0:#0{1}x}".format(v2[2],4)[2:],"{0:#0{1}x}".format(v2[3],4)[2:])
        eax = loc_4dd082(int(h_v2,16))
        eax = eax ^ ebx
        retn[i] = eax
        i += 4
        esi = '0x{}{}{}{}'.format("{0:#0{1}x}".format(const_548c70[i],4)[2:],"{0:#0{1}x}".format(const_548c70[i+1],4)[2:],"{0:#0{1}x}".format(const_548c70[i+2],4)[2:],"{0:#0{1}x}".format(const_548c70[i+3],4)[2:])
    return(retn) # returns dict of dec nums

def checksum1(st1:int,st2:int): # decs as an input
    v4 = 64
    v5 = 1
    a1 = {}
    a1 = [0,0,0,0,0,0,0,0]
    while v4:
        if (v5 & st1):
            a1[7] = a1[7] | v4
        v5 <<= 1
        if (v5 & st1):
            a1[6] = a1[6] | v4
        v5 <<= 1
        if (v5 & st1):
            a1[5] = a1[5] | v4
        v5 <<= 1
        if (v5 & st1):
            a1[4] = a1[4] | v4
        v5 <<= 1
        if (v5 & st1):
            a1[3] = a1[3] | v4
        v5 <<= 1
        if (v5 & st1):
            a1[2] = a1[2] | v4
        v5 <<= 1
        if (v5 & st1):
            a1[1] = a1[1] | v4
        v5 <<= 1
        if (v5 & st1):
            a1[0] = a1[0] | v4
        v5 <<= 1
        v4 = v4 >> 2
    v4 = 128
    v5 = 1
    while v4:
        if (v5 & st2):
            a1[7] = a1[7] | v4
        v5 <<= 1
        if (v5 & st2):
            a1[6] = a1[6] | v4
        v5 <<= 1
        if (v5 & st2):
            a1[5] = a1[5] | v4
        v5 <<= 1
        if (v5 & st2):
            a1[4] = a1[4] | v4
        v5 <<= 1
        if (v5 & st2):
            a1[3] = a1[3] | v4
        v5 <<= 1
        if (v5 & st2):
            a1[2] = a1[2] | v4
        v5 <<= 1
        if (v5 & st2):
            a1[1] = a1[1] | v4
        v5 <<= 1
        if (v5 & st2):
            a1[0] = a1[0] | v4
        v5 <<= 1
        v4 = v4 >> 2
    return a1 # decs as an output

def checksum_3(st):
    m_v5={}
    i=0
    v3=128
    do_v = { 0:v5_1, 1:v5_2, 2:v5_3, 3:v5_4, 4:v5_5, 5:v5_6, 6:v5_7, 7:v5_8 }
    st = list(st.values())
    while i < 3:
        v5 = 0
        for c,s in enumerate(reversed(st)):
            if (s & v3):
                v5 = do_v[c](v5)
                #print('[edi+{}] -> {}'.format(7-c,v5))
        m_v5[i]=v5
        i+=1
        v3 = v3 >> 1
    v6 = 0 
    rv = list(reversed(st))
    for c,s in enumerate(reversed(st)):
        if c < 4:
            if (s & v3):
                v6 = do_v[c](v6)
    m_v5[3]=v6
    result = 2
    i = 4
    while 3 < i < 7:
        v5 = 0
        for c,s in enumerate(reversed(st)):
            if (s & result):
                v5 = do_v[c](v5)
                #print('[edi+{}] -> {}'.format(7-c,v5))
        m_v5[i]=v5
        i+=1
        result *= 2
    v6 = 0
    for c,s in enumerate(rv):
        if c > 3:
            if (s & result):
                v6 = do_v[c-4](v6)
    m_v5[7]=v6
    return(m_v5)

const_548cac = [0x20,0x00,0x0,0x0,0x1,0x0,0x0,0x4,0x0,0x0,0x0,0x0,0x80,0x0,0x1,0x0,0x0,0x0,0x10,0x0,0x0,0x0,0x4,0x0,0x0,0x0,0x0,0x0,0x0,0x8,0x0,0x40,0x0,0x0,0x20,0x0,0x0,0x0,0x0,0x0,0x10,0x0,0x0,0x2,0x0,0x0,0x0,0x0,0x40,0x0,0x0,0x0,0x4,0x0,0x0,0x8,0x0,0x0,0x8,0x0,0x0,0x0,0x0,0x0,0x0,0x2,0x80,0x0,0x0,0x0,0x0,0x80,0x0,0x0,0x40,0x0,0x0,0x0,0x0,0x0,0x0,0x4,0x0,0x0,0x8,0x0,0x0,0x10,0x0,0x0,0x2,0x0,0x0,0x0]
const_548ef8 = [0x00,0x10,0x0,0x0,0x0,0x0,0x80,0x0,0x4,0x0,0x0,0x0,0x0,0x1,0x0,0x0,0x0,0x0,0x4,0x0,0x0,0x0,0x0,0x4,0x2,0x0,0x0,0x0,0x0,0x8,0x0,0x0,0x0,0x0,0x40,0x0,0x0,0x0,0x1,0x0,0x10,0x0,0x0,0x0,0x0,0x0,0x8,0x0,0x0,0x80,0x0,0x0,0x0,0x0,0x10,0x0,0x0,0x4,0x0,0x0,0x0,0x0,0x0,0x8,0x20,0x0,0x0,0x0,0x0,0x0,0x0,0x1,0x0,0x0,0x2,0x0,0x0,0x20,0x0,0x0,0x0,0x0,0x20,0x0,0x80,0x0,0x0,0x0,0x1,0x0,0x0,0x0,0x8,0x0,0x0,0x0]
const_548f58 = [0x00,0x20,0x00,0x00,0x0,0x0,0x1,0x0,0x0,0x4,0x0,0x0,0x0,0x0,0x80,0x0,0x1,0x0,0x0,0x0,0x10,0x0,0x0,0x0,0x4,0x0,0x0,0x0,0x0,0x0,0x0,0x8,0x0,0x40,0x0,0x0,0x20,0x0,0x0,0x0,0x0,0x0,0x10,0x0,0x0,0x2,0x0,0x0,0x0,0x0,0x40,0x0,0x0,0x0,0x4,0x0,0x0,0x8,0x0,0x0,0x8,0x0,0x0,0x0,0x0,0x0,0x0,0x2,0x80,0x0,0x0,0x0,0x0,0x80,0x0,0x0,0x40,0x0,0x0,0x0,0x0,0x0,0x0,0x4,0x0,0x0,0x8,0x0,0x0,0x10,0x0,0x0,0x2,0x0,0x0,0x0]

def counter(st1,st2): # takes decs
    v3 = 0
    v4 = 0
    i=0
    retn = {}
    while v4 < 4:
        v5 = 0
        result = 32
        while result:
            dword_548F58 = '0x{}{}{}{}'.format("{0:#0{1}x}".format(const_548f58[i*4+3],4)[2:],"{0:#0{1}x}".format(const_548f58[i*4+2],4)[2:],"{0:#0{1}x}".format(const_548f58[i*4+1],4)[2:],"{0:#0{1}x}".format(const_548f58[i*4],4)[2:])
            if (st1 & int(dword_548F58,16)):
                v5 |= result
            result >>= 1
            i +=1
        #print("{0:#0{1}x}".format(v5,4))
        retn[v4]=v5
        v4 +=1
    i=0
    while v4 < 8:
        v9 = 0
        result = 32
        while result:
            dword_548ef8 = '0x{}{}{}{}'.format("{0:#0{1}x}".format(const_548ef8[i*4+3],4)[2:],"{0:#0{1}x}".format(const_548ef8[i*4+2],4)[2:],"{0:#0{1}x}".format(const_548ef8[i*4+1],4)[2:],"{0:#0{1}x}".format(const_548ef8[i*4],4)[2:])
            if (st2 & int(dword_548ef8,16)):
                v9 |= result
            result >>= 1
            i +=1
        #print("{0:#0{1}x}".format(v9,4))
        retn[v4]=v9
        v4 += 1
    return(retn) # returns dict of decs

def loc_4dd6b2(ebx:int,edi:int):
    v3 = edi; # lower@checksum_3
    v4 = ebx; # upper@checksum_3
    v5 = esi = 0;
    loc_res=[]
    while v5 < 16:
      if v5 > 0:
          v7 = 0
          while v7 < 2:
              if ( v4 & 0x8000000 ):
                  v4 = 2 * v4 | 1
              else:
                  v4 *= 2
              if ( v3 & 0x8000000 ):
                  v3 = 2 * v3 | 1
              else:
                  v3 *= 2
              if v5 < 2:
                  break
              if v5 == 8:
                  break
              if v5 == 15:
                  break
              v7 +=1
      loc_res.extend(counter(v4,v3).values())
      #print(loc_res)
      v5 += 1
    return(loc_res)

def loc_4dd714(eax,edi):
    i = 0
    ebp = 0x10
    retn = {}
    while ebp:
        ebx=edi
        edi=eax
        stcf20 = list(sub_4dcf20(eax).values())
        v2={}
        v2[3] = hex(const_548e78[stcf20[6] ^ din_548c70[6+i] & 0x3f] | const_548eb8[stcf20[7] ^ din_548c70[7+i] & 0x3f])
        v2[2] = hex(const_548df8[stcf20[4] ^ din_548c70[4+i] & 0x3f] | const_548e38[stcf20[5] ^ din_548c70[5+i] & 0x3f])
        v2[1] = hex(const_548d78[stcf20[2] ^ din_548c70[2+i] & 0x3f] | const_548db8[stcf20[3] ^ din_548c70[3+i] & 0x3f])
        v2[0] = hex(const_548cf8[stcf20[0] ^ din_548c70[0+i] & 0x3f] | const_548d38[stcf20[1] ^ din_548c70[1+i] & 0x3f])
        h_v2 = '0x{}{}{}{}'.format("{0:#0{1}x}".format(int(v2[0],16),4)[2:],"{0:#0{1}x}".format(int(v2[1],16),4)[2:],"{0:#0{1}x}".format(int(v2[2],16),4)[2:],"{0:#0{1}x}".format(int(v2[3],16),4)[2:])
        eax = loc_4dd082(int(h_v2,16))
        eax = eax ^ ebx
        retn[i] = eax
        i += 8
        ebp -= 1
    return(retn)

def inter(st):
    f_chks2_1 = checksum2(st,0x40)
    f_chks2_2 = checksum2(st,0x80)
    f_chks_st_1 = '0x{}{}{}{}'.format("{0:#0{1}x}".format(f_chks2_1[3],4)[2:],"{0:#0{1}x}".format(f_chks2_1[2],4)[2:],"{0:#0{1}x}".format(f_chks2_1[1],4)[2:],"{0:#0{1}x}".format(f_chks2_1[0],4)[2:])
    f_chks_st_2 = '0x{}{}{}{}'.format("{0:#0{1}x}".format(f_chks2_2[3],4)[2:],"{0:#0{1}x}".format(f_chks2_2[2],4)[2:],"{0:#0{1}x}".format(f_chks2_2[1],4)[2:],"{0:#0{1}x}".format(f_chks2_2[0],4)[2:])
    dict1 = loc_4dd0e0(int(f_chks_st_2,16),int(f_chks_st_1,16))
    list_dict1 = list(dict1.values())
    ld_st1=list_dict1[-1]
    ld_st2=list_dict1[-2]
    chks2 = checksum1(ld_st1,ld_st2)
    return(chks2)

def first_stage(string):
    st=string[:8]
    first=inter(st)
    st=string[8:]
    second=inter(st)
    result={}
    i=0
    while i<8:
        result[i]=first[i]^second[i]
        i += 1
    final_result =[]
    j=0
    chksm_3=checksum_3(result)
    high_at_chksm_3='0x{}{}{}{}'.format("{0:#0{1}x}".format(chksm_3[3],4)[2:],"{0:#0{1}x}".format(chksm_3[2],4)[2:],"{0:#0{1}x}".format(chksm_3[1],4)[2:],"{0:#0{1}x}".format(chksm_3[0],4)[2:])
    low_at_chksm_3='0x{}{}{}{}'.format("{0:#0{1}x}".format(chksm_3[7],4)[2:],"{0:#0{1}x}".format(chksm_3[6],4)[2:],"{0:#0{1}x}".format(chksm_3[5],4)[2:],"{0:#0{1}x}".format(chksm_3[4],4)[2:])
    din_548c70=loc_4dd6b2(int(high_at_chksm_3,16),int(low_at_chksm_3,16))
    return(din_548c70)

def second_stage(string):
    bytes_from_Code=main_thing(string)
    low_at_chksm_2 = checksum_2a(bytes_from_Code,0x40)
    low_at_chks_2 = '0x{}{}{}{}'.format("{0:#0{1}x}".format(low_at_chksm_2[3],4)[2:],"{0:#0{1}x}".format(low_at_chksm_2[2],4)[2:],"{0:#0{1}x}".format(low_at_chksm_2[1],4)[2:],"{0:#0{1}x}".format(low_at_chksm_2[0],4)[2:])
    high_at_chksm_2 = checksum_2a(bytes_from_Code,0x80)
    high_at_chks_2 = '0x{}{}{}{}'.format("{0:#0{1}x}".format(high_at_chksm_2[3],4)[2:],"{0:#0{1}x}".format(high_at_chksm_2[2],4)[2:],"{0:#0{1}x}".format(high_at_chksm_2[1],4)[2:],"{0:#0{1}x}".format(high_at_chksm_2[0],4)[2:])
    resresres = list(loc_4dd714(int(high_at_chks_2,16),int(low_at_chks_2,16)).values())
    chks2 = checksum1(resresres[-1],resresres[-2])
    retn=[hex(num) for num in chks2]
    return(retn)

def second_stage1(string):
    bytes_from_Code=string
    low_at_chksm_2 = checksum_2a(bytes_from_Code,0x40)
    low_at_chks_2 = '0x{}{}{}{}'.format("{0:#0{1}x}".format(low_at_chksm_2[3],4)[2:],"{0:#0{1}x}".format(low_at_chksm_2[2],4)[2:],"{0:#0{1}x}".format(low_at_chksm_2[1],4)[2:],"{0:#0{1}x}".format(low_at_chksm_2[0],4)[2:])
    high_at_chksm_2 = checksum_2a(bytes_from_Code,0x80)
    high_at_chks_2 = '0x{}{}{}{}'.format("{0:#0{1}x}".format(high_at_chksm_2[3],4)[2:],"{0:#0{1}x}".format(high_at_chksm_2[2],4)[2:],"{0:#0{1}x}".format(high_at_chksm_2[1],4)[2:],"{0:#0{1}x}".format(high_at_chksm_2[0],4)[2:])
    resresres = [hex(num) for num in loc_4dd714(int(high_at_chks_2,16),int(low_at_chks_2,16)).values()]
    chks2 = checksum1(int(resresres[-1],16),int(resresres[-2],16))
    retn=[hex(num) for num in chks2]
    return(retn)

verify_st = [ '0x44', '0xb6', '0xf8', '0xf1', '0x1', '0x8', '0x1b', '0xff' ]

def gen_matrix():
    v5 = 1
    w,h = 4,8
    Matrix = [[0 for x in range(w)] for y in range(h)]
    for iter in range(w):
        for pos in range(h):
            Matrix[pos][iter]=v5
            v5 <<= 1
    return(Matrix)

matrix = gen_matrix()

def rev_chks1_or_high(x,c):
    binx = format(x,'08b')
    m = 0
    if binx[1] == '1':
        m = m | matrix[c][0]
    if binx[3] == '1':
        m = m | matrix[c][1]
    if binx[5] == '1':
        m = m | matrix[c][2]
    if binx[7] == '1':
        m = m | matrix[c][3]
    return(m)

def rev_chks1_or_low(x,c):
    binx = format(x,'08b')
    m = 0
    if binx[0] == '1':
        m = m | matrix[c][0]
    if binx[2] == '1':
        m = m | matrix[c][1]
    if binx[4] == '1':
        m = m | matrix[c][2]
    if binx[6] == '1':
        m = m | matrix[c][3]
    return(m)


def rev_chks1(inp):
    retn = {}
    st1 = 0
    st2 = 0
    matrix = gen_matrix()
    for c,t in enumerate(reversed(inp)):
        st1 = st1 | rev_chks1_or_high(t,c)
        st2 = st2 | rev_chks1_or_low(t,c)
    retn[1] = st1
    retn[2] = st2
    return(retn)

def f2(eax,i):
    i = i * 8
    stcf20 = list(sub_4dcf20(eax).values())
    v2={}
    v2[3] = hex(const_548e78[stcf20[6] ^ din_548c70[6+i] & 0x3f] | const_548eb8[stcf20[7] ^ din_548c70[7+i] & 0x3f])
    v2[2] = hex(const_548df8[stcf20[4] ^ din_548c70[4+i] & 0x3f] | const_548e38[stcf20[5] ^ din_548c70[5+i] & 0x3f])
    v2[1] = hex(const_548d78[stcf20[2] ^ din_548c70[2+i] & 0x3f] | const_548db8[stcf20[3] ^ din_548c70[3+i] & 0x3f])
    v2[0] = hex(const_548cf8[stcf20[0] ^ din_548c70[0+i] & 0x3f] | const_548d38[stcf20[1] ^ din_548c70[1+i] & 0x3f])
    h_v2 = '0x{}{}{}{}'.format("{0:#0{1}x}".format(int(v2[0],16),4)[2:],"{0:#0{1}x}".format(int(v2[1],16),4)[2:],"{0:#0{1}x}".format(int(v2[2],16),4)[2:],"{0:#0{1}x}".format(int(v2[3],16),4)[2:])
    eax = loc_4dd082(int(h_v2,16))
    return(eax)

def rev_4dd714(eax16,eax15):
    retn = {}
    eax14 = eax16 ^ f2(eax15,15)
    retn[15] = eax14
    eax13 = eax15 ^ f2(eax14,14)
    retn[14] = eax13
    eax12 = eax14 ^ f2(eax13,13)
    retn[13] = eax12
    eax11 = eax13 ^ f2(eax12,12)
    retn[12] = eax11
    eax10 = eax12 ^ f2(eax11,11)
    retn[11] = eax10
    eax9 = eax11 ^ f2(eax10,10)
    retn[10] = eax9
    eax8 = eax10 ^ f2(eax9,9)
    retn[9] = eax8
    eax7 = eax9 ^ f2(eax8,8)
    retn[8] = eax7
    eax6 = eax8 ^ f2(eax7,7)
    retn[7] = eax6
    eax5 = eax7 ^ f2(eax6,6)
    retn[6] = eax5
    eax4 = eax6 ^ f2(eax5,5)
    retn[5] = eax4
    eax3 = eax5 ^ f2(eax4,4)
    retn[4] = eax3
    eax2 = eax4 ^ f2(eax3,3)
    retn[3] = eax2
    eax1 = eax3 ^ f2(eax2,2)
    retn[2] = eax1
    eax0 = eax2 ^ f2(eax1,1)
    retn[1] = eax0
    edi = eax1 ^ f2(eax0,0)
    retn[0] = edi
    return(retn)

def rev_chks2(high,low):
    a = [0,0,0,0,0,0,0,0]
    i = 0
    h_high = hex(high)
    h_low = hex(low)
    ah_high = ['0x{}'.format(h_high[2:4]),'0x{}'.format(h_high[4:6]),'0x{}'.format(h_high[6:8]),'0x{}'.format(h_high[8:10])]
    ah_low = ['0x{}'.format(h_low[2:4]),'0x{}'.format(h_low[4:6]),'0x{}'.format(h_low[6:8]),'0x{}'.format(h_low[8:10])]
    ha_high = ah_high[::-1]
    ha_low = ah_low[::-1]
    b_m = {}
    b_m[128] = format(int(ha_high[0],16),'08b')
    b_m[32] = format(int(ha_high[1],16),'08b')
    b_m[8] = format(int(ha_high[2],16),'08b')
    b_m[2] = format(int(ha_high[3],16),'08b')
    b_m[64] = format(int(ha_low[0],16),'08b')
    b_m[16] = format(int(ha_low[1],16),'08b')
    b_m[4] = format(int(ha_low[2],16),'08b')
    b_m[1] = format(int(ha_low[3],16),'08b')
    while i < 8:
        if b_m[128][i] == '1':
            a[i] = a[i] | 128
        if b_m[32][i] == '1':
            a[i] = a[i] | 32
        if b_m[8][i] == '1':
            a[i] = a[i] | 8
        if b_m[2][i] == '1':
            a[i] = a[i] | 2
        if b_m[64][i] == '1':
            a[i] = a[i] | 64
        if b_m[16][i] == '1':
            a[i] = a[i] | 16
        if b_m[4][i] == '1':
            a[i] = a[i] | 4
        if b_m[1][i] == '1':
            a[i] = a[i] | 1
        i += 1
    return(a)

def reverse_this(a):
    b = [int(num,16) for num in a]
    r_chks1 = rev_chks1(b).values()
    r_4dd714 = rev_4dd714(list(r_chks1)[0],list(r_chks1)[1])
    r_chks2 = rev_chks2(r_4dd714[1],r_4dd714[0])
    retn = ["{0:#0{1}x}".format(num,4) for num in r_chks2]
    return(retn)

if len(sys.argv) > 1:
	string = sys.argv[1]
	string = string.upper()
	din_548c70 = first_stage(string)
	b = reverse_this(verify_st)
	c = '\nActivation code: {}{}{}{}{}{}{}{}'.format(b[0][2:],b[1][2:],b[2][2:],b[3][2:],b[4][2:],b[5][2:],b[6][2:],b[7][2:]).upper()
	print(c)
else:
	print('\nUsage: python this_script.py <environment_code>')
	sys.exit(2)
