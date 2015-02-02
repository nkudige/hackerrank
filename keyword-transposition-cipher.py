# https://www.hackerrank.com/challenges/keyword-transposition-cipher

letters = [chr(i) for i in xrange(65, 91)]

def get_cipherblock(order, cipher, cols):
    res = []
    """print order
    print cipher
    print cols"""
    
    for i in xrange(cols):
        for j in xrange(order[i][1]):
            print j*cols + order[i][0],
            res.append(cipher[(j*cols + order[i][0])] )

    return res

def remove_repeats(key):
    k = []
    for char in key:
        if char not in k:
            k.append(char)
    return k

def build_cipher(key):
    global letters
    
    key = remove_repeats(key)
    cols = cipherlen = len(key)
    cipher = key[:]

    i = 0
    while cipherlen < 26:
        if letters[i] not in cipher:
            cipher.append(letters[i])
            cipherlen += 1
        i += 1

    return (key, cipher, cols)
    
T = int(raw_input())

for i in xrange(T):
    key = raw_input()
    ciphertext = raw_input()

    (key, cipher, cols) = build_cipher(key)

    key_2 = [[j, key[j], 26/cols] for j in xrange(len(key))]

    print key
    print cipher
    print cols
    print key_2
    
    for j in xrange(26%cols):
        key_2[j][2] += 1

    print key_2
    key_2.sort(key = lambda x: x[1])

    print key_2
    order = [(x[0], x[2]) for x in key_2]

    encipher = get_cipherblock(order, cipher, cols)

    result = ''
    for j in xrange(len(ciphertext)):
        if ciphertext[j] == ' ':
            result += ' '
            continue
        result += letters[encipher.index(ciphertext[j])]

    print result
