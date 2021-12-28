# Bibliotecas utilizadas
import time as t
import os 
import sys as s 
import random as r

# funções

def jogo_advinha():
    #----
    for i in range (3):
      os.system('cls')
      print("="*30)
      print("\tJOGO DO ADVINHA")
      print("="*30)
      print("Carregando.")
      t.sleep(0.5)
      os.system('cls')

      
      print("="*30)
      print("\tJOGO DO ADVINHA")
      print("="*30)
      print("Carregando..")
      t.sleep(0.5)
      os.system('cls')

      
      print("="*30)
      print("\tJOGO DO ADVINHA")
      print("="*30)
      print("Carregando...")
      t.sleep(0.5)
      os.system('cls')
    #----  

    #------
    os.system('cls')
    print("Vamos começar..")
    t.sleep(1.5)
    print("Tens que acertar um número entre 1 a 20, BOA SORTEE!.")
    t.sleep(4)
    os.system('cls')
    num_alea = r.randint(1,20)
    #-----

    #-----
    op = "S"
    #-----
    
    #-----
    while  op in ("S","SIM","s","Sim","sim"):
      tentativa = 1
      num_alea = r.randint(0,20)
      while tentativa < 6:
        num = int(input("Insira o número no qual estou pensando: "))
        if num == num_alea:
          os.system('cls')
          print("="*30)
          print("\t PARABÉNS GANHASTE!!")
          print("="*30)
          print(f"Acertaste na {tentativa}ª tentativa!!")
          print("="*30)
          break
        if num > num_alea:
          print("O número no qual inseriu é maior!")
          tentativa +=1 
        elif num < num_alea:
          print("O número no qual inseriu é menor!")
          tentativa +=1
    #-----

      #-----
      if num != num_alea:
        os.system('cls')
        print("="*30)
        print("\t GAME OVER =/")
        print("="*30)
        print(f"O NÚMERO CORRETO ERA {num_alea}")
        print("="*30)
      print("Deseja Reiniciar o jogo ?")  
      op = input("Sim | Não: ")
      os.system('cls')
    #-----  

    #-----
    os.system('cls')
    print("Clique para voltar ao menu inicial")
    op_menu = input("(Enter): ")
    os.system('cls')

 
      
      
      


def loading():
  for i in range (3):
    print("Carregando.")
    t.sleep(0.5)
    os.system('cls')
    print("Carregando..")
    t.sleep(0.5)
    os.system('cls')
    print("Carregando...")
    t.sleep(0.5)
    os.system('cls')
    



# codigo todo
op_menu = "S"

while op_menu in ("s","S","Sim","sim"):
  os.system('cls')
  #----
  print("="*25)
  print("\t  MENU INICIAL")
  print("="*25)
  print("= 1 |  JOGO DO ADVINHA  =")
  print("="*25)
  print("= 2 |  QUIZ INFORMATICA =")
  print("="*25)
  print("= 3 | ADVINHE A TABUADA =")
  print("="*25)
  #----
  op = int(input("Insira o Jogo que deseja jogar: "))
  #----

  if op == 1:
    jogo_advinha()
  if op == 2:
    #----
    for i in range (3):
      os.system('cls')
      print("="*25)
      print("\tQUIZ INFORMATICA")
      print("="*25)
      print("Carregando.")
      t.sleep(0.5)
      os.system('cls')

      
      print("="*25)
      print("\tQUIZ INFORMATICA")
      print("="*25)
      print("Carregando..")
      t.sleep(0.5)
      os.system('cls')

      
      print("="*25)
      print("\tQUIZ INFORMATICA")
      print("="*25)
      print("Carregando...")
      t.sleep(0.5)
      os.system('cls')
    #----

    print("Bem vindo ao quiz!")
    op_game_2 = "s"
    pontos = 0 
    while op_game_2 in("s","S","sim","SIM","Sim"):
      #----- pergunta 1
      print("QUAL O NICKNAME DO FELIPE?")
      questao_1 = int(input("1 - FELIPEDAMIRA \n2 - FAPO \n3 - FYPE \n:"))
      if questao_1 == 1:
        os.system('cls')
        print("RESPOSTA CORRETA!")
        t.sleep(2)
        pontos +=1
        os.system('cls')

      else:
        os.system('cls')
        print("RESPOSTA ERRADA!") 
        t.sleep(2)
        os.system('cls')
      #-----

      #----- pergunta 2
      os.system('cls')
      print("BEAN É NOOB ?")
      questao_1 = int(input("1 - SIM \n2 - COM CERTEZA \n3 - CLARO \n:"))  
      if questao_1 == 2:
        os.system('cls')
        print("RESPOSTA CORRETA!")
        t.sleep(2)
        os.system('cls')
        pontos+=1
      else:
        os.system('cls')
        print("RESPOSTA ERRADA!")
        t.sleep(2)
        os.system('cls')
      #----- 

      #----- pergunta 3
      print("OQUE O DESTROYER É ")
      questao_1 = int(input("1 - GAY \n2 - CORNO \n3 - AGIOTA \n:"))
      if questao_1 == 2:
        os.system('cls')
        print("RESPOSTA CORRETA!")
        t.sleep(2)
        pontos +=1
        os.system('cls')

      else:
        os.system('cls')
        print("RESPOSTA ERRADA!") 
        t.sleep(2)
        os.system('cls')
      #-----

      #----- pergunta 4 
      print("QUAL O NICKNAME DO FELIPE?")
      questao_1 = int(input("1 - FELIPEDAMIRA \n2 - FAPO \n3 - FYPE \n:"))
      if questao_1 == 1:
        os.system('cls')
        print("RESPOSTA CORRETA!")
        t.sleep(2)
        pontos +=1
        os.system('cls')

      else:
        os.system('cls')
        print("RESPOSTA ERRADA!") 
        t.sleep(2)
        os.system('cls')
      #-----

      #----- pergunta 5
      print("QUAL O NICKNAME DO FELIPE?")
      questao_1 = int(input("1 - FELIPEDAMIRA \n2 - FAPO \n3 - FYPE \n:"))
      if questao_1 == 1:
        os.system('cls')
        print("RESPOSTA CORRETA!")
        t.sleep(2)
        pontos +=1
        os.system('cls')
        break

      else:
        os.system('cls')
        print("RESPOSTA ERRADA!") 
        t.sleep(2)
        os.system('cls')
        break
        #--------


      
    print(f"Voçê fez {pontos} pontos!!")
    input("pressiona enter")

  if op == 3:
    #----
    for i in range (3):
      os.system('cls')
      print("="*25)
      print("\tADVINHE A TABUADA")
      print("="*25)
      print("Carregando.")
      t.sleep(0.5)
      os.system('cls')

      
      print("="*25)
      print("\tADVINHE A TABUADA")
      print("="*25)
      print("Carregando..")
      t.sleep(0.5)
      os.system('cls')

      
      print("="*25)
      print("\tADVINHE A TABUADA")
      print("="*25)
      print("Carregando...")
      t.sleep(0.5)
      os.system('cls')
    #----

    #----
    op_jogo_3 = "s"
    #----

    #----
    while op_jogo_3 in ("s","S","Sim","sim","SIM"):
      os.system('cls')
      print("Olá, Bem vindo ao jogo do advinhe a tabuada!")
      t.sleep(1)
      print("Neste jogo tens que advinhar qual tabuada de 1 a 20 aparece no ecrã.")
      t.sleep(1.5)
      print("Vamos Começar?")
      t.sleep(0.9)
      inpu = str(input("Pressione (ENTER) para começar:"))
      os.system('cls')

      tb_alea = r.randint(1,20)

      for i in range(1,11):
        print(f"? * {i} =", tb_alea*i)
        t.sleep(0.8)

      resposta = int(input("Qual é a tabuada apresentada?: "))
      if resposta == tb_alea:
        os.system('cls')
        print("="*30)
        print("\t PARABÉNS ACERTASTE!!")
        print("="*30)
        print(f"A TABUADA ERA DO {tb_alea}")
        print("="*30)
      else:
        os.system('cls')
        print("="*30)
        print("\t GAME OVER =/")
        print("="*30)
        print(f"A TABUADA ERA A {tb_alea}")
        print("="*30)

      print("Deseja Reiniciar o jogo ?")  
      op_jogo_3 = input("Sim | Não: ") 
    #----

    #----
    os.system('cls')
    input("Pressione (ENTER) para voltar ao menu:")
    os.system('cls')
    #----