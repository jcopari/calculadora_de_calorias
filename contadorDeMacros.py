
print('Bem-vindo ao contador de calorias e macros!')

peso = int(input('Qual o seu peso em Kg? R:'))
idade = int(input('Qual a sua idade? R:'))
altura = int(input('Qual sua altura em cm? R:'))
sexo = int(input(' Qual o seu sexo? \n Homem -> 1 Mulher -> 2 \n R: '))
atividade_fisica = int(input('Diga quanto de atividade você faz: \n\n Caso não pratique -> 1 \n Exercício leve de 1x a 3x na semana -> 2 \n Pratica exercício moderado de 3x a 5x na semana -> 3 \n 6x a 7x na semana, corpo completo -> 4 \n Se trabalha com esforço físico e treina 2x por dia -> 5 \n\n Digite o número correspondente: '))
exercicio = 1

def calculo_homem(Peso, Altura, Idade, Exercicio):
    soma = ((10 * Peso) + (6.25 * Altura) - (5 * Idade) + 5) * Exercicio
    return soma

def calculo_mulher(Peso, Altura, Idade, Exercicio):
    soma = ((10 * Peso) + (6.25 * Altura) - (5 * Idade) - 161) * Exercicio
    return soma

if(atividade_fisica == 1):
    exercicio = 1.2
elif(atividade_fisica == 2):
    exercicio = 1.375
elif(atividade_fisica == 3):
    exercicio = 1.55
elif(atividade_fisica == 4):
    exercicio = 1.725
elif(atividade_fisica == 5):
    exercicio = 1.9
else:
    print('Sua taxa metabólica será calculada sem o fator exercício')
    exercicio = 1


if(sexo == 1):
    print('A sua quantidade diária de calorias é: ', calculo_homem(peso, altura, idade, exercicio))
elif(sexo == 2):
    print('A sua quantidade diária de calorias é: ', calculo_mulher(peso, altura, idade, exercicio))
