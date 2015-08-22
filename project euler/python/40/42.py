sumOfWords=0
with open("words.txt") as f:
    W = f.read()
    for w in W.split(","):
        if isTriangle(wordvalue(w[1:-1])): sumOfWords+=1
print sumOFWords
