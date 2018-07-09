# Script to run PCA 
library(ggplot2)
library(jsonlite)

f = read.csv('/Users/iain/Documents/phd/standford_pamphlets/data/Docuscope/Group1WholeNovelsDocuscopeClusterFigure6.1.txt')

df<-f[3:20]
PC<-prcomp(df)
PCi<-data.frame(PC$x, Words=f$Group)
jsonpc <- write_json(PCi, '/Users/iain/Desktop/pca.json')

png('/Users/iain/Desktop/pca.png', width=1080, height = 1080, units = 'px')
ggplot(PCi,aes(x=PC1,y=PC2, col = Words))+
  geom_point(size=3,alpha=0.5)+
  theme_classic()
dev.off()