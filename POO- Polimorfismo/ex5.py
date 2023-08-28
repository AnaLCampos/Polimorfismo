class transportepublico:
    def pegarpassageiro(self):
        pass

    def largarpassageiro(self):
        pass

class onibus(transportepublico):
    def pegarpassageiro(self):
        print("Ônibus: Passageiro embarcando.")

    def largarpassageiro(self):
        print("Ônibus: Passageiro desembarcando.")

class Metro(transportepublico):
    def pegarpassageiro(self):
        print("Metrô: Passageiro entrando na estação.")

    def largarpassageiro(self):
        print("Metrô: Passageiro saindo na próxima estação.")

onibus = o nibus()
onibus.pegarpassageiro()
onibus.largarpassageiro()

metro = Metro()
metro.pegarpassageiro()
metro.largarpassageiro()