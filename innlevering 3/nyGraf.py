from collections import defaultdict
import csv


class Skuespiller:
    def __init__(self, id, navn):
        self.id = id
        self.navn = navn


class Film:
    def __init__(self, id, navn, value: int):
        self.film_id = id
        self.film_navn = navn
        self.vekt = value


actors = "marvel_actors.tsv"
movies = "marvel_movies.tsv"

film_dict = {}

def les_film():
    fil = open(movies, 'r', encoding='utf-8')  
    data = fil
    for line in data:
        deler = [d.strip() for d in line.strip().split('\t')]
        if len(deler) < 3:
            print("Feil. Ikke riktig leset")
        noder = []
        film_dict[deler[0]] = (Film(deler[0], deler[1], float(deler[2])), noder)
        #print(noder)

linjer = []

def les_skue():
    fil = open(actors, 'r', encoding='utf-8')  
    data = fil       
    for line in data:
        deler = [d.strip() for d in line.strip().split('\t')]
        if len(deler) < 3: #sjekker at det er splittet riktig
            continue
        node = Skuespiller(deler[0], deler[1])
        for film in deler[2:]:
            if film in film_dict:
                film_dict[film][1].append(deler[0]) #legger til node IDen, men kan byttes ut med å legge til node objekt eller navn også
    print("Kjørt")

les_film()
les_skue()

for film in film_dict.values(): #for alle nøkler i film_dict
    for i in range(len(film[1])):
        for j in range(i +1, len(film[1])):
            a = film[1][i]
            b = film[1][j]
            vekt = film[0].vekt
            linjer.append((a, b, vekt))


def buildgraph(lines): #tatt fra notat om Utvalgte grafalgoritmer, av Lars Tveito
    V = set() #set av noder
    E = defaultdict(set) #kanter
    w = dict() #vektfunksjon

    for line in lines:
        #print(line)
        deler = []
        for item in line:
            deler.append(item)
        u, v, weight = deler[0], deler[1], deler[2]

        V.add(u)
        V.add(v)

        E[u].add(v)
        E[v].add(u)

        w[(u, v)] = int(weight)
        w[(v, u)] = int(weight)

    
        for film in film_dict.values(): #også legge med naboløse noder
            for actor in film[1]:
                V.add(actor)
                if actor not in E:
                    E[actor] = set()

    return V, E, w

G = buildgraph(linjer)

def ant_kanter():
    return len(linjer)

def hent_noder(G):
    noder, kanter, vekt = G
    return noder

print("Noder: ", len(hent_noder(G)),"\nKanter: ", ant_kanter())



def DFS(G, s): #med stack, også fra graf notat
    V, E, w = G
    besøkt = set()
    resultat = []
    stack = [s]

    while stack:
        u = stack.pop()
        if u not in besøkt:
            resultat.append(u)
            besøkt.add(u)
            for v in E[u]:
                stack.append(v)

    return resultat

DFS(G, linjer[0][0])
