def menu(carro, opcao):
    CONS = 0

    if (0 < carro < 6):
        if (carro == 1):
            if (opcao == 'G'):
                CONS = 11.4
            elif (opcao == 'A'):
                CONS = 7.5
        elif (carro == 2):
            if (opcao == 'G'):
                CONS = 9.6
            elif (opcao == 'A'):
                CONS = 7.6
        elif (carro == 3):
            if (opcao == 'G'):
                CONS = 10.1
            elif (opcao == 'A'):
                CONS = 7.2
        elif (carro == 4):
            if (opcao == 'G'):
                CONS = 11.8
            elif (opcao == 'A'):
                CONS = 7.7
        elif (carro == 5):
            if (opcao == 'G'):
                CONS = 12.8
            elif (opcao == 'A'):
                CONS = 9.1

    return(CONS)

def destino(opcao, G, A):
    print('MENU DO DESTINO (partindo do IFSP)')
    print('------------------------------------------------------')
    print('1 - Casa')
    print("2 - McDonald's")
    print('3 - Shopping')
    print('4 - Getúlio Vargas')
    print('5 - Ibaté')
    print('------------------------------------------------------')

    CONSU = menu(carro, opcao)

    print()
    opc = int(input('Digite o nº do destino: '))
    volta = input('Deseja calcular a volta? (S/N): ')
    volta = volta.upper()

    if (opc == 1):
        if (volta == 'S'):
            KM = 5.2*2
            T = 9*2
            L = (5.2/CONSU)*2
        elif (volta == 'N'):
            KM = 5.2
            T = 9
            L = 5.2/CONSU

    elif (opc == 2):
        if (volta == 'S'):
            KM = 7.4*2
            T = 12*2
            L = (7.4/CONSU)*2
        elif (volta == 'N'):
            KM = 7.4
            T = 12
            L = 7.4/CONSU

    elif (opc == 3):
        if (volta == 'S'):
            KM = 10.9*2
            T = 19*2
            L = (10.9/CONSU)*2
        elif (volta == 'N'):
            KM = 10.9
            T = 19
            L = 10.9/CONSU

    elif (opc == 4):
        if (volta == 'S'):
            KM = 13.3*2
            T = 15*2
            L = (13.3/CONSU)*2
        elif (volta == 'N'): 
            KM = 13.3
            T = 15
            L = 13.3/CONSU  
        
    elif (opc == 5):
        if (volta == 'S'):
            KM = 17.9*2
            T = 18*2
            L = 17.9/CONSU*2
        elif (volta == 'N'):
            KM = 17.9
            T = 18
            L = 17.9/CONSU

    if (opcao == 'G'):
        COMBUS = GAS
    elif (opcao == 'A'):
        COMBUS = ALC

    total = round(L*COMBUS, 2)
    L = round(L, 2)
    
    print()
    print('------------------------------------------------------')
    print('Distância percorrida:', KM, 'km')
    print('------------------------------------------------------')
    print('Tempo gasto:', T, 'minutos')
    print('------------------------------------------------------')
    print('Valor gasto:', 'R$', total)
    print('------------------------------------------------------')
    print('Combustível gasto:', L, 'Litros')
    print('------------------------------------------------------')

print('------------------------------------------------------')
print('MENU DE CARROS')
print('------------------------------------------------------')
print('1 - Golf')
print('2 - Cruze')
print('3 - Astra')
print('4 - Civic')
print('5 - HB20')
print('------------------------------------------------------')

print()
carro = int(input('Digite o nº do carro desejado: '))
print()

opcao = input('Escolha o combustível a ser utilizado ("G" ou "A"): ')
opcao = opcao.upper()

print()
print('------------------------------------------------------')

GAS = 5.44
ALC = 3.78

menu(carro, opcao)
destino(opcao, GAS, ALC)