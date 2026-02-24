import os
import time

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

