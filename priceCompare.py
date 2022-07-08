"""
Features:
- 1: Comparar preço de um produto específico
- 2: Listar total gasto em um mês
- 3: Adicionar Produto
- 4: Ajustar Preço
- 5: 
"""

"""
IDEIAS
- PRODUTOS COMO CLASSES, TENDO NOME, PREÇO, ETC. COMO ATRIBUTOS
- GENERALIZAR SUPERMERCADOS
"""

    #Usar um sistema de ID para melhor identificação

class shopList():
    def __init__(self):
        self.product_list = [] #Lista para a comparação dos preços
    def add_product(self):
    #Usar um sistema de ID para melhor identificação
        product_name = input("Informe o nome do produto\n>>>")
        product_brand = input("Informe o nome da marca do produto\n>>>")
        product_price = input("Informe o nome do preço\n>>>")
        product_date = input("Informe a data de compra do produto\n>>>")
        product_place = input("Informe o nome do estabelecimento de compra do produto\n>>>")
        self.product_list.append([ product_name, product_brand, product_price, product_date, product_place])

    def save_state(self):
        file = open("shopList.txt", "a")
        for item in self.price_list:
            for index,detail in enumerate(item):
                file.write(detail)
                if index == len(item)-1:
                    file.write("\n")
                else:
                    file.write(" ")
            

    def restore_state(self):
        file = open("shopList", "r")
        aux = []
        lines = file.readlines()
        for line in lines:
            item = line.replace("\n","")
            aux = item.split(" ")
            self.product_list.append(aux)

    def set_id(self):
        id_file = open("id_file.txt","r")
        id_number = int(id_file.read())
        id_file.close()
        id_file = open("id_file.txt","w")
        id_file.write(str(id_number+1))

        return id_number

    def reset_all(self):
        self.product_list.clear()
        with open("id_file.txt", 'r+') as f:
            f.truncate(0)

        with open("id_file.txt", 'w') as f:
            f.write("0")

        with open("priceList.txt", 'r+') as f:
            f.truncate(0)

        with open("shopList.txt", 'r+') as f:
            f.truncate(0)

#=====================================================
#=====================================================

class priceList(shopList):

    def __init__(self):
        shopList.__init__(self)
        
    def save_state(self):
        file = open("priceList.txt", "a")
        for item in self.product_list:
            for index,detail in enumerate(item):
                file.write(str(detail))
                if index == len(item)-1:
                    file.write("\n")
                else:
                    file.write(" ")
            

    def restore_state(self):
        file = open("priceList.txt", "r")
        aux = []
        lines = file.readlines()
        for line in lines:
            item = line.replace("\n","")
            aux = item.split(" ")
            self.product_list.append(aux)

    def add_product(self):

        product_name = input("Informe o nome do produto\n>>>")
        product_brand = input("Informe o nome da marca do produto\n>>>")
        product_price = input("Informe o preço\n>>>")
        product_place = input("Informe o nome do estabelecimento de compra do produto\n>>>")

        product_name = product_name.lower()
        product_brand = product_brand.lower()
        product_price = product_price.lower()
        product_place = product_place.lower()

        #Fazer uma busca binária aqui para otimizar
        if len(self.product_list) != 0:
            for item in self.product_list:      
                if product_name == item[1] and product_brand == item[2] and product_place == item[4]:
                    item[3] = product_price
                    print("Preço do produto atualizado")
                    return

            id = self.set_id()
            self.product_list.append([id, product_name, product_brand, float(product_price), product_place])
            print("Produto catalogado com sucesso!")
            return


        id = self.set_id()
        self.product_list.append([id, product_name, product_brand, float(product_price), product_place])
        print("Produto catalogado com sucesso!")

    def compare_individual(self,product_name):
        aux = []
        name = product_name.lower()
        target_item = None
        for item in self.product_list:
            if name == item[1]:
                aux.append(item)
        price = 99999
        print(aux)
        for item in aux:
            if item[3] < price:
                price = item[3]
                target_item = item
        if target_item == None:
            print("Produto inválido")
        return target_item
        

    def compare_for_shop(self):
        print("Digite o nome dos produtos abaixo(Digite 0 para parar):\n>>>")
        aux_dia = []
        aux_arco = []
        buy_item = 1
        while buy_item != "0":
            buy_item = input()
            if (buy_item != "0"):
                aux = self.compare_individual(buy_item)
                if (aux != None and aux[4]=="dia"):
                    aux_dia.append(aux)
                else:
                    aux_arco.append(aux)


        if (aux_dia != [None] and len(aux_dia) > 0):
            print("=======DIA=======")
            for target_item in aux_dia:
                print("Produto: " + str(target_item[1]))
                print("Marca: {}".format(target_item[2]))
                print("Preço: R${}".format(target_item[3]))
                print("\n")

        if (aux_arco != [None] and len(aux_arco) > 0):
            print("=======ARCO-ÍRIS=======")
            for target_item in aux_arco:
                print("Produto: " + str(target_item[1]))
                print("Marca: {}".format(target_item[2]))
                print("Preço: R${}".format(target_item[3]))
                print("\n")
        return
        
            
    def print_list(self):
        for item in self.product_list:
            print(item)


# Interface do programa
def initial_hub():
    opcao = 999
    lista_compras = priceList()
    lista_compras.restore_state()

    while opcao!=0:
        print("Escolha a sua operação:")
        print("1 - Comparar Preço Individual;")
        print("2 - Lista de compras")
        print("3 - Adicionar Produto ao Banco de Dados;")
        print("4 - Ver Banco de Dados")
        print("5 - Compras do Mês")
        print("5 - Remover Produto")
        print("0 - Sair")

        opcao = int(input())

        match opcao:
            case 1:
                item_name = input("Informe o nome do produto para ver o melhor preço:\n>>>")
                lista_compras.compare_individual(item_name)
            case 2:
                lista_compras.compare_for_shop()
            case 3:
                lista_compras.add_product()
            case 4:
                lista_compras.print_list()
            case 5:
                pass
            case 0:
                lista_compras.save_state()
                return
    lista_compras.save_state()
    return


if __name__ == '__main__':
   lista = shopList()
   lista.reset_all()
   initial_hub()


