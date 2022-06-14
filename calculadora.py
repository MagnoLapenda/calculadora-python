print("\n******************* Python Calculator *******************")

#Tela descritiva de escolha do usuário

print('Escolha a operação desejada (1 a 4), conforme valores indicados abaixo:\n')
operacoes = ['1 - Adição', '2 - Subtração', '3 - Multiplicação', '4 - Divisão', '5 - Potência']
for x in operacoes:
    print(x)
    
#Coleta de escolha da operação matemática

while True:

    operacao = input('\nEfetuar operação: ')

    if (operacao == '1' or operacao == '2' or operacao == '3' or operacao == '4' or operacao == '5'):
        valor1_str = input('\nDigite o primeiro valor: ')
        valor2_str = input('\nDigite o segundo valor: ')
        valor1_int = int(valor1_str)
        valor2_int = int(valor2_str)
        break
    else:
        print('Esolha uma opção de 1 a 5.')
    continue

#Cálculo da operação

if operacao == '1':
    print('\n\n\033[1mO resultado da adição é: ', valor1_int+valor2_int)
if operacao == '2':
    print('\n\n\033[1mO resultado da subtração é: ', valor1_int-valor2_int)
if operacao == '3':
    print('\n\n\033[1mO resultado da multiplicação é: ', valor1_int*valor2_int)
if operacao == '4':
    print('\n\n\033[1mO resultado da divisão é: ', valor1_int/valor2_int)
if operacao == '5':
    print('\n\n\033[1mO resultado da potência é: ', valor1_int**valor2_int)
    
#MagnoLapenda

