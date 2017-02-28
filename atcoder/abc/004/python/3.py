t = int(input())
s = "123456"

for i in range(t//5):
    s = s[1:] + s[0]

for i in range(t % 5):
    s = s[:i] + s[i+1] + s[i] + s[i+2:]

print(int(s))
