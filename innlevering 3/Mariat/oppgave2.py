from graf100 import alt_dict

def DFS(G, s, visited):  # beholder signaturen, ignorerer G
    resultat = []
    stack = [s]

    while stack:
        u = stack.pop()
        if u not in visited:
            resultat.append(u)
            visited.add(u)
            # naboer ligger i alt_dict[u]["kant"] som (nabo_id, tittel, filmID, vekt)
            for v, film_tittel, film_id, rating in alt_dict.get(u, {}).get("kant", []):
                if v not in visited:
                    stack.append(v)
    return resultat

# Finner størrelsen på komponentene
def kompSize(G):  # beholder signaturen, ignorerer G
    visited = set()
    size = []

    # bygg V fra nøkler + naboer i alt_dict
    V = set(alt_dict.keys())
    for entry in alt_dict.values():
        for v_id, film_tittel, film_id, rating in entry.get("kant", []):
            V.add(v_id)

    for v in V:
        if v not in visited:
            comp = DFS(G, v, visited)
            size.append(len(comp))
    return size

def skrivStørrelser(G):  # beholder signaturen, ignorerer G
    size = kompSize(G)
    freq = {}
    for i in size:
        freq[i] = freq.get(i, 0) + 1
    for i in freq:
        print("There are", freq[i], "components of size", i)

# kall med en dummy (G brukes ikke lenger)
skrivStørrelser(None)
