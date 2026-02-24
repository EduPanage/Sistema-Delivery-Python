import os       #Funcao para Execucao da Funcao os.system('cls')
import time     #Funcao para Execucao da Funcao time.sleep


def main():
    show_app()
    show_options()
    operation()


def show_app():
        print("""
        
    ██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░███╗░░██╗░█████╗░░██╗░░░░░░░██╗
    ██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗████╗░██║██╔══██╗░██║░░██╗░░██║
    ██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝██╔██╗██║██║░░██║░╚██╗████╗██╔╝
    ██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗██║╚████║██║░░██║░░████╔═████║░
    ██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║██║░╚███║╚█████╔╝░░╚██╔╝░╚██╔╝░
    ╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░
        
        """)
    
def show_options():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def operation():
    option = int(input('Escolha uma das opções: '))

    print(f'\nOpcao Escolhida: {option}\n')
    
    if option == 1:         #Funcoes do Function.py
        add_restaurant()
    elif option == 2:
        os.system('cls')
        print('Operacao Escolhida: Listagem')
    elif option == 3:
        os.system('cls')
    else:
        end_app()


def add_restaurant():
    os.system('cls')
    print('Operacao Escolhida: Cadastro\n\n')
    restaurant_name = input('Informe o nome do restaurante: ')
    restaurant_type = input('Informe o tipo do restaurante(Ex: Hamburgueria): ')
    print(f'\nNome: {restaurant_name} - {restaurant_type}')
    time.sleep(1.5)
    print('\n\nRestaurante Adicionado!')
    time.sleep(1.5)
    os.system('cls')

def end_app():
    os.system('cls')
    print('\n\nEncerrando...\n\n')
    time.sleep(1.5)

