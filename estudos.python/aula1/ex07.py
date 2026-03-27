#// 7. Solicite ao usuário que insira sua data de nascimento e calcule sua idade.
data_nascimento = input("Insira sua data de nascimento (dd/mm/aaaa):")
data_nascimento = datetime.strptime(data_nascimento, "%d%m%Y")
data_atual = datetime.now()
idade = data_atual.year - data_nascimento.year
if (data_atual.month,data_atual.day) < (data_nascimento.month, data_nascimento.day): idade -= 1
print(f"Você tem {idade}anos.")