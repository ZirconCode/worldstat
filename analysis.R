
d <- read.csv("~/worldstat/data.csv")

summary(d)

#plot(d)

plot(d$happyness.index.score,d$population)

abline(lm(d$happyness.index.score~d$population), col="red")
lines(lowess(d$happyness.index.score,d$population), col="blue")

# todo...

eur <- d[d$in.europe == "True",]

plot(eur$perception.of.corruption,eur$population, main="europe only")
abline(lm(eur$perception.of.corruption~eur$population), col="red")
lines(lowess(eur$perception.of.corruption,eur$population), col="blue")


large <- d[d$population >= 100000000,]
plot(large$happyness.index.score,large$population, main="100mil pop only")
lm(large$happyness.index.score~large$population)
abline(lm(large$happyness.index.score~large$population), col="red")     #??
lines(lowess(large$happyness.index.score,large$population), col="blue")

