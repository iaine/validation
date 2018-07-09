# Put a cluster dendrogram using the MFW data
# to try and reproduce the Stanford Literary Leaflet
library(jsonlite)

d = read.table('/Users/iain/Documents/phd/standford_pamphlets/data/MFW/GenreWordData.txt', fill = TRUE)

x<-hclust(dist(d), method = "complete", members = NULL)

png('/Users/iain/Desktop/cluster.png', width=10800, height = 1200, units = 'px')

plot(x, labels = NULL, hang = 0.1, check = TRUE,
     axes = TRUE, frame.plot = FALSE, ann = TRUE,
     main = "Reproducing the Standford Leaflet 1 Cluster Dendrogram",
     sub = NULL, xlab = 'Words', ylab = "Number")
dev.off()