#====================================
#! Ex. Intermediários
#====================================
#? Exercício 1: Tabuada Personalizada
"""
numero = int(input("Digite um número inteiro: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
"""

#? Exercício 2: Somando Cinco Números
"""
soma = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    soma += numero

print(f"Soma total: {soma}")
"""

#? Exercício 3: Menu de Opções Simples
"""
while True:
    print("1 - Continuar")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Você escolheu continuar!")

    elif opcao == "2":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")
"""

#? Exercício 4: Média de Notas com Número Fixo
"""
soma = 0

for i in range(4):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma += nota

media = soma / 4

print(f"Média da equipe: {media}")
"""

#? Exercício 5: Quadrado dos Números
"""
limite = int(input("Digite um número limite: "))

for i in range(1, limite + 1):
    print(f"{i} ao quadrado = {i * i}")
"""

#? Exercício 6: Repetição com Validação de Texto
"""
while True:
    palavra = input("Digite a palavra 'confirmar': ")

    if palavra == "confirmar":
        print("Palavra correta!")
        break

    else:
        print("Tente novamente.")
"""

#? Exercício 7: Filtro de Números Pares
"""
limite = int(input("Digite um número limite: "))

for i in range(1, limite + 1):

    if i % 2 == 0:
        print(i)
"""

#? Exercício 8: O Caixa Eletrônico Infinito
"""
saldo = 500

while True:
    saque = float(input("Digite o valor do saque (0 para sair): "))

    if saque == 0:
        print("Programa encerrado!")
        break

    elif saque <= saldo:
        saldo -= saque
        print("Saque realizado!")
        print(f"Saldo atual: R$ {saldo}")

    else:
        print("Saldo insuficiente!")
"""

#? Exercício 9: Contador de Maiores de Idade
"""
quantidade = int(input("Quantas pessoas vão viajar? "))

maiores = 0

for i in range(quantidade):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))

    if idade >= 18:
        maiores += 1

print(f"Total de maiores de idade: {maiores}")
"""

#? Exercício 10: Somador de Valores Positivos com Alerta
"""
soma = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break

    elif numero < 0:
        print("Números negativos são ignorados!")

    else:
        soma += numero

print(f"Total acumulado: {soma}")
"""

#? Exercício 11: Descobrindo o Maior Número Informado
"""
maior_numero = 0

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número digitado foi: {maior_numero}")
"""

#? Exercício 12: Sistema de Login com Limite de Tentativas
"""
senha_correta = "admin"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso liberado!")
        break

    else:
        tentativas += 1
        print("Senha incorreta!")

if tentativas == 3:
    print("Conta bloqueada!")
"""

#? Exercício 13: O Separador de Ímpares e Pares
"""
for i in range(1, 16):

    if i % 2 == 0:
        print(f"O número {i} é PAR")

    else:
        print(f"O número {i} é ÍMPAR")
"""

#? Exercício 14: Cadastro de Produtos com Alerta de Preço
"""
soma = 0

for i in range(3):
    preco = float(input(f"Digite o preço do produto {i + 1}: "))

    soma += preco

    if preco > 100:
        print("Produto de Luxo detectado!")

print(f"Soma total dos produtos: R$ {soma}")
"""

#? Exercício 15: Jogo do "Plim" (Múltiplos de 4)
"""
for i in range(1, 21):

    if i % 4 == 0:
        print("PLIM!")

    else:
        print(i)
"""

#? Exercício 16: Pesquisa de Satisfação de Clientes
"""
satisfeitos = 0
insatisfeitos = 0

while True:
    nota = int(input("Qual nota você dá para o atendimento (1 a 5 ou 0 para encerrar)? "))

    if nota == 0:
        break

    elif nota == 4 or nota == 5:
        satisfeitos += 1

    elif nota >= 1 and nota <= 3:
        insatisfeitos += 1

    else:
        print("Nota inválida!")

print(f"Clientes satisfeitos: {satisfeitos}")
print(f"Clientes insatisfeitos: {insatisfeitos}")
"""