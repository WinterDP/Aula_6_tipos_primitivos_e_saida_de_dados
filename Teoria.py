'''
Anotações da aula 06 de python
Tipos primitívos e saída de dados

'''

#resolução do problema apresentado na última aula
print('\nrealize a soma de dois números\n')

#region resolução com problema
print('resolução do exercício com problema\n')

n1 = input('digite um numero ')
print(type(n1)) #análise e estudo dos tipos, método retorna o tipo primitivo da variável, esperava-se int mas temos str
n2 = input('digite um segundo numero ')
print(type(n2)) #análise dos tipos
soma = n1 + n2

print('a soma desses dois números é ', soma)

#endregion

#region resolução sem o problema

print('\nresolução do exercício sem o problema\n')

n1 = int( input('digite um numero ') ) # os números quando passados pelo usário são considerados strings, é nessessário informar que temos um número inteiro para manipular ou seja o tipo int
print(type(n1)) #análise dos tipos, agora temos o int esperado
n2 = int( input('digite um segundo numero ') )
print(type(n2)) #análise dos tipos
soma = n1 + n2 # Agora o simbolo de soma será utilizado para fazer a soma dos dois números inteiros e não a concatenação, pois deixamos claro qual tipo cada variável se refere

print('a soma desses dois números é ', soma)


#endregion

#region explicação de tipos primitivos

'''
principais tipos primitivos python
int: se referem aos números inteiros não possuem parte decimal
    exemplo: 7, 2, -2, 0, 500

float: se referem a valores reais com ponto flutuante
    exemplo: 6.5, 3.4, -2.6, -15.6, 6.0
    
bool: se referem aos tipos booleanos verdadeiro e falso
    "exemplo": True e False
str: se referem as "frases" e números que são tratados como os caracteres do computador
    obs: preferencia da comunidade por aspas simples no tratamento de strings
    exemplo: 'frase', '6.5', ''

'''

#endregion

# Strings formatadas com .format dão uma maior liberdade de formatação nas saídas para o usuário

print('\nmelhora da formatação com .format\n')

print('a soma dos numeros {} e {} é {}!!!'.format(n1, n2, soma)) # como é possivel tratar a string de saída como objeto, caracterisitica do python é possível usar o método format para a formatação da string com o uso de máscaras

# exibição de um mesmo número tratado como diferentes tipos
print('\nvalor 0 tratado como se fosse de tipos diferentes\n')


v = str(0)
print(type(v))
print()
v = int(0)
print(type(v))
print(v)
v = bool(0)
print(type(v))
print(v)
v = float(0)
print(type(v))
print(v)
