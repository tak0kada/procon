import sys

for line in sys.stdin.readlines()[::-1]:
    s = (" " + line)[-2::-1]
    print(s)
