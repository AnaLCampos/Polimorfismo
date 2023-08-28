class item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class produto(item):
    def calcularvalor(self):
        return self.preco

class servico(item):
    def calcularvalor(self):
        pass

produto = produto("Notebook", 1200.00)
servico = servico("Manutenção", 50.00)

print(produto.nome, " - Valor:", produto.calcularvalor())
print(servico.nome, " - Valor:", servico.calcularvalor())
