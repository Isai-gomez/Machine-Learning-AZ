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

  