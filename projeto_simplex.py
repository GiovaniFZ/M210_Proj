class Simplex():
  def __init__(self, num_var, num_rest):
      # Criando um array global que represente cada um dos quadros simplex.
      global q_simp
      q_simp = []
      # Criando o quadro
      self.num_var = num_var
      self.num_rest = num_rest
      self.cria_quadro(num_rest, num_var)
      # Tamanho de cada linha
      tam = num_rest*num_var
      # Mostrando o quadro
      self.mostrar_quadro(num_var, num_rest)

      while not self.verifica_iteracao(tam):
          pos_pivo = self.encontra_pivo(num_rest, num_var)
          self.encontra_lref(pos_pivo, num_var, num_rest)
          self.mostrar_quadro(num_var, num_rest)
      self.mostrar_resultados(num_var, num_rest)


  def cria_quadro(self, num_rest, num_var):
      # O tamanho do quadro será (num_rest+1) X (num_var*num_rest)
      rep = (num_rest + 1)*(num_var*num_rest)+1 # 24
      # 4*6 = 24
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

  def verifica_iteracao(self, tam):
      parar = True
      for i in range(tam):
          if q_simp[i] < 0:
              parar = False
      return parar

  def encontra_pivo(self, num_rest, num_var):
      # Encontrando a coluna pivo
      aux = 0 # Obtem o indice do menor elemento da linha 0
      aux4 = float('inf') # Maior valor
      pos_pivo = 0
      tam = num_rest*num_var
      for i in range(tam):
          if q_simp[i] < q_simp[aux]:
              aux = i
      # Dividindo cada elemento para obter o menor deles
      aux2 = aux + tam
      aux5 = 11
      # AUX5 = CONTROLA AS COLUNAS DO LADO DIREITO
      # AUX2 = CONTROLA A COLUNA DO PIVO
      for i in range(num_rest):
          if q_simp[aux2] > 0: # Divisao por zero nao deve existir, e o elemento pivo deve ser maior que 0
              aux3 = q_simp[aux5]/q_simp[aux2] # 83.3
              if aux3 < aux4 and aux3 != 0: 
                  aux4 = aux3
                  pos_pivo = aux2
          aux2 += tam # Vai pra proxima linha
          aux5 += tam
      return pos_pivo

  def dividir_linha_pivo(self, pos_pivo, num_var, num_rest):
      # Dividindo a linha do pivo pelo elemento pivo
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
      tam = num_rest*num_var
      tam_q = 4*tam
      # linha começo e linha fim do pivo
      linha_com = pos_pivo
      linha_fim = pos_pivo
      if pos_pivo % aux != 0:
          while linha_com % aux != 0:
              linha_com = linha_com - 1
          while linha_fim % aux != 0:
              linha_fim = linha_fim + 1
      elif linha_com < tam_q:
              linha_fim += tam

      linha_fim = linha_fim - 1
      # coluna começo e coluna fim do pivo
      coluna_com = pos_pivo
      coluna_fim = pos_pivo
      while coluna_com >= aux:
          coluna_com = coluna_com - 6
      for i in range(aux):
          if coluna_fim + aux < len(q_simp):
              coluna_fim = coluna_fim + aux
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
      aux = 0
      tam = num_rest*num_var
      tam_q = 4*tam
      parar = False

      while aux < tam_q:
          if aux in linha_ref_ids:
              aux += tam
              linha_id += 1
          for i in range(tam):
              if aux <= tam_q:
                  linha1.append(q_simp[aux])
                  aux += 1
              else:
                  parar = True
                  break
          if (parar == False):
              self.calcular_nova_linha(linha1, linha_id, linha_ref, col_ref, col_ref_ids, pos_pivo, tam)
              linha1.clear() # Apaga a linha
              linha_id += 1 # Incrementa id da linha (devem ter 4 linhas)
              # Resultado esperado:
              #[-5.0, 0.0, 0.0, 4.666666666666667, 0.0, 466.6666666666667]
              #[3.0, 0.0, 1.0, 0.0, 0.0, 250.0]
              #[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
              #[0.25, 0.0, 0.0, -0.3333333333333333, 1.0, 16.66666666666667]
      # No exemplo, linha1 = [-5.0, -7.0, 0.0, 0.0, 0.0, 0.0]
      # Linha 1 nova = [-5.0, 0.0, 0.0, 4.666666666666667, 0.0, 466.6666666666667]

      # Divide a linha do pivo
      self.dividir_linha_pivo(pos_pivo, num_var, num_rest)

  def calcular_nova_linha(self, linha, linha_id, linha_ref, col_ref, col_ref_ids, pos_pivo, tam):
      # Variavel auxiliar para multiplicar o elemento na mesma linha por -1.
      aux = col_ref[linha_id] #-7
      aux = aux/q_simp[pos_pivo] # aux = Elemento da coluna_ref/pivo
      aux2 = linha_id*tam
      # Percorrendo a linha 1
      for i in range(tam):
          linha[i] = linha[i] - aux*linha_ref[i]
          q_simp[aux2] = linha[i] # Adicionando no quadro simplex
          aux2 += 1

  def mostrar_quadro(self, num_var, num_rest):
      print("QUADRO:")
      aux = 1
      for i in range(4*num_var*num_rest):
          print(round(q_simp[i],2), end=" | ")
          if aux % 6 == 0 and i != 0:
              print('\n')
          aux +=1
      print('\n')

  def mostrar_resultados(self, num_var, num_rest):
      print("RESULTADOS:")

      # Mostrar lucro máximo (negativo do valor na última linha, primeira coluna)
      lucro_maximo = q_simp[(num_var * num_rest) - 1]
      print(f"Lucro Máximo: {lucro_maximo}")

      # Mostrar preços sombra (última linha, exceto o último elemento)
      precos_sombra = q_simp[((num_var * num_rest)-4):(num_var * num_rest)-1]
      print("Preços Sombra:", precos_sombra)











