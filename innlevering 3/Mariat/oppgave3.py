from graf1000 import alt_dict, film_dict

film_edges = {}
for film_id, (film_obj, actors) in film_dict.items():
    for i in range(len(actors)):
        for j in range(i + 1, len(actors)):
            a = getattr(actors[i], "id", actors[i])  
            b = getattr(actors[j], "id", actors[j])  
            film_edges.setdefault((a, b), []).append(film_obj)  
            film_edges.setdefault((b, a), []).append(film_obj)  

actor_names = {}
for navn, (navn, actors) in film_dict.items():  
    for a in actors:  
        a_id = getattr(a, "id", a)  
        a_navn = getattr(a, "navn", None)  
        if a_navn:  
            actor_names[a_id] = a_navn  

#Korte veien mellom to skuespillere
from collections import deque
def BFSVisit(G, start, visited):
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)

    while len(queue) > 0:
        u = queue.popleft()
        for v in G[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
def BFSFull(G):
    visited = set()
    for v in G:
        if v not in visited:
            BFSVisit(G, v, visited)
#BFS for å finne korteste vei
def finn_sti(start, mål):
    # V, E, w = G.hentV(), G.hentE(), G.hentW()
    V = set(alt_dict.keys())
    E = {u: set() for u in V}

    for (a, b) in film_edges.keys():  
        if a in E and b in E:         
            E[a].add(b)               
            E[b].add(a)   



    queue = deque([start])
    visited = set([start])
    forelder = {start: None}

    while queue:
        u = queue.popleft()
        if u == mål:
            break
        for v in E.get(u, []):
            if v not in visited:
                visited.add(v)
                forelder[v] = u
                queue.append(v)
        
    if mål not in forelder:
        print(f"Ingen sti funnet mellom {actor_names.get(start, start)} og {actor_names.get(mål, mål)}")  
        return

    #Lager stien  
    sti = []
    node = mål
    while node is not None:
        sti.append(node)
        node = forelder[node]
    sti.reverse()

    print(f"Sti fra {actor_names.get(start, start)} til {actor_names.get(mål, mål)}")  
    print(actor_names.get(sti[0], sti[0]), end="")  
    for i in range(1, len(sti)):
        a, b = sti[i-1], sti[i]
        filmer = film_edges.get((a, b), [])

        if filmer:
            film = filmer[0]
            print(f" ===[ {film.film_navn} ({film.vekt}) ]==> {actor_names.get(b, b)}", end="")  
        else:
            print(f" ===[ ? ]==> {actor_names.get(b, b)}", end="")  
    print("\n")


# finn_sti("nm0000375", "nm0424060")
# finn_sti("nm0001765", "nm0000375")



finn_sti("nm2255973", "nm0000460")
finn_sti("nm0424060", "nm8076281")
finn_sti("nm4689420","nm0000365")
finn_sti("nm0000288","nm2143282")
finn_sti("nm0637259", "nm0931324")
