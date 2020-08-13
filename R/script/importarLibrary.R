# Plantilla de pre procesado datos 
# Importar el dataset 
dataset <- read.csv("Data.csv")
# Tratamiento de Nas
dataset$Age <- ifelse(is.na(dataset$Age),
                      ave(dataset$Age, FUN = function(x) median(x, na.rm = TRUE))
                      ,dataset$Age)
dataset$Salary <- ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = function(x) median(x,na.rm = TRUE)),
                         dataset$Salary)
#Codificar las variables categóricas
dataset$Country = factor(dataset$Country, levels = c("France", "Spain", "Germany"), labels = c(1,2,3))
dataset$Purchased = factor(dataset$Purchased, levels = c("No", "Yes"),labels = c(0,1)) 
# Dividir el dataset en train y test
library(caTools) #instalar librería en R
