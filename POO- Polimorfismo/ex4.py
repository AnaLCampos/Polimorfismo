class contabancaria:
    def calcularjuros(self):
        pass

class contapoupanca(contabancaria):
    def calcularjuros(self, saldo):
        return saldo * 0.05

class contacorrente(contabancaria):
    def calcularjuros(self, saldo):
        return saldo * 0.02


contapoupanca = contapoupanca()
saldopoupanca = 1000
jurospoupanca = contapoupanca.calcularjuros(saldopoupanca)
print(f"Juros da Conta Poupança: R${jurospoupanca:.2f}")

contacorrente = contacorrente()
saldocorrente = 1500
juroscorrente = contacorrente.calcularjuros(saldocorrente)
print(f"Juros da Conta Corrente: R${juroscorrente:.2f}")