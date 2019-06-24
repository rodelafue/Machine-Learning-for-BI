##Cargamos las librerias
library(FactoMineR)
library(ggplot2)
library(calibrate)
library(lattice)

##Fijando el directorio de trabajo
setwd("~/Dropbox/Cursos UdeC/Cursos pregrado/Data Mining/clasificaci??n jer??rquica y k medias")

##Cargamos la tabla de datos
tabla <- read.csv("ejemplonotasestudiantes.csv", sep = ";", dec = ",")

##Analisis en componentes principales
res.pca<-PCA(tabla[,-1], scale.unit = TRUE, ncp = 4, ind.sup = NULL, 
             quanti.sup = NULL, quali.sup = NULL, row.w = NULL, 
             col.w = NULL, graph = TRUE, axes = c(1,2))

plot(res.pca$ind$coord[,c(1,2)], ylim = c(-2, 2))
text(res.pca$ind$coord[,c(1)], res.pca$ind$coord[,c(2)], labels=tabla[,1], cex= 0.7, pos = 3)

hc2 <- HCPC(res.pca, kk=Inf, nb.clust=3)

##Clustering jerarquico
distancias <- dist(tabla)
res.hclust.median <- hclust(distancias, method = "median")
res.hclust.comp <- hclust(distancias, method = "complete")
res.hclust.ward.D <- hclust(distancias, method = "ward.D")
res.hclust.ward.D2 <- hclust(distancias, method = "ward.D2")

par(mfrow=c(2,2))
plot(res.hclust.comp)
plot(res.hclust.median)
plot(res.hclust.ward.D)
plot(res.hclust.ward.D2)

##k-means
set.seed(20)
notasCluster <- kmeans(tabla[,-1], 3, nstart = 20)
notasCluster

##Visualizacion
