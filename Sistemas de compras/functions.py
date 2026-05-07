
class Produto:

    def __init__(self, cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho

def act1(nome):

        print(f"Olá, {nome}. Estamos felizes em poder te ajudar!")
        reclamar = input("Nos conte o que há de errado: ")
        print("Estamos felizes em entender você!")
        print("Para que seu chamado possa ser resolvido, digite seu email de contato") 
        contato = input("Email: ")

        while len(reclamar) == 0:
            print("Digite algo!")
            reclamar = input("Deixe o seu feedback aqui: ")
            
        while "@" not in contato:
            print("Email inválido!")
            contato = input("Digite um email válido: ")
    
        print("Email validado! Aguarde até 3 dias úteis para que possamos contatar-lo.")

def act2(nome):

        print(f"Olá, {nome}. Qual informação necessitas?")
        info = input("Produto, Entrega, Empresa: ")

        roupa_produto = Produto("Vermelho", "M")
        tenis_produto = Produto("Azul", "37")

        def product():

            def product1():
                print("Cor: ", roupa_produto.cor)
                print("Tamanho: ", roupa_produto.tamanho)

            def product2():
                print("Cor: ", tenis_produto.cor)
                print("Tamanho: ", tenis_produto.tamanho)
            
            def product3():
                print("Sua roupa:")
                print("Cor: ", roupa_produto.cor)
                print("Tamanho: ", roupa_produto.tamanho)
                print("Seu tênis: ")
                print("Cor: ", tenis_produto.cor)
                print("Tamanho: ", tenis_produto.tamanho)

            print("Qual produto você adquiriu?")
            print("Digite 1 para roupa")
            print("Digite 2 para tênis")    
            print("Digite 3 para ambos")
            produto = int(input("Digite: "))

            if produto == 1:
                product1()
            elif produto == 2:
                product2()
            elif produto == 3:
                product3()        
            else:

                while produto not in [1,2,3]:

                    print("Apenas 1,2 ou 3!")
                    produto = int(input("Digite: "))

                    if produto == 1:
                        product1()
                        break
                    elif produto == 2:
                        product2()
                        break
                    elif produto == 3:
                        product3()
                        break

        def empresa():
            print(f"Olá, {nome}. Ficamos felizes de saber que você quer conhecer um pouco sobre a nossa empresa")
            print("Nosso objetivo é oferecer tênis e roupas que façam cada pessoa se sentir confiante e confortável sendo quem é. ")
            print("Queremos que cada peça carregue estilo, qualidade e um toque de identidade. ")
            print("Mais do que vender, desejamos criar uma conexão com quem entra na loja. ")
            print("Aqui, cada escolha é sobre sentir-se bem de verdade.")
        
        def entrega():  
            print(f"Olá, {nome}. O que gostaria de saber acerca da entrega?")
            print("Prazo de entrega: Nossos produtos levam de 7 a 15 dias para serem entregues.")
            print("O seu produto pode ser acompanhado pelo site dos correios, com o número da compra.")
            print("Número da compra: 123456AB")  


        if info in ["Produto", "produto"]:
            product()

        elif info in ["Entrega", "entrega"]: 
            entrega()
        
        elif info in ["Empresa", "empresa"]:
            empresa()
        
        else:

            while info not in ["Produto", "Entrega", "Empresa"]:

                print("Apenas essas três opções")
                print("Digite Sair para sair")
                info = input("Digite o que deseja fazer: ")

                if info in ["Sair", "sair"]:
                    break

                elif info in ["Produto", "produto"]:
                    product()
                    break

                elif info in ["Entrega", "entrega"]:
                    entrega()
                    break

                elif info in ["Empresa", "empresa"]:
                    empresa()
                    break

def act3(nome):

        print(f"Olá, {nome}. Gostaria de nos contar o por que deseja cancelar o produto?")
        input("Conte-nos: ")
        print("Informe o número de compra. Caso não saiba, digite ""Saber"" ")
        cancel = input("Número: ")

        def certo():
    
            print(f"{nome}, informe-nos seu email para enviar o número de protocolo: ")
            email = input("Email: ")

            while "@" not in email:
                print("Email inválido!")
                email = input("Digite um email válido: ")

            print("Email validado! Aguarde até 3 dias úteis para que possamos contatar-lo.") 

        def saber():

            print("Número de compra: 123456AB")
            cancel = input("Informe o número de compra: ")

            while "123456AB" not in cancel:
                print("Número inválido")
                cancel = input("Digite o número válido: ")

            certo()
            
        if cancel == "123456AB":
            certo()
        elif cancel in ["Saber", "saber"]:
            saber()
        else:
            raise Exception("(ERRO) Número inválido!")
        
def act4(nome):

        print(f"Olá, {nome}. Estamos felizes em receber o seu feedback!")
        feedback = input("Deixe o seu feedback aqui: ")
        email = input(f"{nome}, informe-nos seu email: ")

        while len(feedback) == 0:
            print("Digite algo!")
            feedback = input("Deixe o seu feedback aqui: ")

        while "@" not in email:
            print("Email inválido!")
            email = input("Digite um email válido: ")

        print("Email validado! Iremos entrar em contato para agradecer.")