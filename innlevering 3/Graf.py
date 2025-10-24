a_filnavn = input("Skuespillere: ")
m_filnavn = input("Filmer: ")
print("\n")


class Node:
    def __init__(self, id, navn):
        self.id = id
        self.navn = navn
        self.naboer = []

class Skuespiller(Node):
    def __init__(self, id, navn, filmer: list):
        super().__init__(id, navn)
        self.filmer = filmer

class Film(Node):
    def __init__(self, id, navn, rating):
        super().__init__(id, navn)
        self.rating = rating

class Kant:
    def __init__(self, node1, node2):
        self.verdi = 1
        self.node1 = node1
        self.node2 = node2

class Graf:
    def __init__(self):
        self.noder = []
        self.kanter = []

    def addNode(self, node):
        if node not in self.noder:
            self.noder.append(node)
        else:
            return
    
    def addKant(self,node1, node2):
        kant = Kant(node1, node2)
        self.kanter.append(kant)
        node1.naboer.append(node2)
        node2.naboer.append(node1)

    def ant_noder(self):
        return len(self.noder)
    
    def ant_kanter(self):
        return len(self.kanter)
    
    def finn_node(self, id):
        for node in self.noder:
            if node.id == id:
                return node
        return None


graf = Graf()

with open(m_filnavn, "r") as fil:
    for line in fil:
        deler = line.split()
        film = Film(deler[0], deler[1], deler[2])
        graf.addNode(film)


with open(a_filnavn, "r") as fil:
    for line in fil:
        deler = line.split()
        skue = Skuespiller(deler[0], deler[1], deler[2:])
        graf.addNode(skue)
        gyld_filmer = []
        for film in skue.filmer:
            film_obj = graf.finn_node(film)
            if film_obj:
                gyld_filmer.append(film)
                graf.addKant(skue, film_obj)
        skue.naboer = gyld_filmer
        
    

print("Oppave 1\n\nNodes:", graf.ant_noder())
print("Edges", graf.ant_kanter())

