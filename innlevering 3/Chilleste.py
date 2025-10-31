from buildGrafFinal import Graf
import csv
#Oppgave 4

import heapq

def les_tsv(filnavn):
    with open(filnavn, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        data = [(rad[0], rad[1], rad[2]) for rad in reader if len(rad) >= 3]
    return data

kanter = les_tsv("edges.tsv")

G = Graf(kanter)

def dijkstra_finn_korteste_sti(graf, id1, id2):
    
    noder = graf.hentV()
    edges = graf.hentE()
    w = graf.hentW()

    startnode = graf.finn_node(id1)
    sluttnode = graf.finn_node(id2)

    avstand = {node: float('inf') for node in noder} #gir inf verdi til alle noder
    avstand[startnode] = 0
    forelder = {node: None for node in noder}

    pq = []
    heapq.heappush(pq, (0, startnode))
    besøkt = set()

    while pq:
        nåværende_avstand, nåværende_node = heapq.heappop(pq)

        if nåværende_node in besøkt:
            continue
        besøkt.add(nåværende_node)

        if nåværende_node == sluttnode:
            break  # Vi har funnet korteste vei


        
        for nabo, vekt in graf.hent_naboer(nåværende_node[0]):
            ny_avstand = nåværende_avstand + vekt
            if ny_avstand > avstand[nabo]:
                avstand[nabo] = ny_avstand
                forelder[nabo] = nåværende_node
                heapq.heappush(pq, (ny_avstand, nabo))

    # Rekonstruer korteste sti
    sti = []
    node = sluttnode
    while node is not None:
        sti.append(node)
        node = forelder[node]
    sti.reverse()

    for i in range(1, len(sti)):
        a, b = sti[i-1], sti[i]
        film = kanter.get((a, b))
        if film:
            print(f"===[ {film.film_navn} ({film.vekt}) ] ===> {b}") #lånte fra Samiras kode
        else:
            print(f"===[ ? ] ===> {b}")

    return avstand[sluttnode], sti


dijkstra_finn_korteste_sti(G, "nm2255973","nm0000460")
