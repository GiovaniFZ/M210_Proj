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
        self.mostrar_quadro(num_var, num_rest)
        pos_pivo = self.encontra_pivo(num_rest, num_var)
        self.elimina(pos_pivo, num_var, num_rest)
        
       # while self.verifica_iteracao(num_var):
        #    
         #   self.dividir_linha_pivo(pos_pivo, num_var, num_rest)
         #   self.elimina(pos_pivo, num_var, num_rest)
         #   self.mostrar_quadro(num_var, num_rest)

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
    
    def dividir_linha_pivo(self, pos_pivo, num_var, num_rest):
        valor = pos_pivo
        pivo = q_simp[pos_pivo]
        aux = num_rest*num_var
        while valor % aux != 0:
            valor = valor - 1
        for i in range(6):
            q_simp[valor] = q_simp[valor]/pivo
            valor += 1
    
    def elimina(self, pos_pivo, num_var, num_rest):
        aux = num_var*num_rest # Auxiliar para iterar
        # linha começo e linha fim do pivo
        linha_com = pos_pivo
        linha_fim = pos_pivo
        while linha_com % aux!= 0:
            linha_com = linha_com - 1
        while linha_fim % aux != 0:
            linha_fim = linha_fim + 1
        linha_fim = linha_fim - 1
        # coluna começo e coluna fim do pivo
        coluna_com = pos_pivo
        coluna_fim = pos_pivo
        while coluna_com > aux:
            coluna_com = coluna_com - 6
        for i in range(num_var*num_var):
            if coluna_fim + 6 < len(q_simp):
                coluna_fim = coluna_fim + 6
        print(coluna_com) # OK
        print(coluna_fim) # OK
        print(linha_com)
        print(linha_fim)
        coluna_com_aux = coluna_com
        linha_com_aux = linha_com
        linha_fim_aux = linha_fim
        
        # Identificando a coluna e a linha de referencia
        coluna_ref = []
        linha_ref = []
        while coluna_com_aux < 24:
            coluna_ref.append(q_simp[coluna_com_aux])
            coluna_com_aux += 6
        print(coluna_ref)
        while linha_com_aux <= linha_fim:
            linha_ref.append(q_simp[linha_com_aux])
            linha_com_aux = linha_com_aux + 1
        print(linha_ref)
        
    def trocar_colunas(self, coluna1, coluna2, num_var, num_rest, linha_pivo, coluna_pivo):
        coluna1 = []
        coluna2 = []
        coluna3 = []
        
    def mostrar_quadro(self, num_var, num_rest):
        print("QUADRO:")
        for i in range(24):
            print(round(q_simp[i],2), end=" ")
            if i == 5 or i == 11 or i == 23 or i == 17:
               print('\n')
        print('\n')