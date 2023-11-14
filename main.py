from projeto_simplex import Simplex

# Criando o quadro
num_var = int(input("Numero de variaveis de decisao: "))
num_rest = int(input("Numero de restricoes: "))

smp = Simplex(num_var, num_rest)