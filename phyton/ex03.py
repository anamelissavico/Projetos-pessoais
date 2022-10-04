continuar=1
while continuar==1:
    print(f' Bem vindo a nossa academia!')
    plano= int(input("Olá qual plano você gostaria de assinar?\n [1] musculação\n [2] musculação + funcional\n [3] crossfit\n"))

    if plano==1:
        dias_semana=int(input(f'Os planos de musculação tem as seguintes frequências:\n [1] 2 dias na semana\n [2] 3 dias na semana \n [3] livre\n Que plano você gostaria de assinar?\n'))
        if dias_semana==1:
            print(f'O valor do plano é 80 reais.')
        elif dias_semana==2:
            print(f'O valor do plano é 100 reais.')
        elif dias_semana==3:
            print(f'O valor do plano é 120 reais.')
        elif dias_semana>3:
            continuar= int(input('Essa não é uma opção válida, deseja escolher uma nova opção?\n [1] Sim, quero escolher novamente. \n [2] Não, quero sair.\n'))

    elif plano==2:
        dias_semana=int(input(f'Os planos de musculação + funcional tem as seguintes frequências:\n [1] 2 dias na semana\n [2] 3 dias na semana \n [3] livre\n Que plano você gostaria de assinar?\n'))
        if dias_semana==1:
            print(f'O valor do plano é 120 reais.')
        elif dias_semana==2:
            print(f'O valor do plano é 140 reais.')
        elif dias_semana==3:
            print(f'O valor do plano é 170  reais.')
        elif dias_semana>3:
                continuar= int(input('Essa não é uma opção válida, deseja escolher uma nova opção?\n [1] Sim, quero escolher novamente. \n [2] Não, quero sair.\n'))
    elif plano==3:
        dias_semana=int(input(f'Os planos de crossfit tem as seguintes frequências:\n [1] 2 dias na semana\n [2] 3 dias na semana \n [3] livre\n Que plano você gostaria de assinar?\n'))
        if dias_semana==1:
            print(f'O valor do plano é 120 reais.')
        elif dias_semana==2:
            print(f'O valor do plano é 160 reais.')
        elif dias_semana==3:
            print(f'O valor do plano é 200 reais.')
        elif dias_semana>3:
            continuar= int(input('Essa não é uma opção válida, deseja escolher uma nova opção?\n [1] Sim, quero escolher novamente. \n [2] Não, quero sair.\n'))
        continuar=2
    elif plano>3:
        print('Essa não é uma opção válida.')
        continuar= int(input('Deseja escolher uma nova opção?\n [1] Sim, quero escolher novamente. \n [2] Não, quero sair.\n'))
print('Obrigada por escolher a gente, Bora malhar!!!!')
print('──────────────────────────────────\n'
'──▄██─────────────────────────██▄─\n'
'─████──▄▄▄▄─────────────▄▄▄▄──████\n'
'─██████▐▐▐▐█████████████▐▐▐▐██████\n'
'─████──▀██▀─────────────▀██▀──████\n'
'──▀██───██───────────────██───██▀─\n'
'────────██───────────────██───────\n'
'────────██───────────────██───────\n'
'██████──██▄█████▄─▄█████▄██───────\n'
'──██────███████████████████───────\n'
'──██────████▌▐███████▌▐████───────\n'
'──██────███████████████████───────\n'
'──██────███████████████████───────\n'
'──██────█████▌▐█████▌▐█████───────\n'
'──██─────██████▄▄▄▄▄██████────────\n'
'──██──────███████████████─────────\n'
'──██───────█████████████──────────\n'
'──██────────▀█████████▀───────────\n'
'──██──────────▀█████▀─────────────\n'
'██████──────────▀█▀───────────────\n'
'──────────────────────────────────\n'
'─█▀▀──▀──▀█▀──█▀▀▄──▄▀▀──▄▀▀──▄▀▀─\n'
'─█────█───█───█──█──█────█────█───\n'
'─█▀▀──█───█───█──█──█▀▀───▀▄───▀▄─\n'
'─█────█───█───█──█──█──────█────█─\n'
'─█────█───█───█──█──▀▄▄──▄▄▀──▄▄▀─\n')