from controller import Controller
import customtkinter as ctk


controller = Controller()
ctk.set_appearance_mode("light")


class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Sistema de Controle - Pizzaria')
        self.geometry('1000x500')
        self.after(100, self.state, "zoomed")

        self.labelTitulo = ctk.CTkLabel(self, text='LOGIN', font=('Arial', 20))
        self.labelTitulo.pack(padx=10, pady=20)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20)

        self.labelUsuario = ctk.CTkLabel(self.frame, text='USUÁRIO', font=('Arial', 14))
        self.labelUsuario.grid(row=0, column=0, padx=10, pady=10)

        self.entryUsuario = ctk.CTkEntry(self.frame, placeholder_text='Digite seu usuário')
        self.entryUsuario.grid(row=1, column=0, padx=10, pady=10)

        self.labelSenha = ctk.CTkLabel(self.frame, text='SENHA', font=('Arial', 14))
        self.labelSenha.grid(row=2, column=0, padx=10, pady=10)

        self.entrySenha = ctk.CTkEntry(self.frame, placeholder_text='Digite sua senha', show='*')
        self.entrySenha.grid(row=3, column=0, padx=10, pady=10)

        self.buttomLogin = ctk.CTkButton(self, text='Login', fg_color='green', hover_color='darkgreen', command=self.fazerLogin)
        self.buttomLogin.pack(padx=10, pady=10)

        self.labelResposta = ctk.CTkLabel(self, text='', font=('Arial', 14), text_color='red')
        self.labelResposta.pack(padx=10, pady=10)

    def fazerLogin(self):
        usuario = self.entryUsuario.get()
        senha = self.entrySenha.get()

        if controller.fazerLogin(usuario, senha):
            self.destroy()
            Menu()
        else:
            self.labelResposta.configure(text="Usuário ou senha incorretos!", text_color="red")


class Menu(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title('Sistema de Controle - Pizzaria')
        self.state("zoomed")

        self.labelTitulo = ctk.CTkLabel(self, text='MENU INICIAL', font=('Arial', 20))
        self.labelTitulo.pack(padx=10, pady=20)
        
        self.buttomRegistrarPedido = ctk.CTkButton(self, text='Registrar Pedido', fg_color='green', hover_color='darkgreen', command=self.registrarPedido)
        self.buttomRegistrarPedido.pack(padx=10, pady=10)

    def registrarPedido(self):
        self.destroy()
        RegistrarPedidoCliente()


class RegistrarPedidoCliente(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title('Sistema de Controle - Pizzaria')
        self.state("zoomed")

        self.labelTitulo = ctk.CTkLabel(self, text='REGISTRAR PEDIDO', font=('Arial', 20))
        self.labelTitulo.pack(padx=10, pady=20)

        self.labelCliente = ctk.CTkLabel(self, text='CLIENTE', font=('Arial', 16))
        self.labelCliente.pack(padx=10)

        self.frameDadosCliente = ctk.CTkFrame(self)
        self.frameDadosCliente.pack(pady=20)

        self.labelNomeCliente = ctk.CTkLabel(self.frameDadosCliente, text='NOME')
        self.labelNomeCliente.grid(row=0, column=0, padx=10, pady=10)

        self.entryNomeCliente = ctk.CTkEntry(self.frameDadosCliente, placeholder_text='Digite o nome')
        self.entryNomeCliente.grid(row=0, column=1, padx=10, pady=10)

        self.labelEnderecoCliente = ctk.CTkLabel(self.frameDadosCliente, text='ENDEREÇO')
        self.labelEnderecoCliente.grid(row=1, column=0, padx=10, pady=10)

        self.entryEnderecoCliente = ctk.CTkEntry(self.frameDadosCliente, placeholder_text='Digite o endereço')
        self.entryEnderecoCliente.grid(row=1, column=1, padx=10, pady=10)

        self.labelFoneCliente = ctk.CTkLabel(self.frameDadosCliente, text='TELEFONE')
        self.labelFoneCliente.grid(row=2, column=0, padx=10, pady=10)

        self.entryFoneCliente = ctk.CTkEntry(self.frameDadosCliente, placeholder_text='Digite o telefone')
        self.entryFoneCliente.grid(row=2, column=1, padx=10, pady=10)

        self.labelBairroCliente = ctk.CTkLabel(self.frameDadosCliente, text='BAIRRO')
        self.labelBairroCliente.grid(row=3, column=0, padx=10, pady=10)

        self.entryBairroCliente = ctk.CTkEntry(self.frameDadosCliente, placeholder_text='Digite o bairro')
        self.entryBairroCliente.grid(row=3, column=1, padx=10, pady=10)

        self.frameBotaoCliente = ctk.CTkFrame(self)
        self.frameBotaoCliente.pack(pady=20)

        self.buttomRegistrarCliente = ctk.CTkButton(self.frameBotaoCliente, text='Registrar Cliente', fg_color='green', hover_color='darkgreen', command=self.registrarPedidoCliente)
        self.buttomRegistrarCliente.grid(row=0, column=0, padx=10, pady=10)

        self.buttomResetarCliente = ctk.CTkButton(self.frameBotaoCliente, text='Resetar', fg_color='#ff9500', hover_color='#ff7b00', command=self.resetarPedidoCliente)
        self.buttomResetarCliente.grid(row=0, column=1, padx=10, pady=10)

        self.labelRespostaCliente = ctk.CTkLabel(self, text='', font=('Arial', 14), text_color='red')
        self.labelRespostaCliente.pack(padx=10, pady=10)

    def registrarPedidoCliente(self):
        nome = self.entryNomeCliente.get()
        endereco = self.entryEnderecoCliente.get()
        fone = self.entryFoneCliente.get()
        bairro = self.entryBairroCliente.get()

        if nome and endereco and fone and bairro:
            controller.cadastrarCliente(nome, endereco, fone, bairro)
            controller.cadastrarPedido(controller.getAtendente(), controller.getCliente())
            self.destroy()
            RegistrarPedidoPizza()
        else:
            self.labelRespostaCliente.configure(text="Dados incompletos ou incorretos!", text_color="red")

    def resetarPedidoCliente(self):
        self.destroy()
        RegistrarPedidoCliente()


class RegistrarPedidoPizza(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title('Sistema de Controle - Pizzaria')
        self.state("zoomed")

        self.labelTitulo = ctk.CTkLabel(self, text='REGISTRAR PEDIDO', font=('Arial', 20))
        self.labelTitulo.pack(padx=10, pady=20)

        self.labelCliente = ctk.CTkLabel(self, text='PIZZA', font=('Arial', 16))
        self.labelCliente.pack(padx=10)

        self.framePizza = ctk.CTkFrame(self)
        self.framePizza.pack(pady=20)

        self.labelSabor = ctk.CTkLabel(self.framePizza, text='SABOR', font=('Arial', 14))
        self.labelSabor.grid(row=0, column=0, padx=10, pady=10)

        self.comboSabor = ctk.CTkComboBox(self.framePizza, values=self.carregarSabores())
        self.comboSabor.grid(row=1, column=0, pady=10, padx=10)

        self.labelTamanho = ctk.CTkLabel(self.framePizza, text='TAMANHO', font=('Arial', 14))
        self.labelTamanho.grid(row=0, column=1, padx=10, pady=10)

        self.comboTamanho = ctk.CTkComboBox(self.framePizza, values=["Média", "Grande", "Gigante"])
        self.comboTamanho.grid(row=1, column=1, pady=10, padx=10)

        self.labelQuantidade = ctk.CTkLabel(self.framePizza, text='QUANTIDADE', font=('Arial', 14))
        self.labelQuantidade.grid(row=0, column=2, padx=10, pady=10)

        self.entryQuantidade = ctk.CTkEntry(self.framePizza, placeholder_text='Digite a quantidade')
        self.entryQuantidade.grid(row=1, column=2, padx=10, pady=10)

        self.buttomAdicionarPizza = ctk.CTkButton(self.framePizza, text='Adicionar', fg_color='green', hover_color='darkgreen', command=self.adicionarPizza)
        self.buttomAdicionarPizza.grid(row=2, column=1, padx=10, pady=10)

        self.frameAdicionada = ctk.CTkFrame(self)
        self.frameAdicionada.pack(pady=20)

        self.labelQuantidadePizza = ctk.CTkLabel(self.frameAdicionada, text='QUANTIDADE', font=('Arial', 14))
        self.labelQuantidadePizza.grid(row=0, column=0, padx=10, pady=10)

        self.labelSaborPizza= ctk.CTkLabel(self.frameAdicionada, text='SABOR', font=('Arial', 14))
        self.labelSaborPizza.grid(row=0, column=1, padx=10, pady=10)

        self.labelTamanhoPizza = ctk.CTkLabel(self.frameAdicionada, text='TAMANHO', font=('Arial', 14))
        self.labelTamanhoPizza.grid(row=0, column=2, padx=10, pady=10)

        self.labelPrecoPizza = ctk.CTkLabel(self.frameAdicionada, text='PREÇO (R$)', font=('Arial', 14))
        self.labelPrecoPizza.grid(row=0, column=3, padx=10, pady=10)

        self.labelRespostaPizza = ctk.CTkLabel(self, text='', font=('Arial', 14), text_color='green')
        self.labelRespostaPizza.pack(padx=10, pady=10)

        self.buttomConfirmarPedido = ctk.CTkButton(self, text='Confirmar Pedido', fg_color='green', hover_color='darkgreen', command=self.confirmarPedido)
        self.buttomConfirmarPedido.pack(padx=10, pady=10)

    def carregarSabores(self):
        sabores = controller.buscarSabores()
        return sabores

    def adicionarPizza(self):
        sabor = self.comboSabor.get()
        tamanho = self.comboTamanho.get()
        quantidade = self.entryQuantidade.get()

        if quantidade.isdigit() and int(quantidade) > 0:
            preco = controller.buscarPreco(sabor, tamanho)
            pizza = controller.montarPizza(sabor, tamanho, preco)

            itemPedido = controller.montarItemPedido(pizza, quantidade)
            pedido = controller.getPedido()
            pedido.adicionarItem(itemPedido)

            linha = 1

            for item in pedido.getItens():
                pizza = item.getPizza()
                sabor = pizza.getSabor()
                tamanho = pizza.getTamanho()
                preco = pizza.getPreco()
                quantidade = int(item.getQuantidade())
            
                ctk.CTkLabel(self.frameAdicionada, text=f"{quantidade}", font=('Arial', 13)).grid(row=linha, column=0, padx=10, pady=5)
                ctk.CTkLabel(self.frameAdicionada, text=f"{sabor}", font=('Arial', 13)).grid(row=linha, column=1, padx=10, pady=5)
                ctk.CTkLabel(self.frameAdicionada, text=f"{tamanho}", font=('Arial', 13)).grid(row=linha, column=2, padx=10, pady=5)
                ctk.CTkLabel(self.frameAdicionada, text=f"{preco:.2f}", font=('Arial', 13)).grid(row=linha, column=3, padx=10, pady=5)
            
                linha += 1
        
            self.labelRespostaPizza.configure(text=" ", text_color="green")
            self.labelRespostaPizza.configure(text="Pizza adicionada ao pedido!", text_color="green")

        else:
            self.labelRespostaPizza.configure(text=" ", text_color="red")
            self.labelRespostaPizza.configure(text="Quantidade inválida!", text_color="red")

    def confirmarPedido(self):
        self.destroy()
        ResumoPedido()


class ResumoPedido(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title('Sistema de Controle - Pizzaria')
        self.state("zoomed")

        self.labelTitulo = ctk.CTkLabel(self, text='REGISTRAR PEDIDO', font=('Arial', 20))
        self.labelTitulo.pack(padx=10, pady=20)

        self.labelCliente = ctk.CTkLabel(self, text='RESUMO DO PEDIDO', font=('Arial', 16))
        self.labelCliente.pack(padx=10)

        self.frameCliente = ctk.CTkFrame(self)
        self.frameCliente.pack(pady=20)

        cliente = controller.getCliente()
        nome = cliente.getNome()
        endereco = cliente.getEndereco()
        fone = cliente.getFone()
        bairro = cliente.getBairro()

        self.labelNomeCliente = ctk.CTkLabel(self.frameCliente, text='NOME:', font=('Arial', 14))
        self.labelNomeCliente.grid(row=0, column=0, padx=10, pady=10)

        self.labelNomeClienteRegistrado = ctk.CTkLabel(self.frameCliente, text=f'{nome}', font=('Arial', 13))
        self.labelNomeClienteRegistrado.grid(row=0, column=1, padx=10, pady=10)

        self.labelEnderecoCliente = ctk.CTkLabel(self.frameCliente, text='ENDEREÇO:', font=('Arial', 14))
        self.labelEnderecoCliente.grid(row=1, column=0, padx=10, pady=10)

        self.labelEnderecoClienteRegistrado = ctk.CTkLabel(self.frameCliente, text=f'{endereco}', font=('Arial', 13))
        self.labelEnderecoClienteRegistrado.grid(row=1, column=1, padx=10, pady=10)

        self.labelFoneCliente = ctk.CTkLabel(self.frameCliente, text='TELEFONE:', font=('Arial', 14))
        self.labelFoneCliente.grid(row=2, column=0, padx=10, pady=10)

        self.labelFoneClienteRegistrado = ctk.CTkLabel(self.frameCliente, text=f'{fone}', font=('Arial', 13))
        self.labelFoneClienteRegistrado.grid(row=2, column=1, padx=10, pady=10)

        self.labelBairroCliente = ctk.CTkLabel(self.frameCliente, text='BAIRRO:', font=('Arial', 14))
        self.labelBairroCliente.grid(row=3, column=0, padx=10, pady=10)

        self.labelBairroClienteRegistrado = ctk.CTkLabel(self.frameCliente, text=f'{bairro}', font=('Arial', 13))
        self.labelBairroClienteRegistrado.grid(row=3, column=1, padx=10, pady=10)

        self.framePedido = ctk.CTkFrame(self)
        self.framePedido.pack(pady=20)

        self.labelQuantidadePedido = ctk.CTkLabel(self.framePedido, text='QUANTIDADE', font=('Arial', 14))
        self.labelQuantidadePedido.grid(row=0, column=0, padx=10, pady=10)

        self.labelSaborPedido = ctk.CTkLabel(self.framePedido, text='SABOR', font=('Arial', 14))
        self.labelSaborPedido.grid(row=0, column=1, padx=10, pady=10)

        self.labelTamanhoPedido = ctk.CTkLabel(self.framePedido, text='TAMANHO', font=('Arial', 14))
        self.labelTamanhoPedido.grid(row=0, column=2, padx=10, pady=10)

        self.labelPrecoPedido = ctk.CTkLabel(self.framePedido, text='PREÇO (R$)', font=('Arial', 14))
        self.labelPrecoPedido.grid(row=0, column=3, padx=10, pady=10)
        
        pedido = controller.getPedido()
        linha = 1
        total = 0

        for item in pedido.getItens():
            pizza = item.getPizza()
            sabor = pizza.getSabor()
            tamanho = pizza.getTamanho()
            preco = pizza.getPreco()
            quantidade = int(item.getQuantidade())
            
            ctk.CTkLabel(self.framePedido, text=f"{quantidade}", font=('Arial', 13)).grid(row=linha, column=0, padx=10, pady=5)
            ctk.CTkLabel(self.framePedido, text=f"{sabor}", font=('Arial', 13)).grid(row=linha, column=1, padx=10, pady=5)
            ctk.CTkLabel(self.framePedido, text=f"{tamanho}", font=('Arial', 13)).grid(row=linha, column=2, padx=10, pady=5)
            ctk.CTkLabel(self.framePedido, text=f"{preco:.2f}", font=('Arial', 13)).grid(row=linha, column=3, padx=10, pady=5)
            

            linha += 1
            total += pizza.getPreco() * quantidade

        self.labelTotalPedido = ctk.CTkLabel(self.framePedido, text='TOTAL:', font=('Arial', 14))
        self.labelTotalPedido.grid(row=linha, column=0, padx=10, pady=10)

        self.labelTotalPedidoRegistrado = ctk.CTkLabel(self.framePedido, text=f'R$ {total:.2f}', font=('Arial', 13))
        self.labelTotalPedidoRegistrado.grid(row=linha, column=1, padx=10, pady=10)

        self.frameBotao = ctk.CTkFrame(self)
        self.frameBotao.pack(pady=20)

        self.buttomFinalizarPedido = ctk.CTkButton(self.frameBotao, text='Finalizar Pedido', fg_color='green', hover_color='darkgreen', command=self.finalizarPedido)
        self.buttomFinalizarPedido.grid(row=0, column=0, padx=10, pady=10)

        self.buttomCancelarPedido = ctk.CTkButton(self.frameBotao, text='Cancelar Pedido', fg_color='#dd0000', hover_color='#b30000', command=self.cancelarPedido)
        self.buttomCancelarPedido.grid(row=0, column=1, padx=10, pady=10)

    def finalizarPedido(self):
        cliente = controller.getCliente()
        pedido = controller.getPedido()

        controller.cadastrarClienteBD(cliente)
        controller.cadastrarPedidoBD(pedido)
        controller.cadastrarItemPedidoBD(pedido)

        controller.limparDados()

        self.destroy()
        Menu()

    def cancelarPedido(self):
        controller.limparDados()
        
        self.destroy()
        Menu()


app = Login()
app.mainloop()
