m <- 0
for (i in 100:999){
  for (j in i:999){
    str <- as.character(i*j)
    tmp_rev <- rev(strsplit(str, NULL)[[1]])
    str_rev <- paste(tmp_rev, collapse='')
    if (str == str_rev){
      m <- max(m, i*j)
    }
  }
}
print(m)