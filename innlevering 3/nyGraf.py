from collections import defaultdict
import graphviz


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

film_dict = {}

def les_film():
    with open(m_filnavn, "r") as fil:
        for line in fil:
            deler = line.split('\t')
            noder = []
            film_dict[deler[0]] = (Film(deler[0], deler[1], float(deler[2])), noder)
            #print(noder)


linjer = []


def les_skue():
    with open(a_filnavn, "r") as fil:
        for line in fil:
            deler = line.split('\t') #for å splitte korrekt
            node = Skuespiller(deler[0], deler[1])
            filmer = deler[2:]
            for film in filmer: #for hver film knyttet til skuespilleren
                if film in film_dict: #sjekkes det om denne eksisterer som kant
                    film_dict[film][1].append(node) #referer til noder listen inne i Film objektet
                    
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


def buildgraph(lines):
    V = set() #set av noder
    E = defaultdict(set) #kanter
    w = dict() #vektfunksjon

    for line in lines:
        print(line)
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

    return V, E, w


                
def hent_kant():
    return int(len(m_filnavn))

def hent_act():
    return int(len(a_filnavn))


G = buildgraph(linjer)

print()
print()
print("Alt kjørt suksessfult, yay :)")
print()
