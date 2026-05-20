#====================================
#! Ex. Básicos
#====================================
#? Exercício 1: Positivo ou Negativo
"""
numero = -3

if numero >= 0:
    print("Número positivo")
else:
    print("Número negativo")
"""

#? Exercício 2: Par ou Ímpar
"""
valor = 8

if valor % 2 == 0:
    print("É par")
else:
    print("É ímpar")
"""

#? Exercício 3: Pode ou não pode votar?
"""
idade = 15

if idade >= 16:
    print("Você já pode votar!")
else:
    print("Você ainda não pode votar.")
"""

#? Exercício 4: Alerta de Temperatura
"""
temperatura = 35

if temperatura > 30:
    print("Está muito quente, beba água!")
else:
    print("A temperatura está agradável.")
"""

#? Exercício 5: Frete Grátis
"""
valor_compra = 160.0

if valor_compra >= 150:
    print("Parabéns! Você ganhou frete grátis.")
else:
    print("O frete será cobrado.")
"""

#? Exercício 6: Sinal de Trânsito Simples
"""
sinal = "vermelho"

if sinal == "verde":
    print("Siga")
else:
    print("Pare")
"""
#====================================
#! Ex. Intermediários/Avançados
#====================================
#? Exercício 1: Saudação por Turno
"""
hora = int(input("Digite a hora atual (0 a 23): "))

if hora < 12:
    print("Bom dia!")
elif hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")
"""

#? Exercício 2: Qual é o Maior?
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"{num1} é maior")
elif num2 > num1:
    print(f"{num2} é maior")
else:
    print("Os números são iguais")
"""

#? Exercício 3: Aprovação com Faltas
"""
media = float(input("Digite a média do aluno: "))
faltas = int(input("Digite a quantidade de faltas: "))

if media >= 7.0 and faltas < 10:
    print("Aprovado")
else:
    print("Reprovado")
"""

#? Exercício 4: Permissão da Montanha-Russa
"""
altura = float(input("Digite sua altura em metros: "))

if altura >= 1.50:
    print("Pode ir sozinho")
elif altura >= 1.20:
    print("Só pode ir acompanhado")
else:
    print("Não pode ir")
"""

#? Exercício 5: Calculadora Básica
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite 1 para somar ou 2 para subtrair: ")

if operacao == "1":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif operacao == "2":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
else:
    print("Operação inválida")
"""

#? Exercício 6: Categoria de Idade Esportiva
"""
idade = int(input("Digite a idade do atleta: "))

if idade <= 12:
    print("Infantil")
elif idade <= 17:
    print("Juvenil")
else:
    print("Adulto")
"""

#? Exercício 7: Ano Bissexto
"""
ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    print("O ano tem 366 dias")
else:
    print("O ano tem 365 dias")
"""

#? Exercício 8: Lógica de Troco do Supermercado
"""
valor_compra = float(input("Digite o valor da compra: "))
valor_pago = float(input("Digite o valor pago: "))

if valor_pago < valor_compra:
    falta = valor_compra - valor_pago
    print(f"Falta dinheiro! Faltam R$ {falta:.2f}")
elif valor_pago == valor_compra:
    print("Pagamento exato, não há troco.")
else:
    troco = valor_pago - valor_compra
    print(f"Pagamento aprovado. Seu troco é de R$ {troco:.2f}")
"""

#? Exercício 9: Caixa Eletrônico
"""
valor = int(input("Digite o valor do saque: "))

if valor % 10 == 0:
    print("Saque autorizado")
else:
    print("Valor inválido. O caixa só opera com notas de R$ 10")
"""

#? Exercício 10: Triângulo Válido
"""
lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("As medidas formam um triângulo")
else:
    print("As medidas não formam um triângulo")
"""

#? Exercício 11: Classificador de Triângulos
"""
lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1 == lado2 == lado3:
    print("Triângulo Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")
"""

#? Exercício 12: Dano em Jogo de RPG
"""
ataque = int(input("Digite o poder de ataque: "))
defesa = int(input("Digite a defesa do monstro: "))

dano = ataque - defesa

if dano < 0:
    dano = 0

print(f"O monstro sofreu {dano} de dano!")
"""

#? Exercício 13: Doação de Sangue
"""
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

if idade >= 16 and idade <= 69 and peso > 50:
    print("Apto para doação")
else:
    print("Não apto para doação")
"""

#? Exercício 14: Calculadora de Imposto de Renda
"""
salario = float(input("Digite o salário: "))

if salario <= 2000:
    print("Isento de Imposto")
elif salario <= 5000:
    imposto = salario * 0.10
    print(f"Imposto: R$ {imposto:.2f}")
else:
    imposto = salario * 0.20
    print(f"Imposto: R$ {imposto:.2f}")
"""

#? Exercício 15: Rodízio de Veículos
"""
final_placa = int(input("Digite o número final da placa: "))

if final_placa == 1 or final_placa == 2:
    print("Não roda na Segunda-feira")
elif final_placa == 3 or final_placa == 4:
    print("Não roda na Terça-feira")
else:
    print("O carro roda normalmente nos primeiros dias da semana")
"""

#? Exercício 16: Identificador de Trimestre
"""
mes = int(input("Digite o número do mês: "))

if mes >= 1 and mes <= 3:
    print("1º Trimestre")
elif mes >= 4 and mes <= 6:
    print("2º Trimestre")
elif mes >= 7 and mes <= 9:
    print("3º Trimestre")
elif mes >= 10 and mes <= 12:
    print("4º Trimestre")
else:
    print("Mês inválido")
"""
#====================================