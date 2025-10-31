from collections import defaultdict
#import graphviz


class Skuespiller:
    def __init__(self, id, navn):
        self.id = id
        self.navn = navn


class Film:
    def __init__(self, id, navn, value: int):
        self.film_id = id
        self.film_navn = navn
        self.vekt = value

a_filnavn = "marvel_actors.tsv"
m_filnavn = "marvel_movies.tsv"

# a_filnavn = "actors.tsv"
# m_filnavn = "movies.tsv"

film_dict = {}
actor_names = {} #kobler skuespiller-ID til navn

def les_film():
    with open(m_filnavn, "r", encoding = "utf-8") as fil:
        for line in fil:
            deler = line.split('\t')
            noder = []
            film_dict[deler[0]] = (Film(deler[0], deler[1], float(deler[2])), noder)
            #print(noder)

linjer = []

def les_skue():
    with open(a_filnavn, "r", encoding = "utf-8") as fil:
        for line in fil:
            deler = [d.strip() for d in line.strip().split('\t')]
            if len(deler) < 3: #sjekker at det er splittet riktig
                continue
            node = Skuespiller(deler[0], deler[1])
            actor_names[deler[0]] = deler[1]
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


for film, (film_obj, actors) in film_dict.items():
    if len(actors) == 1:
        print(actors[0],"er alene i filmen", film_obj.film_navn)
    
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



def DFS(G, s, visited): #med stack, også fra graf notat
    V, E, w = G
    # visited = set()  #den nullstiller visited, trengte DFSFull så neinei
    resultat = []
    stack = [s]

    while stack:
        u = stack.pop()
        if u not in visited:
            resultat.append(u)
            visited.add(u)
            for v in E[u]:
                stack.append(v)
    
    # print("Er", len(resultat), "riktig ant noder?")
    # mld = input("")
    # if mld.upper() == "NEI":
    #     print("Too bad ig")
    return resultat
    

def DFSFull(G):
    V, E, w = G
    visited = set()
    komponenter = []
    antall = 0
    for v in V:
        if v not in visited:
            komp=DFS(G,v,visited)
            komponenter.append(komp)
            antall += len(komponenter)
    # return komponenter,  antall
    print("Antall komponenter i grafen er ", len(komponenter))



def kompSize(G):
    V, E, w = G
    visited = set()
    size = []
    for v in V:
        if v not in visited:
            comp = DFS(G, v, visited)
            size.append(len(comp))
    return size
    
def skrivStørrelser(G):
    size = kompSize(G)
    freq = {}
    for i in size:
        freq[i] = freq.get(i,0)+1
        print(i)
        print("det er", freq[i], "antall grafer med ", i," noder")




graf = buildgraph(linjer)
DFSFull(graf)
skrivStørrelser(graf)

