# -*- coding: utf-8 -*-

# @author Rikzim

# Bibliotecas utilizadas

import time as t
import os 
import sys as s 
import random as r

# funções

def jogo_advinha():
    #----
    os.system('cls')
    for i in range (3):
      print("="*25)
      print("     JOGO DA ADVINHA")
      print("="*25)
      print("\t■□□□")
      t.sleep(0.5)
      os.system('cls')

      
      print("="*25)
      print("     JOGO DA ADVINHA")
      print("="*25)
      print("\t□■□□")
      t.sleep(0.5)
      os.system('cls')

      
      print("="*25)
      print("     JOGO DA ADVINHA")
      print("="*25)
      print("\t□□■□")
      t.sleep(0.5)
      os.system('cls')

      print("="*25)
      print("     JOGO DA ADVINHA")
      print("="*25)
      print("\t□□□■")
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
      while tentativa < 6 :
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
    input("Pressione (ENTER) para voltar ao menu:")
    os.system('cls')
#-------------
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
#-------------
def win():
  os.system("cls")
  print("="*30)
  print("\t RESPOSTA CORRETA!")
  print("="*30)
  print("         +1 PONTO")
  print("="*30)
  t.sleep(1)
  os.system('cls')
#-------------
def lose():
  os.system("cls")
  print("="*30)
  print("\t RESPOSTA ERRADA!")
  print("="*30)
  print(f"         0 PONTOS")
  print("="*30)
  t.sleep(1.5)
  os.system('cls')
#------------


# codigo todo
op_menu = "S"

while op_menu in ("s","S","Sim","sim"):
  os.system('cls')
  os.system('color 0F')
  #----
  print("━"*26)
  print("┃      MENU INICIAL      ┃")
  print("━"*26)
  print ('┃ 1 ┃''\033[31m'+'  JOGO DA ADVINHA   '+'\033[0;0m''┃')
  print("━"*26)
  print ('┃ 2 ┃''\033[34m'+'  QUIZ PROGRAMAÇÃO  '+'\033[0;0m''┃')
  print("━"*26)
  print ('┃ 3 ┃''\033[35m'+'  ADVINHE A TABUADA '+'\033[0;0m''┃')
  print("━"*26)
  #----
  op = input("Insira o Jogo que deseja jogar: ")
  
  #----

  if op == "1":
    os.system('color 0C')
    jogo_advinha()
  if op == "2":
    #----
    os.system('color 09')
    os.system('cls')
    for i in range (3):
      print("="*25)
      print("     QUIZ PROGRAMAÇÃO")
      print("="*25)
      print("\t■□□□")
      t.sleep(0.5)
      os.system('cls')

      
      print("="*25)
      print("     QUIZ PROGRAMAÇÃO")
      print("="*25)
      print("\t□■□□")
      t.sleep(0.5)
      os.system('cls')

      
      print("="*25)
      print("     QUIZ PROGRAMAÇÃO")
      print("="*25)
      print("\t□□■□")
      t.sleep(0.5)
      os.system('cls')

      print("="*25)
      print("     QUIZ PROGRAMAÇÃO")
      print("="*25)
      print("\t□□□■")
      t.sleep(0.5)
      os.system('cls')
    #----

    print("Bem vindo ao quiz!")
    print("Neste Quiz terás que responder perguntas sobre programação em contexto geral.")
    t.sleep(1.5)
    print("Boa Sorte !")

    inpu = str(input("Pressione (ENTER) para começar:"))

    os.system('cls')
    op_game_2 = "s"
    pontos = 0 
    rodada = 0
    while op_game_2 in("s","S","sim","SIM","Sim"):
      while rodada <6:
        #----- pergunta 1
        os.system('cls')
        print("Qual é a linguagem de programação mais utilizada? ")
        questao_1 = input("1 - JAVASCRIPT \n2 - JAVA \n3 - PYTHON \n:")
        if questao_1 == "1":
          pontos += 1
          rodada += 1
          win()
        else:
          rodada += 1
          lose()
        #-----

        #----- pergunta 2
        os.system('cls')
        print("Oque é essecial para desenvolvimento Web?")
        questao_2 = input("1 - PYTHON \n2 -  C# \n3 - HTML \n:")
        if questao_2 == "3":
          os.system('cls')
          pontos += 1
          rodada += 1
          win()
        else:
          rodada += 1
          lose()
        #----- 

        #----- pergunta 3
        print("Qual é a linguagem mais antiga?")
        questao_3 = input("1 - ASSEMBLY \n2 - LINGUAGEM C \n3 - LINGUAGEM C++ \n:")
        if questao_3 == "1":
          pontos += 1
          win()

        else:
          rodada += 1
          lose()
        #-----

        #----- pergunta 4 
        print("Qual é a linguagem mais utilizada em desevolvimento de jogos?")
        questao_4 = input("1 - C# \n2 - PYTHON \n3 - C++ \n:")
        if questao_4 == "3":
          pontos += 1
          rodada += 1
          win()

        else:
          rodada += 1
          lose()
        #-----

        #-----
        print("="*25)
        print("   PERGUNTA FINAL!")
        print("="*25)
        t.sleep(1.2)
        os.system('cls')
        #-----

        #----- pergunta 5
        print("Qual é a linguagem mais facíl de se aprender?")
        questao_5 = input("1 - C# \n2 - JAVASCRIPT \n3 - PYTHON \n:")
        if questao_5 == "3":
          pontos += 1
          win()
          break

        else:
          lose()
          break
      #-----

    #------  
      os.system("cls")
      print("="*30)
      print("\t FIM DO QUIZ!")
      print("="*30)
      print(f"    GANHASTE {pontos} NESTE QUIZ!")
      print("="*30)
      t.sleep(2)
      print("JOGUE COM OS TEUS AMIGOS E VEJA VOSSA PONTUAÇÃO!")
      t.sleep(2)
    #------

    #-----
      os.system('cls')
      print("Deseja Reiniciar o jogo ?")  
      op_game_2 = input("Sim | Não: ") 
    #-----
    #------
    os.system('cls')
    input("Pressione (ENTER) para voltar ao menu:")
    os.system('cls')
    #------    
  if op == "3":
    #----
    os.system('color 0D')
    os.system('cls')
    for i in range (3):
      print("="*25)
      print("     ADVINHE A TABUADA")
      print("="*25)
      print("\t■□□□")
      t.sleep(0.5)
      os.system('cls')

      
      print("="*25)
      print("     ADVINHE A TABUADA")
      print("="*25)
      print("\t□■□□")
      t.sleep(0.5)
      os.system('cls')

      
      print("="*25)
      print("     ADVINHE A TABUADA")
      print("="*25)
      print("\t□□■□")
      t.sleep(0.5)
      os.system('cls')

      print("="*25)
      print("     ADVINHE A TABUADA")
      print("="*25)
      print("\t□□□■")
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

      resposta = input("Qual é a tabuada apresentada?: ")
      if resposta == tb_alea:
        os.system('cls')
        print("="*28)
        print("    PARABÉNS ACERTASTE!!")
        print("="*28)
        print(f"    A TABUADA ERA DO {tb_alea}")
        print("="*28)
      else:
        os.system('cls')
        print("="*30)
        print("\t GAME OVER =/")
        print("="*30)
        print(f"     A TABUADA ERA A {tb_alea}")
        print("="*30)

      print("Deseja Reiniciar o jogo ?")  
      op_jogo_3 = input("Sim | Não: ") 
    #----

    #----
    os.system('cls')
    input("Pressione (ENTER) para voltar ao menu:")
    os.system('cls')
    #----



else:
  op_menu = "S"
