def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

def is_lhycherl(n):
    m = n
    for i in range(50):
        m += int(str(m)[::-1])
        if is_palindrome(m):
            return False
    else:
        return True

count, L = 0, []
for i in range(1, 10000):
    if is_lhycherl(i):
        count += 1
        L.append(i)

print(count)
