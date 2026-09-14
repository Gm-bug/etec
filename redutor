# Sistema de desconto progressivo
# Este programa calcula o desconto de acordo com o valor da compra.

# Solicita ao usuário o valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica qual percentual de desconto deve ser aplicado
if valor_compra < 200:
    percentual_desconto = 0.05  # 5% de desconto
elif valor_compra < 300:
    percentual_desconto = 0.10  # 10% de desconto
else:
    percentual_desconto = 0.15  # 15% de desconto

# Calcula o valor do desconto
valor_desconto = valor_compra * percentual_desconto

# Calcula o valor final após aplicar o desconto
valor_final = valor_compra - valor_desconto

# Exibe os resultados para o usuário
print("\n--- RESUMO DA COMPRA ---")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {percentual_desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")
