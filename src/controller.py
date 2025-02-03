from database import PostgreSQLConnection
from model import Atendente, Cliente, Pedido, ItemPedido, Pizza


class Controller:
    def __init__(self):
        self.__db = PostgreSQLConnection()
        self.__atendente = None
        self.__cliente = None
        self.__pedido = None


    def getAtendente(self):
        return self.__atendente
    

    def setAtendente(self, atendente: Atendente):
        self.__atendente = atendente


    def getCliente(self):
        return self.__cliente
    

    def setCliente(self, cliente: Cliente):
        self.__cliente = cliente


    def getPedido(self):
        return self.__pedido
    

    def setPedido(self, pedido: Pedido):
        self.__pedido = pedido


    def fazerLogin(self, usuario: str, senha: str):
        try:
            query = "SELECT * FROM ATENDENTE WHERE USUARIO = %s;"
            params = (usuario,)
            
            resposta = self.__db.execute_query(query, params, fetch=True)

            if resposta:
                senha_db = resposta[0][3]

                if senha == senha_db:
                    nome = resposta[0][1]
                    if self.cadastrarAtendente(nome, usuario, senha):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        except Exception as e:
            return False
    

    def cadastrarAtendente(self, nome: str, usuario: str, senha: str):
        atendente = Atendente(nome, usuario, senha)
        self.setAtendente(atendente)
        return True


    def cadastrarCliente(self, nome: str, endereco: str, fone: str, bairro: str):
        cliente = Cliente(nome, endereco, fone, bairro)
        self.setCliente(cliente)
        return True
        

    def cadastrarPedido(self, atendente: Atendente, cliente: Cliente, status: str ='Em aberto'):
        pedido = Pedido(atendente, cliente, status)
        self.setPedido(pedido)
        return True

    
    def montarPizza(self, sabor: str, tamanho: str, preco: float):
        pizza = Pizza(sabor, tamanho, preco)
        return pizza
    

    def montarItemPedido(self, pizza: Pizza, quantidade: int):
        itemPedido = ItemPedido(pizza, quantidade)
        return itemPedido


    def cadastrarClienteBD(self, cliente: Cliente):
        try:
            query = "INSERT INTO CLIENTE (NOME, ENDERECO, FONE, BAIRRO) VALUES (%s, %s, %s, %s)"
            params = (cliente.getNome(), cliente.getEndereco(), cliente.getFone(), cliente.getBairro())  # Sempre passar os parâmetros como tupla
            
            self.__db.execute_query(query, params)

            return True

        except Exception as e:
            return False


    def cadastrarPedidoBD(self, pedido: Pedido):
        try:
            atendente = pedido.getAtendente()
            cliente = pedido.getCliente()

            codAtend = self.buscarCodAten(atendente)
            codCli = self.buscarCodCli(cliente)
            valor = self.calcularValor(pedido)

            query = "INSERT INTO PEDIDO (COD_ATEN, COD_CLI, VALOR, STATUS) VALUES (%s, %s, %s, %s)"
            params = (codAtend, codCli, valor, pedido.getStatus())
            
            self.__db.execute_query(query, params)

            return True

        except Exception as e:
            return False
    

    def cadastrarItemPedidoBD(self, pedido: Pedido):
        try:
            codPed = self.buscarUltimoCodPed()
            itens = pedido.getItens()

            for item in itens:
                pizza = item.getPizza()
                codPiz = self.buscarCodPiz(pizza)
                quantidade = int(item.getQuantidade())

                query = "INSERT INTO ITEM_PEDIDO (COD_PED, COD_PIZ, QUANT) VALUES (%s, %s, %s)"
                params = (codPed, codPiz, quantidade)
            
                self.__db.execute_query(query, params)

            return True

        except Exception as e:
            return False
    
    
    def buscarSabores(self):
        try:
            sabores = []
            query = 'SELECT SABOR FROM PIZZA'
            params = ()
            
            resposta = self.__db.execute_query(query, params, fetch=True)

            for tupla in resposta:
                for sabor in tupla:
                    if sabor not in sabores:
                        sabores.append(sabor)

            return sabores
        
        except Exception as e:
            print("Erro ao buscar sabores:", e)
            return []


    def buscarPreco(self, sabor: str, tamanho: str):
        try:
            query = "SELECT PRECO FROM PIZZA WHERE SABOR = %s AND TAMANHO = %s;"
            params = (sabor, tamanho)
            
            resposta = self.__db.execute_query(query, params, fetch=True)

            preco = resposta[0][0]

            return preco

        except Exception as e:
            return False

    
    def buscarCodAten(self, atendente: Atendente):
        try:
            query = "SELECT COD_ATEN FROM ATENDENTE WHERE NOME = %s AND USUARIO = %s AND SENHA = %s;"
            params = (atendente.getNome(), atendente.getUsuario(), atendente.getSenha())

            resposta = self.__db.execute_query(query, params, fetch=True)

            codAtend = resposta[0][0]

            return codAtend

        except Exception as e:
            return False


    def buscarCodCli(self, cliente: Cliente):
        try:
            query = "SELECT COD_CLI FROM CLIENTE WHERE NOME = %s AND ENDERECO = %s AND FONE = %s AND BAIRRO = %s;"
            params = (cliente.getNome(), cliente.getEndereco(), cliente.getFone(), cliente.getBairro())

            resposta = self.__db.execute_query(query, params, fetch=True)

            codAtend = resposta[0][0]

            return codAtend

        except Exception as e:
            return False

    
    def buscarCodPiz(self, pizza: Pizza):
        try:
            query = "SELECT COD_PIZ FROM PIZZA WHERE SABOR = %s AND TAMANHO = %s;"
            params = (pizza.getSabor(), pizza.getTamanho())

            resposta = self.__db.execute_query(query, params, fetch=True)

            codPiz = resposta[0][0]

            return codPiz

        except Exception as e:
            return False


    def buscarUltimoCodPed(self):
        try:
            query = "SELECT COD_PED FROM PEDIDO ORDER BY COD_PED DESC LIMIT 1;"
            params = ()

            respota = self.__db.execute_query(query, params, fetch=True)

            codPed = respota[0][0]

            return codPed

        except Exception as e:
            return False
        
    
    def calcularValor(self, pedido: Pedido):
        valor = 0
        itens = pedido.getItens()

        for item in itens:
            pizza = item.getPizza()
            preco = pizza.getPreco()
            quantidade = item.getQuantidade()

            valor += preco * int(quantidade)

        return round(valor, 2)


    def limparDados(self):
        self.setCliente(None)
        self.setPedido(None)
