fib <- function(n){
  f1 <- 1; f2 <- 2
  if (n == 1) f1
  else if (n == 2) f2
  else {
    for (i in 1:(n-2)){
      tmp.f1 <- f1; f1 <- f2; f2 <- tmp.f1 + f2
    }
    f2
  }
}

sum <- 0
n <- 2

while (TRUE) {
  if (fib(n) > 4000000) break
  else {
    sum <- sum + fib(n)
    n <- n + 4
  }
}

print(sum)