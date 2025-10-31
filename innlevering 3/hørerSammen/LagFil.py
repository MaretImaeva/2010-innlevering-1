class Skuespiller:
    def __init__(self, id, navn):
        self.id = id
        self.navn = navn


class Film:
    def __init__(self, id, navn, value: int):
        self.film_id = id
        self.film_navn = navn
        self.vekt = value


actors = "actors.tsv"
movies = "movies.tsv"

#actors = "marvel_actors.tsv"
#movies = "marvel_movies.tsv"


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
        filmer = []
        for film in deler[2:]:
            filmer.append(film)
            if film in film_dict:
                film_dict[film][1].append(deler[0]) #legger til node IDen, men kan byttes ut med å legge til node objekt eller navn også

    
    for line in data:
        if line not in film_dict:
            print("Lagt til alene node")
            linjer.append((deler[0], None, None))

les_film()
les_skue()
print("Lest input filer")


for film in film_dict.values(): #for alle nøkler i film_dict
    for i in range(len(film[1])):
        for j in range(i +1, len(film[1])):
            a = film[1][i]
            b = film[1][j]
            vekt = film[0].vekt
            linjer.append((a, b, vekt))

class Fil:
    def __init__(self):
        # ...existing code...
        # Skriv linjer (a, b, weight) til en TSV-fil
        with open("edges.tsv", "w", encoding="utf-8") as f:
            for a, b, vekt in linjer:
                f.write(f"{a}\t{b}\t{vekt}\n")
        # ...existing code...
        print("Fil laget.")
