# Un ejemplo multivariado: componentes principales
library(tidyverse)  # visualizacion y manipulacion de datos
library(gridExtra)  # manejo de graficos

# cargamos el conjunto de datos, el que viene incluido en R
data("USArrests")

# imprimimos en pantalla los primeros diez datos
head(USArrests, 10)

# calculamos la varianza de cada variable
apply(USArrests, 2, var)

# creamos una nueva tabla con las variables centradas
scaled_df <- apply(USArrests, 2, scale)
head(scaled_df)

# calculamos los valores y vectores propios
arrests.cov <- cov(scaled_df)
arrests.eigen <- eigen(arrests.cov)
# reumen informativo del arreglo
str(arrests.eigen)

# Extraemos los dos primeros vectores propios (dos primeras componentes)
(phi <- arrests.eigen$vectors[,1:2])

# Agregamos las etiquetas
phi <- -phi
row.names(phi) <- c("Murder", "Assault", "UrbanPop", "Rape")
colnames(phi) <- c("PC1", "PC2")
phi

# Calculamos los puntajes en cada dimension
PC1 <- as.matrix(scaled_df) %*% phi[,1]
PC2 <- as.matrix(scaled_df) %*% phi[,2]

# Creamos una tabla con los puntajes asociados a cada dimension
PC <- data.frame(State = row.names(USArrests), PC1, PC2)
head(PC)

# Graficamos las dos primeras componentes principales para cada estado
ggplot(PC, aes(PC1, PC2)) + 
  modelr::geom_ref_line(h = 0) +
  modelr::geom_ref_line(v = 0) +
  geom_text(aes(label = State), size = 3) +
  xlab("Primera Componente Principal") + 
  ylab("Segunda Componente Principal") + 
  ggtitle("Dos primeras componentes principales para los datos USArrests")


# Culculo de inercia
PVE <- arrests.eigen$values / sum(arrests.eigen$values)
round(PVE, 2)

# Graficando la inercia para diferentes grupos
PVEplot <- qplot(c(1:4), PVE) + 
  geom_line() + 
  xlab("Principal Component") + 
  ylab("PVE") +
  ggtitle("Scree Plot") +
  ylim(0, 1)

# Inercia acumulada
cumPVE <- qplot(c(1:4), cumsum(PVE)) + 
  geom_line() + 
  xlab("Principal Component") + 
  ylab(NULL) + 
  ggtitle("Cumulative Scree Plot") +
  ylim(0,1)

#Graficando la inercia acumulada
grid.arrange(PVEplot, cumPVE, ncol = 2)

# Aplicamos componentes princi
pca_result <- prcomp(USArrests, scale = TRUE)
names(pca_result)

# media para cada variable
pca_result$center

# desviaciones estandar
pca_result$scale

# direcciones
pca_result$rotation
pca_result$rotation <- -pca_result$rotation
pca_result$rotation

# Actualizando resultados
pca_result$x <- - pca_result$x
head(pca_result$x)

# Graficamos las dos primeras componentes con las variables
biplot(pca_result, scale = 0)

# varianzas, algunos calculos auxiliares
pca_result$sdev
(VE <- pca_result$sdev^2)
PVE <- VE / sum(VE)
round(PVE, 2)

# Funcion para crear el circulo de correlacion
circle <- function(center = c(0, 0), npoints = 100) {
  r = 1
  tt = seq(0, 2 * pi, length = npoints)
  xx = center[1] + r * cos(tt)
  yy = center[1] + r * sin(tt)
  return(data.frame(x = xx, y = yy))
}
corcir = circle(c(0, 0), npoints = 100)

# Creamos una tabla con las correlaciones entre variables y las componentes principales
correlations = as.data.frame(cor(USArrests, pca_result$x))

# Generamos una tabla con las "flechas"
arrows = data.frame(x1 = c(0, 0, 0, 0), y1 = c(0, 0, 0, 0), x2 = correlations$PC1, 
                    y2 = correlations$PC2)

# Dibujamos los resultados
ggplot() + geom_path(data = corcir, aes(x = x, y = y), colour = "gray65") + 
  geom_segment(data = arrows, aes(x = x1, y = y1, xend = x2, yend = y2), colour = "gray65") + 
  geom_text(data = correlations, aes(x = PC1, y = PC2, label = rownames(correlations))) + 
  geom_hline(yintercept = 0, colour = "gray65") + geom_vline(xintercept = 0, 
                                                             colour = "gray65") + 
  xlim(-1.1, 1.1) + ylim(-1.1, 1.1) + labs(x = "componente principal 1", y = "componente principal 2") + 
  ggtitle("Circulo de correlaciones")


