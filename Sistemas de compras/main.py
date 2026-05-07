import functions

print("Seja bem-vindo ao sistema de compras!")
nome = input("Por favor, insira seu nome: ")
print(f"Olá, {nome}. O que deseja fazer?")
print("Para reclamar de algum produto: 1")
print("Para informações: 2")
print("Para cancelamento de produto: 3")
print("Para feedback geral: 4")
act = int(input("O que deseja fazer: "))

if act == 1:
    functions.act1(nome)

elif act == 2:
    functions.act2(nome)

elif act == 3:
    functions.act3(nome)

elif act == 4:
    functions.act4(nome)

else:

    while act not in [1,2,3,4]:

        print("Apenas uma das 4 opções!")
        act = int(input("O que deseja fazer: "))

        if act == 1:
            functions.act1(nome)
            break

        elif act == 2:
            functions.act2(nome)
            break

        elif act == 3:
            functions.act3(nome)
            break

        elif act == 4:
            functions.act4(nome)
            break

        else:
            print("Apenas uma das 4 opções!")
            break