library(ggplot2)
library(data.table) 
library(dplyr)
library(moments)


files <- list.files(path = "C:/Users/Jonas Lind/Desktop/p4Data/CSV files",pattern = ".csv", full.names = TRUE)
temp <- lapply(files, fread, sep=";",encoding = 'UTF-8', check.names = FALSE)
data <- rbindlist( temp )
dataOutliers <- filter(data, data$ReactionTime < 10, data$ReactionTime > 0.3 )
dataOutliers$Female <- NULL

##_________________________The big sad_____________________________________________##
##_________________________Taking means of accuracy and reaction time for individual sounds______##

allMonsterGrowl <- dataOutliers %>% filter_all(any_vars(. %in% c('Monster growl')))
meanSpeedMonsterGrowl <- mean(allMonsterGrowl$ReactionTime)
meanAccMonsterGrowl <- mean(allMonstergrowl$Precision)

allStikkontakt <- dataOutliers %>% filter_all(any_vars(. %in% c('Stikkontakt')))
meanSpeedStikkontakt <- mean(allStikkontakt$ReactionTime)
meanAccStikkontakt <- mean(allStikkontakt$Precision)

allChatter <- dataOutliers %>% filter_all(any_vars(. %in% c('Chatter')))
meanSpeedChatter <- mean(allChatter$ReactionTime)
meanAccChatter <- mean(allChatter$Precision)

allHarpFloursih <- dataOutliers %>% filter_all(any_vars(. %in% c('Harp floursih')))
meanSpeedHarpFlourish <- mean(allHarpFloursih$ReactionTime)
meanAccHarpFlourish <- mean(allHarpFloursih$Precision)

allManScream <- dataOutliers %>% filter_all(any_vars(. %in% c('Man scream')))
meanSpeedManScream <- mean(allManScream$ReactionTime)
meanAccManScream <- mean(allManScream$Precision)

allLevelomplete <- dataOutliers %>% filter_all(any_vars(. %in% c('Level complete')))
meanSpeedlevelComplete <- mean(allLevelomplete$ReactionTime)
meanAccLevelComplete <- mean(allLevelomplete$Precision)

allGirlScream <- dataOutliers %>% filter_all(any_vars(. %in% c('Girl Scream')))
meanSpeedGirlScream <- mean(allGirlScream$ReactionTime)
meanAccGirlScream <- mean(allGirlScream$Precision)

allSkrivemaskine <- dataOutliers %>% filter_all(any_vars(. %in% c('Skrivemaskine')))
meanSpeedSkrivemaskine <- mean(allSkrivemaskine$ReactionTime)
meanAccSkrivemaskine <- mean(allSkrivemaskine$Precision)

allWeirdoScream <- dataOutliers %>% filter_all(any_vars(. %in% c('Weirdo scream')))
meanSpeedWeirdoScream <- mean(allWeirdoScream$ReactionTime)
meanAccWeirdoScream <- mean(allWeirdoScream$Precision)

allapplaus <- dataOutliers %>% filter_all(any_vars(. %in% c('applaus')))
meanSpeedApplaus <- mean(allapplaus$ReactionTime)
meanAccApplaus <- mean(allapplaus$Precision)

allGlassBreaking <- dataOutliers %>% filter_all(any_vars(. %in% c('Glass Breaking')))
meanSpeedGlassBreaking <- mean(allGlassBreaking$ReactionTime)
meanAccGlassBreaking <- mean(allGlassBreaking$Precision)

allHiphopBeat <- dataOutliers %>% filter_all(any_vars(. %in% c('HipHop beat')))
meanSpeedHiphopBeat <- mean(allHiphopBeat$ReactionTime)
meanAccHiphopBeat <- mean(allHiphopBeat$Precision)

allKuglepen <- dataOutliers %>% filter_all(any_vars(. %in% c('Kuglepen')))
meanSpeedKuglepen <- mean(allKuglepen$ReactionTime)
meanaccKuglepen <- mean(allKuglepen$Precision)

allAnnouncement <- dataOutliers %>% filter_all(any_vars(. %in% c('Announcement')))
meanSpeedAnnouncement <- mean(allAnnouncement$ReactionTime)
meanAccAnnouncement <- mean(allAnnouncement$Precision)

allUprise <- dataOutliers %>% filter_all(any_vars(. %in% c('Uprise')))
meanSpeedUprise <- mean(allUprise$ReactionTime)
meanAccUprise <- mean(allUprise$Precision)


##_______________________Creating a barplot of indvidual sounds reaction time from highest to lowest_______##

IndividualMeans <- c(meanSpeedMonsterGrowl, meanSpeedManScream, meanSpeedGirlScream, meanSpeedWeirdoScream, meanSpeedGlassBreaking,
                     meanSpeedKuglepen, meanSpeedStikkontakt, meanSpeedSkrivemaskine, meanSpeedChatter, meanSpeedHiphopBeat,
                     meanSpeedAnnouncement, meanSpeedHarpFlourish, meanSpeedlevelComplete, meanSpeedUprise, meanSpeedApplaus)
orderedIndividualMeans <- sort(IndividualMeans, decreasing = FALSE)

par(mar = c(6, 4, 4, 2) + 0.1) ##Change size of graph##
barplot(orderedIndividualMeans, ##Creates bar plot
        main = "means of all individual sounds reaction speed",
        ylab = "Means",
        las = 2,
        names.arg = c("Man Scream", "Skrivemaskine", "Harp Flourish", "Uprise", "Monster Growl",
                      "Announcement", "Level Complete", "Hiphop Beat", "Chatter", "Stikkontakt",
                      "Weirdo Scream", "Girl Scream", "Kuglepen", "applaus", "Glass Breaking"),
        cex.names = 0.8,##Change font size##
        
)

##________________________Creating a barplot of individual sounds accuracy_________________##

IndividualAccuracy <- c(meanAccMonsterGrowl, meanAccManScream, meanAccGirlScream, meanAccWeirdoScream, meanAccGlassBreaking,
                        meanaccKuglepen, meanAccStikkontakt, meanAccSkrivemaskine, meanAccChatter, meanAccHiphopBeat,
                        meanAccAnnouncement, meanAccHarpFlourish, meanAccLevelComplete, meanAccUprise, meanAccApplaus)

orderedIndividualAccuracy <- sort(IndividualAccuracy, decreasing = FALSE)


barplot(orderedIndividualAccuracy, ##Creates bar plot
        main = "means of all individual sounds Accuracy",
        ylab = "Means",
        las = 2,
        names.arg = c("Hiphop Beat", "man Scream", "Glass Breaking", "Girl Scream", "Uprise",
                      "Monster Growl", "Kuglepen", "Applaus", "Weirdo Scream", "Level Complete",
                      "Annoouncement", "Harp Flourish", "Chatter", "Hiphop Beat", "Stikkontakt"),
        cex.names = 0.8,##Change font size##
        
)

##_________________________Hypothesis 1____________________________________________##

allNegatives = dataOutliers %>% filter_all(any_vars(. %in% c('Negative')))
meansNegative = mean(allNegatives$ReactionTime)

allNeutrals = dataOutliers %>% filter_all(any_vars(. %in% c('Neutral')))
meansNeutral = mean(allNeutrals$ReactionTime)

allPositives = dataOutliers %>% filter_all(any_vars(. %in% c('Positive')))
meansPositive = mean(allPositives$ReactionTime)

allMeans <- c(meansNegative, meansNeutral, meansPositive)

##________________________________Skewness + kurtosis beregninger + median___________##

kurtosisReaction <- kurtosis(dataOutliers$ReactionTime)
skewnessReaction <- skewness(dataOutliers$ReactionTime)

kurtosisReactionNegative <- kurtosis(allNegatives$ReactionTime)
skewnessNegative <- skewness(allNegatives$ReactionTime)

kurtosisReactionNeutral <- kurtosis(allNeutrals$ReactionTime)
skewnessNeutral <- skewness(allNeutrals$ReactionTime)

kurtosisReactionPositive <- kurtosis(allPositives$ReactionTime)
skewnessPositive <- skewness(allPositives$ReactionTime)

kurtosisPrecisionBlind <- kurtosis(allBlindfold$Precision)
skewnessPrecisionBlind <- skewness(allBlindfold$Precision)

kurtosisPrecisionNotBlind <- kurtosis(allNotBlindfold$Precision)
skewnessPrecisionNotBlind <- skewness(allNotBlindfold$Precision)

kurtosisTotal<- kurtosis(dataOutliers$Precision)
skewnesstotalBlindfold <- skewness(dataOutliers$Precision)

sortAllReaction <- sort(dataOutliers$ReactionTime, decreasing = FALSE)
median(sortAllReaction)

sortNegativeReaction <- sort(allNegatives$ReactionTime, decreasing = FALSE)
median(sortNegativeReaction)

sortNeutralReaction <- sort(allNeutrals$ReactionTime, decreasing = FALSE)
median(sortNeutralReaction)

sortPositiveReaction <- sort(allPositives$ReactionTime, decreasing = FALSE)
median(sortPositiveReaction)

sortBlindfold <- sort(allBlindfold$Precision, decreasing = FALSE)
median(sortBlindfold)

sortNotBlindfold <- sort(allNotBlindfold$Precision, decreasing = FALSE)
median(sortNotBlindfold)

sortAllBlindfold <- sort(dataOutliers$Precision, decreasing = FALSE)
median(sortAllBlindfold)


##________________________________deviance calculations______________________##

deviancemean <- mean(dataOutliers$ReactionTime)

reactionTimeDeviance <- dataOutliers$ReactionTime - deviancemean
sumSeactionTimeDeviance <- sum(reactionTimeDeviance)
ssReactionTimeDeviance <- sum((dataOutliers$ReactionTime - deviancemean) * (dataOutliers$ReactionTime - deviancemean))
varianceReactionTime <- sqrt(ssReactionTimeDeviance / 348-1)


encapsulation <- filter(dataOutliers, dataOutliers$ReactionTime < deviancemean + (varianceReactionTime *2),
                        dataOutliers$ReactionTime > deviancemean - (varianceReactionTime * 2))

(322/348)*100
##________________________________Boxplots________________##

par(mar = c(5, 4, 4, 2) + 0.1)
boxplot(allNegatives$ReactionTime, allNeutrals$ReactionTime, allPositives$ReactionTime,
        main = "Boxplots displaying sound mood reaction times seperated by mood",
        xlab = "Seconds",
        names = c("Negative", "neutral", "Positive"),
        horizontal = TRUE,
        col = "red",
        notch = TRUE
        )



##________________________________Shapiro Wilk test_____________________##
shapiro.test(allNegatives$ReactionTime)
shapiro.test(allNeutrals$ReactionTime)
shapiro.test(allPositives$ReactionTime)


##_____________Friedman test___________________________________________##

Comined <- matrix(c(allNegatives$ReactionTime, allNeutrals$ReactionTime, allPositives$ReactionTime), ncol = 3)

friedman.test(Comined)



##________________________________Histogram plot_______________________##


mygraphA <- ggplot(dataOutliers, aes(x = dataOutliers$ReactionTime))
(mygraphA + geom_histogram(aes(y = ..density..),binwidth = 0.5) + geom_density() + 
    geom_vline(xintercept = deviancemean, col="blue") + 
    geom_vline(xintercept = deviancemean - varianceReactionTime, col="green") +
    geom_vline(xintercept = deviancemean + varianceReactionTime, col="green") + 
    geom_vline(xintercept = deviancemean - (varianceReactionTime * 2), col="red") + 
    geom_vline(xintercept = deviancemean + (varianceReactionTime * 2), col="red"))


mygraphTest <- ggplot(dataOutliers, aes(x = dataOutliers$Precision))


##__________________________Bar plot_________________________________##

barplot(allMeans, ##Creates bar plot
main = "Means of Negative Neutral and Positive sound reactionstimes",
xlab = "Averages",
ylab = "Means",
names.arg = c("Negative", "Neutral", "Positive"),
col = "red",
)


##_________________________________Hypothesis 2_____________________________##

##_____________________________Separate blindfold and not blindfold tests____##

allBlindfold = dataOutliers %>% filter_all(any_vars(. %in% c('TRUE')))
allNotBlindfold = dataOutliers %>% filter_all(any_vars(. %in% c('FALSE')))


##_________________________________Means of blindfold and not blindfold__________##
meanBlindfold <- mean(allBlindfold$Precision)
meanNotBLindfold <- mean(allNotBlindfold$Precision)

##_______________________________Shapiro tests________________________##
shapiro.test(allBlindfold$Precision)
shapiro.test(allNotBlindfold$Precision)


##__________________________________Deviance calculations of precision_________##

devianceMeanPrecision <- mean(dataOutliers$Precision)

precisionDeviance <- dataOutliers$Precision - devianceMeanPrecision
sumPresisionDeviance <- sum(precisionDeviance)
ssPrecisionDeviance <- sum((dataOutliers$Precision - devianceMeanPrecision) * (dataOutliers$Precision - devianceMeanPrecision))
variancePrecision <- sqrt(ssPrecisionDeviance/ 348-1)

encapsulationDeviance <- filter(dataOutliers, dataOutliers$Precision < devianceMeanPrecision + (variancePrecision *2),
                        dataOutliers$Precision > devianceMeanPrecision - (variancePrecision * 2))

(329/348)*100


##___________________________________Boxplot of all precision__________________##



mygraphB <- ggplot(dataOutliers, aes(x = dataOutliers$Precision))
(mygraphB + geom_histogram(aes(y = ..density..),binwidth = 1) + geom_density() + 
    geom_vline(xintercept = devianceMeanPrecision, col="blue") + 
    geom_vline(xintercept = devianceMeanPrecision - variancePrecision, col="green") +
    geom_vline(xintercept = devianceMeanPrecision + variancePrecision, col="green") + 
    geom_vline(xintercept = devianceMeanPrecision - (variancePrecision * 2), col="red") + 
    geom_vline(xintercept = devianceMeanPrecision + (variancePrecision * 2), col="red"))

##__________________________________BOX PLOTS___________________________________##

boxplot(allBlindfold$Precision, allNotBlindfold$Precision,
        main = "Boxplots displaying results of accuracy with and without blidfold",
        xlab = "Accuracy in degrees",
        names = c("With Blindfold", "Without Blindffold"),
        horizontal = TRUE,
        col = "red",
        notch = TRUE
)



##__________________________________Wilcoxon test______________________________##

wilcox.test(allBlindfold$Precision, allNotBlindfold$Precision, paired=TRUE)
