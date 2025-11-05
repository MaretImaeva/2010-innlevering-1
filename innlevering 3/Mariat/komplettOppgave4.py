from collections import defaultdict
from itertools import combinations
import heapq 
import csv
import itertools

counter = itertools.count()

movies = "movies.tsv"
actors = "actors.tsv"

alt_dict = defaultdict(list)


class Skuespiller:
    def __init__(self, id, navn):
        self.id = id
        self.navn = navn

class Film:
    def __init__(self, id, navn, value: int):
        self.film_id = id
        self.film_navn = navn
        self.vekt = value

film_dict = {} #nøkkelen er film IDen, verdien er et tuppel med film objektet og en liste av skuespillere i filmen

def les_film():
    fil = open(movies, 'r', encoding='utf-8')  
    data = fil
    for line in data:
        deler = [d.strip() for d in line.strip().split('\t')]
        if len(deler) < 3:
            print("Feil. Ikke riktig leset")
        noder = []  #skuespiller id-er     
        film_dict[deler[0]] = (Film(deler[0], deler[1], float(deler[2])), noder)

def les_skue():
    fil = open(actors, 'r', encoding='utf-8')  
    data = fil       
    for line in data:
        deler = [d.strip() for d in line.strip().split('\t')]
        if len(deler) < 3: #sjekker at det er splittet riktig
            continue
        node = Skuespiller(deler[0], deler[1])
        alt_dict[node] 
        filmer = []
        for film in deler[2:]:
            filmer.append(film)
            if film in film_dict:
                film_dict[film][1].append(node) #legger til noden, men kan byttes ut med å legge til node id eller navn også

    print("Lagret alle skuespillere, selv de ensomme")

    print("Laster...")

les_film()
les_skue()

for film_obj, actors in film_dict.values():
    #Fjerner ugyldige elementer
    actors = [a for a in actors if isinstance(a, Skuespiller)]
    for a, b in combinations(actors, 2):
        alt_dict[a].append((b, film_obj))
        alt_dict[b].append((a, film_obj))
    



def antall_noder():
    return "Antall noder:", len(alt_dict)

def antall_kanter():
    kanter = 0
    for val in alt_dict.values():
        for nabo, kant in val:
            kanter += 1
    return "Antall kanter:", kanter



def dijkstra_finn_korteste_sti(alt_dict, id1, id2):
    start = next((n for n in alt_dict if n.id == id1), None)
    mål = next((n for n in alt_dict if n.id == id2), None)
    if start is None or mål is None:
        print(f"En av nodene finnes ikke: {id1} eller {id2}")
        return None, []

    #startnode = finn_node(id1)
    #sluttnode = finn_node(id2)

    if (alt_dict[id1]) is None or (alt_dict[id2]) is None:
        print(f"En av nodene finnes ikke i grafen: {id1} eller {id2}")
        return None, []
    
    #startnode = startnode.navn #bytt til .id om man ønkser å søke med id
    #sluttnode = sluttnode.navn

    avstand = {node: float('inf') for node in alt_dict}
    avstand[start] = 0
    forelder = {node: None for node in alt_dict}

    pq = [(0, next(counter), start)]
    besøkt = set()

    while pq:
        nåværende_avstand, _, nåværende_node = heapq.heappop(pq)

        if nåværende_node in besøkt:
            continue
        besøkt.add(nåværende_node)

        if nåværende_node == mål:
            break  # Vi har funnet korteste vei

        #print(type(alt_dict[nåværende_node]), alt_dict[nåværende_node])
        for nabo, film_obj in alt_dict[nåværende_node]:
            vekt = 10-film_obj.vekt
            ny_avstand = nåværende_avstand + vekt
            if ny_avstand < avstand[nabo]:
                avstand[nabo] = ny_avstand
                forelder[nabo] = nåværende_node
                heapq.heappush(pq, (ny_avstand, next(counter), nabo))


    # Rekonstruer korteste sti
    sti = []
    node = mål
    while node is not None:
        sti.append(node)
        node = forelder[node]
    sti.reverse()

    if not sti:
        print(f"Ingen sti funnet mellom {start.navn} og {mål.navn}")
        return None, []

    total_weight = 0 

    print(f"Sti fra {start.navn} til {mål.navn}")
    for i in range(1, len(sti)):
        a, b = sti[i-1], sti[i]

        for nabo, film_obj in alt_dict[a]:
            if nabo == b:
                vekt = 10 - float(film_obj.vekt)  # vektfunksjonen fra oppgaven
                total_weight += vekt
                print(f"===[ {film_obj.film_navn} ({vekt}) ] ===>{b.navn}")
                break

    print("Total weight:", round(total_weight, 2))
    return avstand[mål], sti


#dijkstra_finn_korteste_sti(alt_dict, "Donald Glover","Jeremy Irons")
dijkstra_finn_korteste_sti(alt_dict, "nm2255973", "nm0000460")
