from Graf1000 import film_dict
from collections import deque, defaultdict  

# Bygg navn-oppslag, kanter og nabokart (E) i én passering
actor_names = {}
film_edges = defaultdict(list)   
E = defaultdict(set)             

for x, (film_obj, actors) in film_dict.items():
    ids = []
    for a in actors:
        a_id = getattr(a, "id", a)    #brukter getattr for å hente attributer fra objekter, her henter den ut id til objektet
        a_navn = getattr(a, "navn", None) #henter ut navnet her
        if a_navn:
            actor_names[a_id] = a_navn
        ids.append(a_id)

    n = len(ids)
    for i in range(n - 1):
        for j in range(i + 1, n):
            a, b = ids[i], ids[j]
            film_edges[(a, b)].append(film_obj)  
            film_edges[(b, a)].append(film_obj)  
            E[a].add(b)                          
            E[b].add(a)                          

def finn_sti(start, mål):
    if start not in E or mål not in E:
        print(f"Ingen sti funnet mellom {actor_names.get(start, start)} og {actor_names.get(mål, mål)}")
        return

    queue = deque([start])
    visited = {start}
    forelder = {start: None}

    while queue:
        u = queue.popleft()
        if u == mål:
            break
        for v in E.get(u, ()):
            if v not in visited:
                visited.add(v)
                forelder[v] = u
                queue.append(v)

    if mål not in forelder:
        print(f"Ingen sti funnet mellom {actor_names.get(start, start)} og {actor_names.get(mål, mål)}")
        return

    # Rekonstruer stien
    sti = []
    node = mål
    while node is not None:
        sti.append(node)
        node = forelder[node]
    sti.reverse()

    # Skriv ut med navn og film mellom hvert steg
    def navn(a_id): return actor_names.get(a_id, a_id)

    print(f"Sti fra {navn(start)} til {navn(mål)}")
    print(navn(sti[0]), end="")
    for i in range(1, len(sti)):
        a, b = sti[i - 1], sti[i]
        filmer = film_edges.get((a, b), [])
        if filmer:
            film = filmer[0]
            print(f" ===[ {film.film_navn} ({film.vekt}) ]==> {navn(b)}", end="")
        else:
            print(f" ===[ ? ]==> {navn(b)}", end="")
    print("\n")



finn_sti("nm2255973", "nm0000460")
finn_sti("nm0424060", "nm8076281")
finn_sti("nm4689420","nm0000365")
finn_sti("nm0000288","nm2143282")
finn_sti("nm0637259", "nm0931324")
