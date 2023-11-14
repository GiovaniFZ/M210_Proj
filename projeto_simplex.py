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
        self.encontra_lref(pos_pivo, num_var, num_rest)
        self.mostrar_quadro(num_var, num_rest)
        
       # while self.verifica_iteracao(num_var):
        #    
         #   self.dividir_linha_pivo(pos_pivo, num_var, num_rest)
         #   self.encontra_lref(pos_pivo, num_var, num_rest)
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
        for i in range(aux):
            q_simp[valor] = q_simp[valor]/pivo
            valor += 1
    
    def encontra_lref(self, pos_pivo, num_var, num_rest):
        aux = num_var*num_rest # Auxiliar para iterar
        # linha começo e linha fim do pivo
        linha_com = pos_pivo
        linha_fim = pos_pivo
        while linha_com % aux != 0:
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
        coluna_com_aux = coluna_com
        linha_com_aux = linha_com
        linha_fim_aux = linha_fim
        # Identificando a coluna e a linha de referencia
        coluna_ref = []
        coluna_ref_ids = []
        linha_ref = []
        linha_ref_ids = []
        while coluna_com_aux < 24:
            coluna_ref.append(q_simp[coluna_com_aux])
            coluna_ref_ids.append(coluna_com_aux)
            coluna_com_aux += 6
        # No exemplo, col_ref = [-7, 0, 1.5, 0.5]
        while linha_com_aux <= linha_fim:
            linha_ref.append(q_simp[linha_com_aux])
            linha_ref_ids.append(linha_com_aux)
            linha_com_aux = linha_com_aux + 1
        self.encontrar_linhas(linha_ref, linha_ref_ids, num_rest, num_var, coluna_ref, coluna_ref_ids, pos_pivo)
    
    def encontrar_linhas(self, linha_ref, linha_ref_ids, num_rest, num_var, col_ref, col_ref_ids, pos_pivo):
        # Encontrando as linhas
        linha1 = []
        linha_id = 0
        tam = num_rest*num_var
        
        for i in range(tam):
            linha1.append(q_simp[i])
        self.calcular_nova_linha(linha1, linha_id, linha_ref, col_ref, col_ref_ids, pos_pivo, tam)
        # No exemplo, linha1 = [-5.0, -7.0, 0.0, 0.0, 0.0, 0.0]
        # Linha 1 nova = [-5.0, 0.0, 0.0, 4.666666666666667, 0.0, 466.6666666666667]
        
        #for i in range(24):
        #    if i % 6 == 0 and i != 0 and i not in linha_ref_ids:
        #        self.calcular_nova_linha(linha1, linha_id, linha_ref, col_ref, col_ref_ids, pos_pivo, tam)
        #        linha_id += 1
        #    else:
        #        linha1.append(q_simp[i])
        
    def calcular_nova_linha(self, linha, linha_id, linha_ref, col_ref, col_ref_ids, pos_pivo, tam):
        # Variavel auxiliar para multiplicar o elemento na mesma linha por -1.
        aux = col_ref[linha_id]# 7
        print(aux)
        aux = aux/q_simp[pos_pivo]
        # Percorrendo a linha 1
        for i in range(tam):
            linha[i] = linha[i] - aux*linha_ref[i]
            q_simp[i] = linha[i] # Adicionando no quadro simplex
        linha.clear() # Apagando a linha
        
    def trocar_colunas(self, coluna1, coluna2, num_var, num_rest, linha_pivo, coluna_pivo):
        coluna1 = []
        coluna2 = []
        coluna3 = []
        
    def mostrar_quadro(self, num_var, num_rest):
        print("QUADRO:")
        aux = 1
        for i in range(4*num_var*num_rest):
            print(round(q_simp[i],2), end=" | ")
            if aux % 6 == 0 and i != 0:
                print('\n')
            aux +=1
        print('\n')