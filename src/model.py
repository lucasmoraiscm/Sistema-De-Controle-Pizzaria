class Atendente:
    def __init__(self, nome: str, usuario: str, senha: str):
        self.__nome = nome
        self.__usuario = usuario
        self.__senha = senha

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome: str):
        self.__nome = nome

    def getUsuario(self):
        return self.__usuario
    
    def setUsuario(self, usuario: str):
        self.__usuario = usuario

    def getSenha(self):
        return self.__senha

    def setSenha(self, senha: str):
        self.__senha = senha


class Cliente:
    def __init__(self, nome: str, endereco: str, fone: str, bairro: str):
        self.__nome = nome
        self.__endereco = endereco
        self.__fone = fone
        self.__bairro = bairro

    def getNome(self):
        return self.__nome

    def setNome(self, nome: str):
        self.__nome = nome

    def getEndereco(self):
        return self.__endereco
    
    def setEndereco(self, endereco: str):
        self.__endereco = endereco

    def getFone(self):
        return self.__fone
    
    def setFone(self, fone: str):
        self.__fone = fone

    def getBairro(self):
        return self.__bairro
    
    def setBairro(self, bairro: str):
        self.__bairro = bairro


class Pizza:
    def __init__(self, sabor: str,tamanho: str, preco: float):
        self.__sabor = sabor
        self.__tamanho = tamanho
        self.__preco = preco

    def getSabor(self):
        return self.__sabor
    
    def setSabor(self, sabor: str):
        self.__sabor = sabor

    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, tamanho: str):
        self.__tamanho = tamanho

    def getPreco(self):
        return self.__preco
    
    def setPreco(self, preco: float):
        self.__preco = preco


class Pedido:
    def __init__(self, atendente: Atendente, cliente: Cliente, status: str ='Em aberto'):
        self.__atendente = atendente
        self.__cliente = cliente
        self.__status = status
        self.__valor = 0
        self.__itens = []

    def getCliente(self):
        return self.__cliente
    
    def setCliente(self, cliente: Cliente):
        self.__cliente = cliente

    def getAtendente(self):
        return self.__atendente
    
    def setAtendente(self, atendente: Atendente):
        self.__atendente = atendente
    
    def getStatus(self):
        return self.__status
    
    def setStatus(self, status):
        self.__status = status
    
    def getValor(self):
        return self.__valor
    
    def adicionarValor(self, valor):
        self.__valor += valor

    def getItens(self):
        return self.__itens

    def adicionarItem(self, item):
        self.__itens.append(item)


class ItemPedido:
    def __init__(self, pizza: Pizza, quantidade: int):
        self.__pizza = pizza
        self.__quantidade = quantidade

    def getPizza(self):
        return self.__pizza
    
    def setPizza(self, pizza: Pizza):
        self.__pizza = pizza

    def getQuantidade(self):
        return self.__quantidade
    
    def setQuantidade(self, quantidade: int):
        self.__quantidade = quantidade
