#region Desafio 003
'''
Desafio 003

Some dois números colocados pelo usuário, utilizando 
somente os conceitos dados nessa aula


'''
print('\nDesafio 003 \n')


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma = n1+n2

print(soma) 


#endregion

#region Desafio 004
'''
Desafio 004

Faça um programa que leia algo pelo teclado e mostre 
o seu tipo primitivo e todas as informações possíveis 
sobre ela.


'''
print('\nDesafio 004 \n')


entrada = input('Digite algo: ')


print(type(entrada))
print('numérico: {} '.format(entrada.isnumeric()))
print('caixa alta: {}'.format(entrada.isupper()))
print('caixa baixa: {}'.format(entrada.islower()))
print('digito: {}'.format(entrada.isdigit()))

#endregion