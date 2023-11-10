class Simplex():
    def __init__(self):
        num_var = int(input("Numero de variaveis de decisao: ")) #2
        num_rest = int(input("Numero de restricoes: "))#3
        # O tamanho do quadro será (num_rest+1) X (num_var*num_rest)
        rep = (num_rest + 1)*(num_var*num_rest)+1
        # Criando um array que represente cada um dos quadros simplex.
        q_simp = []
        for i in range(rep):
            q_simp.append(0.0)
        
        # Entrando com a função objetivo
        for i in range(num_var):
            var1 = float(input("Função objetivo - Valor " + str(i+1) +": "))
            # No quadro, as variáveis da função objetivo serão negativas
            q_simp[i] = var1*(-1)
        
        # Entrando com as restricoes
        # As linhas serão descritas pelo indice num_var*num_rest
        aux = num_var*num_rest # 6
        for i in range(num_rest):
            for j in range(num_var):
                rest = float(input("Restricao " + str(i+1) + " - variavel " + str(j+1) + ": "))
                q_simp[aux] = rest
                aux += 1 # vai pra proxima coluna
                print(aux)
            aux += 3
            print(aux)
            l_dir = float(input("Lado direito: "))
            q_simp[aux] = l_dir
            aux +=1 # vai pra proxima linha
            
        # Construindo a matriz identidade
        aux = 8
        for i in range(3):
            q_simp[aux] = 1.0
            aux += 7
        
        # Printando o quadro simplex
        for i in range(24):
            print(q_simp[i], end=" ")
            if i == 5 or i == 11 or i == 23 or i == 17:
                print('\n')
        
        # Dividindo os elementos e pegando o menor