
d <- read.csv("~/worldstat/data.csv")

summary(d)

#plot(d)

plot(d$happyness.index.score,d$population)

abline(lm(d$happyness.index.score~d$population), col="red")
lines(lowess(d$happyness.index.score,d$population), col="blue")

# todo...