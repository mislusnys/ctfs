import base64
import binascii

key = 'flareon_is_so_cute'

target = 'ErZVpc7xaW3bf0h8ythQz62wRdQlMpg3nTEKPYsyE9OtxAU4fCbwYg8zfbxlTnLb3BpLkcSSeuiskPQoEeyrEdZts9jKxSRiiYlr0Q/PDPhri78Sm4vTsUx/ascx7lt0EEvP5YsvQTjW2QvS1+3dyk7x8c8QlQ=='

def rc4(data, key):
    """RC4 encryption and decryption method."""
    S, j, out = range(256), 0, []

    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    for ch in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(chr(ord(ch) ^ S[(S[i] + S[j]) % 256]))

    return "".join(out)

target_hex = base64.b64decode(target)
length = len(target_hex)

s = ''
for i in xrange(length):
    for char in xrange(0x20, 0x7f):
        current = s + chr(char)
        if rc4(current, key)[i] == target_hex[i]:
            s += chr(char)
            break

print s
