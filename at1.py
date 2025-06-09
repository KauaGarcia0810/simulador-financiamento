print('BEM VINDO(a) AO FINANCIAMENTO DE CASA DO KAUÂ!')

p = input('Então você quer comprar uma casa? ').strip().lower()

if p == 'sim' or p == 'claro':
    print('O senhor veio no lugar certo!')

    nome = input('Qual seu nome? ')
    print(f'Certo {nome}, preciso de algumas informações sua.')

    g1 = float(input('Qual é o valor da casa que o senhor planeja comprar? '))
    g2 = float(input('Quanto o senhor recebe? '))

    unidade = input(
        'Você quer pagar a casa em "anos" ou "meses"? ').strip().lower()
    if unidade == 'anos':
        g3 = float(input('Em quantos anos o senhor planeja quitar a casa? '))
        meses = g3 * 12
    elif unidade == 'meses':
        meses = float(
            input('Em quantos meses o senhor planeja quitar a casa? '))
    else:
        print('Opção inválida, vou considerar pagamento em anos.')
        g3 = float(input('Em quantos anos o senhor planeja quitar a casa? '))
        meses = g3 * 12

    s1 = g1 / meses
    print(f'Tudo bem, a prestação da casa vai ficar: R$ {s1:.2f} por mês.')

    limite = g2 * 0.30

    if s1 > limite:
        print('\033[1;31mFinanciamento negado!\033[m')
    else:
        print('\033[1;32mFinanciamento aprovado!\033[m')

else:
    print('Tudo bem! Tenha um bom dia.')
