import os
from function import end_app
from function import add_restaurant

print("""
      
██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░███╗░░██╗░█████╗░░██╗░░░░░░░██╗
██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗████╗░██║██╔══██╗░██║░░██╗░░██║
██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝██╔██╗██║██║░░██║░╚██╗████╗██╔╝
██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗██║╚████║██║░░██║░░████╔═████║░
██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║██║░╚███║╚█████╔╝░░╚██╔╝░╚██╔╝░
╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░
      
      """)

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

option = int(input('Escolha uma das opções: '))

print(f'\nOpcao Escolhida: {option}\n')

if option == 1:
    add_restaurant()
elif option == 2:
    os.system('cls')
    print('Operacao Escolhida: Listagem')
elif option == 3:
    os.system('cls')
else:
    end_app()
    