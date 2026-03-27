
#// 8. Solicite ao usuário que insira seu nome e sobrenome .Em seguida, gere um e-mail concatenando a inicial do seu nome com o sobrenome seguindo de "@gmail.com". O e-mail deve esta todo em letras minúsculas.
#// exemplo: nome: Gustavo , sobrenome: Lavadenz , e-mail:glavadenz@gmail.com
nome = input("Por favor, insira seu nome: ")
sobrenome = input("Por favor, insira seu sobrenome: ")
email = f"{nome[0].lower()}{sobrenome.lower()}@gmail.com"
print("Seu e-mail gerado é:", email)
