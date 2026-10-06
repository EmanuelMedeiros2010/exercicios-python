idade = int(input("Idade do candidato: "))
if idade >= 18:
    print("✅ Acesso liberado ao sistema de Rh")
    print("Iniciando processo de admissão...")
else:
    print("❌ Acessso negado. O candidato deve ter pelo menos 18 anos.")