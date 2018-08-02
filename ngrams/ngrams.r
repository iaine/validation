# Redoing the culturomics 
library(ggplot2)

convert_items <- function (dfA) {
  return(unlist(as.integer(strsplit(as.character(dfA), ','))))
}
#files <- list.files(path="/Users/iain/Desktop/ngram_data/")
yearsdf <- read.table(file = "/Users/iain/Desktop/culturomics/googlebooks-eng-all-1gram-20120701-1", sep="\t", fill = T, quote = "")
total <- read.table(file = "/Users/iain/Desktop/culturomics/googlebooks-eng-all-totalcounts-20120701.txt", header=F, sep="\t", fill = T, quote = "")

total_counts = data.frame(year=integer(), match=integer(), volume=integer(), last=integer())
for (i in total) {
  tmp = convert_items(total$x[i])
  print(tmp)
  counts=data.frame(year=tmp[0], match=tmp[1], volume=tmp[2], last=tmp[3])
  total_counts <- rbind(total_counts, counts)
}

years <- yearsdf[yearsdf$V1 %in% c(1850, 1910, 1950), ]

ggplot(data=years, aes(x=V2, y=V3, col = V1)) + geom_line() + xlab("Years") + ylab("Frequency")
