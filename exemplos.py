import time as t
import os
import sys as s
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





senha = int(input("Defina uma senha: "))
loading()
tentativa = 0
senha_c = 0
while senha_c != senha and tentativa <3:
    senha_c = int(input("Insira uma senha: "))
    if senha_c == senha:
        break
    else:
        print("Acesso negado tente novamente")
        tentativa+=1
if senha_c == senha:
    print("Bem vindo a conta!")
elif tentativa == 3:        
    print("Suas chances acabaram tente novamente mais tarde!")
    s.exit
