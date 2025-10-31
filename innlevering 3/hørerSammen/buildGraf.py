from collections import defaultdict
import csv
from LagFil import Fil

fil = Fil()

def les_tsv(filnavn):
    with open(filnavn, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        data = [(rad[0], rad[1], rad[2]) for rad in reader if len(rad) >= 3]
    return data


class Graf:
    def __init__(self, lines):
        self.V = set() #set av noder
        self.E = defaultdict(set) #kanter
        self.w = dict() #vektfunksjon
        self.naboer = defaultdict(list)

        for line in lines:
            #print(line)
            deler = []
            for item in line:
                deler.append(item)
            u, v, weight = deler[0], deler[1], deler[2]

            self.V.add(u)
            self.V.add(v)

            self.E[u].add(v)
            self.E[v].add(u)
            self.naboer[deler[0]].append((deler[1], float(weight)))
            self.naboer[deler[1]].append((deler[0], float(weight)))

            if None in line:
                continue

            self.w[(u, v)] = float(weight)
            self.w[(v, u)] = float(weight)

    

    def finn_node(self, node_id): 
        if node_id not in self.V:
            return
        for node in self.V: #om noder legges inn som objekter, endre node til node.id
            if node == node_id:
                return node
            
    def hentV(self):
        return self.V
    
    def hentE(self):
        return self.E
    
    def hentW(self):
        return self.w
    
    def hent_naboer(self, node_id):
        return self.naboer[node_id]
    
kanter = les_tsv("edges.tsv")

G = Graf(kanter)

def ant_kanter():
    return len(kanter)

def hent_noder(G):
    return G.hentV()

print("Noder: ", len(hent_noder(G)),"\nKanter: ", ant_kanter())
