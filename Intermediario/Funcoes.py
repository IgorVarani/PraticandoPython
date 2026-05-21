#====================================
#! Ex. Intermediários
#====================================
#? Exercício 1: Calculadora de Desconto
"""
def aplicar_desconto(preco, porcentagem):
    desconto = preco * porcentagem
    return desconto

preco = int(input("Qual o preço do produto? "))
porcentagem = .2
resultado_desconto = aplicar_desconto(preco, porcentagem)
resultado_final = preco - resultado_desconto
print(f"Valor do desconto: R${resultado_desconto:.2f}")
print(f"Preço do produto com desconto: R${resultado_final:.2f}")
"""

#? Exercício 2: Validador de Senha Segura
"""
def validar_senha(caracteres):
    if len(caracteres) < 8:
        print("Senha fraca demais!")
        return False
    else:
        print("Senha forte o suficiente!")
        return True

senha = input("Digite sua senha: ")
validar_senha(senha)
"""

#? Exercício 3: Classificador de Temperatura
"""
def analisar_clima(temperatura):
    if temperatura < 15:
        print("Frio! ❄️")
    if temperatura >= 15:
        print("Agradável! ⛅")
    if temperatura > 25:
        print("Calor! ☀️")

temperatura = int(input("A temperatura está em quantos graus? "))
analisar_clima(temperatura)
"""