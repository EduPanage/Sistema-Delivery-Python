import os       #Funcao para Execucao da Funcao os.system('cls')
import time     #Funcao para Execucao da Funcao time.sleep

restaurants = []


def main():
    show_app()
    show_options()
    operation()

def small_main():
    show_options()
    operation()

def show_app():
        print("""
    
    ██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗   ███╗░░██╗░█████╗░░██╗░░░░░░░██╗
    ██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗  ████╗░██║██╔══██╗░██║░░██╗░░██║
    ██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝  ██╔██╗██║██║░░██║░╚██╗████╗██╔╝
    ██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗  ██║╚████║██║░░██║░░████╔═████║░
    ██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║  ██║░╚███║╚█████╔╝░░╚██╔╝░╚██╔╝░
    ╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░
        """)
    
def show_options():
    print('1. Cadastrar restaurante')
    print('2. Remover Restaurante')
    print('3. Listar restaurante')
    print('4. Ativar restaurante')
    print('5. Sair\n')


def operation():

    try:
        option = int(input('Escolha uma das opções: '))

        print(f'\nOpcao Escolhida: {option}\n')
        
        if option == 1:         #Funcoes do Function.py
            add_restaurant()
        elif option == 2:
            os.system('cls')
            remove_restaurant()
        elif option == 3:
            os.system('cls')
            show_restaurants()
        elif option == 4:
            os.system('cls') 
        elif option == 5:
            end_app()
        else:
            invalid_option()
    except:
        invalid_option()


def add_restaurant():
    os.system('cls')
    print('Operacao Escolhida: Cadastro\n\n')

    restaurant_name = str(input('Informe o nome do restaurante: '))
    # restaurant_type = str(input('Informe o tipo do restaurante(Ex: Hamburgueria): '))
    restaurants.append(restaurant_name)
    print(f'\n\nNome: {restaurant_name}')
    time.sleep(1.5)
    print('\n\nRestaurante Adicionado!')
    time.sleep(1.5)
    os.system('cls')
    small_main()

def show_restaurants():
    aux = 1
    os.system('cls')
    print('Operacao Escohida: Listagem\n\n')

    try: 
        if restaurants:
            for restaurant in restaurants:
                print(f'{aux} - {restaurant}')
                aux += 1
            print('\n\nListagem finalizada!\n\n')
        else:
            print('\nA Lista está vazia!\n\n')
    except Exception as error:
        print(f'\n\nNão foi possivel listar devido ao erro: {error}')
    time.sleep(3)
    small_main()

def remove_restaurant():
    os.system('cls')
    print('Operação Escolhida: Remoção\n')

    if not restaurants:
        print("Nenhum restaurante cadastrado.\n")
        return
    
    restaurant_name = input('Nome do restaurante a remover: ').strip()
    
    try:
        # Tenta remover diretamente (lança ValueError se não existir)
        restaurants.remove(restaurant_name)  # Case-sensitive
        print(f'\nRestaurante "{restaurant_name}" removido!\n')
    except ValueError:
        print(f'\nRestaurante "{restaurant_name}" não encontrado.\n')
    except Exception as error:
        print(f'\nErro inesperado: {error}')
        import traceback
        traceback.print_exc()
        
    small_main()
    

def end_app():  
    os.system('cls')
    print('\n\nEncerrando...\n\n')
    time.sleep(1.5)



def invalid_option():
    os.system('cls')
    print('\n\nOpção informada é inválida!')
    
    print('\nRetornando ao menu de opções...')
    time.sleep(2.5)
    os.system('cls')
    small_main()


