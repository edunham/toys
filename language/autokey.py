#! /usr/bin/env python
import rotN

def make_ints(string):
    return [ord(char) - 96 for char in string.lower()]

def make_chars(ints):
    return ''.join(chr(i+96) for i in ints)

def wrap(ints):
    out = []
    for i in ints:
        if i <= 26:
            out.append(i)
        else:
            out.append(i-26)
    return out

def chunkstring(string, length):
    # http://stackoverflow.com/questions/18854620/whats-the-best-way-to-split-a-string-into-fixed-length-chunks-and-work-with-the
    return (string[0+i:length+i] for i in range(0, len(string), length))

def encode_block(cipher_ints, key_ints):
    # TODO: check whether they're the same length
    out = []
    for i in range(len(cipher_ints)):
        out.append(cipher_ints[i] + key_ints[i] - 1)
    return wrap(out)

def decode_block(cipher_ints, key_ints):
    # TODO: check whether they're the same length
    out = []
    for i in range(len(cipher_ints)):
        new = cipher_ints[i] - key_ints[i] + 1
        if new < 0:
            new += 26
        out.append(new)
    return out

def enc(cipher, key):
    cipher = cipher.lower()
    key = key.lower()
    key_ints = make_ints(key)
    cipher_chunks = chunkstring(cipher, len(key))
    out = ""
    for chunk in cipher_chunks:
        chunk_ints = make_ints(chunk)
        encoded_ints = decode_block(chunk_ints, key_ints)
        out += make_chars(encoded_ints)
        key_ints = encoded_ints

def dec(cipher, key):
    cipher = cipher.lower()
    key = key.lower()
    key_ints = make_ints(key)
    cipher_chunks = chunkstring(cipher, len(key))
    out = ""
    for chunk in cipher_chunks:
        chunk_ints = make_ints(chunk)
        decoded_ints = decode_block(chunk_ints, key_ints)
        out += make_chars(decoded_ints)
        key_ints = decoded_ints
    return out

def derp_dec(cipher, key):
    cipher = cipher.lower()
    key = key.lower()
    key_ints = make_ints(key)
    cipher_chunks = chunkstring(cipher, len(key))
    out = ""
    for chunk in cipher_chunks:
        chunk_ints = make_ints(chunk)
        decoded_ints = decode_block(chunk_ints, key_ints)
        out += make_chars(decoded_ints)
    return out


lanyards = ["LVFU`XAN`YIJ`UVXRB`RKOYOFB",
            "LVFUXANYIJUVXRBRKOYOFB",
            ]
keys = ["stonehg",
        "stonehenge",
        "drummers",
        "drumes",
        "hope",
        "hopeconf",
        "hopehope",
        "eleven",
        ]

#print dec("WMPMMXXAEYHBRYOCA", "KILT")

for l in lanyards:
    for k in keys:
        print l + " " + k
        print "\t"+derp_dec(l.lower(), k)
        #print rotN.derp(dec(l.lower(), k))
