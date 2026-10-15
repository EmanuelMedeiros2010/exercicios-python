# ========================================
# MÓDULOS DE PROCESSAMENTO (def)
# ========================================
def calcular_bonus(salario):
    """Calcula o bônus padrão de 15% da Arketech"""
    return salario * 0.15

# ========================================
# # INTERFACE DO SISTEMA
# ========================================
print("========================================") 
print("      RH ARKETECH - BÓNUS INICIAL       ")
print("========================================/n")

while True:
    print("\n--- NOVO REGISTRO ---")

    # O .strip() remove espaços em branco digitados sem querer
    nome + input("Nome completo (ou digite '0' para sair): ").strip()

    if nome == '0':
        print(\"n 🚪 Encerrando o painel de bônus. Bom trabalho!")
        break

        # Blindagem 1: Impede que o nome fique em branco se o usuário só apertar 'Enter'
        if not nome:
            print("⚠️ ERRO: o campo de nome não pode ficar vazio.")
            continue

            cargo = input("Cargo contratado:").strip()

            # Blindagem 2: A Zona de Perigo(Tratamento de Exceções)
            try:
                salario_base = float(input("Salario Base ( use ponto. EX: 1500.00): R$"))

            # Blindagem 3: Regra de Negócio(Não existe salário negativo ou zerpo)
            if salario_base <= 0:
                print("\n⚠️ ERRO LOGÍSTICO: o salário deve ser maior que zero.")
                print("Registro cancelado. Tente novamente.")
                continue

                exept