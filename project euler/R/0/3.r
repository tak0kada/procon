N <- 600851475143
for (i in 2:sqrt(N)){
  while (N %% i == 0){
    N <- N %/% i
  }
  if (N == 1){
    print(i)
    break
  }
}