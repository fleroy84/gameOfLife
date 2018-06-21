setwd("~/Google Drive LAK/Mes Documents /Espace Python/Git/gameOfLife/performances")

gosper <- read.csv("test_gosper.csv")
hwss <- read.csv("test_hwss.csv")
mathus <- read.csv("test_mathusalem.csv")
replicateur <- read.csv("test_replicateur_highlife.csv")
tagalong <- read.csv("test_tagalong.csv")

#graphiques
plot(gosper$Génération, gosper$Temps, col = "blue", xlab = "Génération", ylab = "Temps (sec)", main = "Canon de Gosper")
abline(lm(gosper$Temps~gosper$Génération), lwd = 2, col = "red")

plot(hwss$Génération, hwss$Temps, col = "blue", xlab = "Génération", ylab = "Temps (sec)", main = "Heavy Weight Space Ship")
abline(lm(hwss$Temps~hwss$Génération), lwd = 2, col = "red")

plot(mathus$Génération, mathus$Temps, col = "blue", xlab = "Génération", ylab = "Temps (sec)", main = "Mathusalem")
abline(lm(mathus$Temps~mathus$Génération), lwd = 2, col = "red")

plot(replicateur$Génération, replicateur$Temps, col = "blue", xlab = "Génération", ylab = "Temps (sec)", main = "Replicateur (règle HighLife)")
abline(lm(replicateur$Temps~replicateur$Génération), lwd = 2, col = "red")

plot(tagalong$Génération, tagalong$Temps, col = "blue", xlab = "Génération", ylab = "Temps (sec)", main = "Tagalong")
abline(lm(tagalong$Temps~tagalong$Génération), lwd = 2, col = "red")

#modèles de regression
gosper_mdl <- lm(Temps~Génération, data = gosper)
summary(gosper_mdl)
cor.test(gosper$Temps, gosper$Génération)
