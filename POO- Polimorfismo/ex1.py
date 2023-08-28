class animalaquatico:
    def nadando(self):
        pass

class peixe(animalaquatico):
    def nadando(self):
        return "O peixe está nadando."

class tartaruga(animalaquatico):
    def nadando(self):
        return "A tartaruga está nadando."

# Criando objetos
peixe = peixe()
tartaruga = tartaruga()

animaisaquaticos = [peixe, tartaruga]

for animal in animaisaquaticos:
    print(animal.nadando())
