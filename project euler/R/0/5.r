n <- seq(1,20)

for (i in 1:19){
  for (j in (i+1):20){
    if (n[j]%%n[i] == 0){
      n[j] <- n[j] %/% n[i]
    }
  }
}

print(prod(n))