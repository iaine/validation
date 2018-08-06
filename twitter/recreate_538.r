library(ggplot2)

twitter_data <- read.csv('russian-troll-tweets/IRAhandle_tweets.csv?raw=true')

df2 <- data.frame(table(format(as.Date(twitter_data$publish_date, "%d/%m/%Y"), "%Y-%m")))

#png('/Users/iain/Desktop/538all.png', width=1080, height = 540, units = 'px')

#ggplot(data=df2, aes(x=Var1, y=Freq)) + geom_bar(stat = "identity") + 
#  xlab("Month") + 
#  theme(axis.text.x = element_text(angle = 90, hjust = 1))
#dev.off()

tags <- twitter_data[twitter_data$account_category == "HashtagGamer", ]
df_tags <- data.frame(table(format(as.Date(tags$publish_date, "%d/%m/%Y"), "%Y-%m")))

png('/Users/iain/Desktop/538gamer.png', width=1080, height = 540, units = 'px')

ggplot() + 
  geom_bar(stat = "identity", fill = "Black", data=df2, aes(x=Var1, y=Freq)) +
  geom_bar(stat = "identity", fill = "Purple", data=df_tags, aes(x=Var1, y=Freq)) + 
  xlab("Month") + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1))
dev.off()
