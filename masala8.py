class FilmKutubxonasi:
    def __init__(self, nom, filmlar=None):
        self.nom = nom
        self.filmlar = filmlar if filmlar is not None else []

    def __len__(self):
        return len(self.filmlar)

    def __getitem__(self, indeks):
        return self.filmlar[indeks]

    def __contains__(self, film):
        return film in self.filmlar


kutubxona = FilmKutubxonasi("Kinolar", ["Avatar", "Titanik", "Temir odam"])

print(len(kutubxona))
print(kutubxona[0])
print("Avatar" in kutubxona)
print("Batman" in kutubxona)