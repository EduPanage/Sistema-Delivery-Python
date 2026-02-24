import os
import time

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
    os.system('cls')
    print('Operacao Escolhida: Cadastro\n\n')
    restaurant_name = input('Informe o nome do restaurante: ')
    restaurant_type = input('Informe o tipo do restaurante(Ex: Hamburgueria): ')
    os.system('cls')
elif option == 2:
    os.system('cls')
    print('Operacao Escolhida: Listagem')
elif option == 3:
    os.system('cls')
else:
    os.system('cls')
    print('Encerrando...')
    time.sleep(1.5)
    