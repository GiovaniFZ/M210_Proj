class Simplex():
    def __init__(self):
        # Criando um array global que represente cada um dos quadros simplex.
        global q_simp
        q_simp = []
        # Criando o quadro
        num_var = int(input("Numero de variaveis de decisao: "))
        num_rest = int(input("Numero de restricoes: "))
        self.cria_quadro(num_rest, num_var)
        # Mostrando o quadro
        self.mostrar_quadro()
        
        while self.verifica_iteracao(num_var):
            pos_pivo = self.encontra_pivo(num_rest, num_var)
            self.dividir_linhas(pos_pivo, num_var, num_rest)
            self.elimina(pos_pivo, num_var, num_rest)
            self.mostrar_quadro()

    def cria_quadro(self, num_rest, num_var):
        # O tamanho do quadro será (num_rest+1) X (num_var*num_rest)
        rep = (num_rest + 1)*(num_var*num_rest)+1
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
            aux += 3
            l_dir = float(input("Lado direito: "))
            q_simp[aux] = l_dir
            aux +=1 # vai pra proxima linha
            
        # Construindo a matriz identidade
        aux = 8
        for i in range(num_rest):
            q_simp[aux] = 1.0
            aux += 7
            
    def verifica_iteracao(self, num_var):
        for i in range(num_var):
            if q_simp[i] < 0:
                return True
            else:
                return False
                
    def encontra_pivo(self, num_rest, num_var):
        # Encontrando a coluna pivo
        # Obtendo o indice da coluna menor
        aux = 0
        aux4 = 10000
        pos_pivo = 0
        for i in range(num_var):
            if q_simp[i] < aux:
                aux = i
        # Dividindo cada elemento
        aux2 = aux + (num_rest*num_var) 
        for i in range(num_rest):
            if q_simp[aux2] != 0: # Divisao por zero nao deve existir
                aux3 = q_simp[aux2+4]/q_simp[aux2]
                if aux3 < aux4:
                    aux4 = aux3
                    pos_pivo = aux2
            aux2 += 6
        return pos_pivo
    
    def dividir_linhas(self, pos_pivo, num_var, num_rest):
        valor = pos_pivo
        pivo = q_simp[pos_pivo]
        aux = num_rest*num_var
        while valor % aux != 0:
            valor = valor - 1
        for i in range(6):
            q_simp[valor] = q_simp[valor]/pivo
            valor += 1
    
    def elimina(self, pos_pivo, num_var, num_rest):
        pivo = q_simp[pos_pivo]
        aux = num_rest * num_var

        for i in range(aux):
            if i != pos_pivo:
                razao = q_simp[i] / q_simp[pos_pivo]
                for j in range(6):
                    q_simp[i + j] -= razao * q_simp[pos_pivo + j]

    def trocar_colunas(self, coluna1, coluna2, num_var, num_rest):
        for i in range(num_rest + 1):
            q_simp[coluna1], q_simp[coluna2] = q_simp[coluna2], q_simp[coluna1]
            coluna1 += num_var * num_rest
            coluna2 += num_var * num_rest
        
    def mostrar_quadro(self):
        print("QUADRO:")
        for i in range(24):
            print(round(q_simp[i],2), end=" ")
            if i == 5 or i == 11 or i == 23 or i == 17:
               print('\n')
        print('\n')