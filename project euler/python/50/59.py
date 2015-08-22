def encrypt(cipher, keys):
    txt = [0] * len(cipher)
    for i, key in enumerate(keys):
        xor = lambda x: key ^ x
        txt[i::len(keys)] = map(xor, cipher[i::len(keys)])
    return txt

with open("cipher1.txt", 'r') as f:
    cipher = f.read()
    cipher = map(int, cipher.split(','))

key_cands = [[], [], []]
for i in range(3):
    for j in range(97, 123):
        for k in map(lambda ci: ci ^ j, cipher[i::3]):
            if not (k == ord('\n') or 31 < k < 127):
                break
        else:
            key_cands[i].append(j)

for i in key_cands[len(cipher) % 3][:]:
    if i ^ cipher[-1] not in map(ord, ('\n', '.', '!', '?', ')')):
        key_cands[0].remove(i)

cs_max = 0
for i in key_cands[0]:
    for j in key_cands[1]:
        for k in key_cands[2]:
            txt = encrypt(cipher, (i, j, k))
            cs = txt.count(ord(' '))
            if cs > cs_max:
                cs_max, ans = cs, txt

print(sum(ans))
print("".join(map(chr, ans)))
