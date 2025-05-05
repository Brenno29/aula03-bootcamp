CONSTANTE_BONUS = 1000
nome_usuario = input("Digite o seu nome: ")
salario_usuario = float(input("Digite o seu salário: "))
bonus_usuario = float(input("Digite o seu bonus: "))

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

print(f"O usuario {nome_usuario} possue o bonus de {valor_do_bonus}.")