# Pesquisa de Opinião - Atendimento ao Cliente
# Empresa: TudoWeb
# Estruturas utilizadas: repetição (for) e decisão (if/elif/else)

# Para validar o programa, use 10 entrevistados.
# Para a versão final da atividade, altere o valor abaixo para 50.
QUANTIDADE_ENTREVISTADOS = 10

# Contadores das opiniões pedidas no enunciado
qtd_excelente = 0
qtd_ruim = 0

print("=" * 50)
print("   PESQUISA DE OPINIAO - ATENDIMENTO TUDOWEB")
print("=" * 50)
print("Opinioes validas:")
print("  1 - EXCELENTE")
print("  2 - BOM")
print("  3 - RUIM")
print("=" * 50)

# Estrutura de repetição para coletar os dados de cada entrevistado
for i in range(1, QUANTIDADE_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {QUANTIDADE_ENTREVISTADOS} ---")

    nome = input("Digite o nome: ").strip()

    # Validação simples da idade (precisa ser um número)
    while True:
        idade_texto = input("Digite a idade: ").strip()
        if idade_texto.isdigit() and int(idade_texto) > 0:
            idade = int(idade_texto)
            break
        print("Idade invalida. Digite um numero inteiro positivo.")

    # Validação da opinião (apenas 1, 2 ou 3)
    while True:
        opiniao_texto = input("Digite a opiniao (1=EXCELENTE, 2=BOM, 3=RUIM): ").strip()
        if opiniao_texto in ("1", "2", "3"):
            opiniao = int(opiniao_texto)
            break
        print("Opiniao invalida. Digite apenas 1, 2 ou 3.")

    # Estrutura de decisão para verificar a opinião
    if opiniao == 1:
        qtd_excelente += 1
        descricao = "EXCELENTE"
    elif opiniao == 2:
        descricao = "BOM"
    elif opiniao == 3:
        qtd_ruim += 1
        descricao = "RUIM"
    else:
        descricao = "INVALIDA"

    print(f"Registrado: {nome}, {idade} anos, opiniao {descricao}.")

# Relatório final pedido no enunciado
print("\n" + "=" * 50)
print("           RESULTADO DA PESQUISA")
print("=" * 50)
print(f"a) Quantidade de respostas EXCELENTE: {qtd_excelente}")
print(f"b) Quantidade de respostas RUIM: {qtd_ruim}")
print("=" * 50)
print("Pesquisa encerrada. Obrigado!")
