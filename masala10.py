class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

class Savat:
    def __init__(self, nom):
        self.nom = nom
        self.mahsulotlar = []

    def __len__(self):
        return len(self.mahsulotlar)

    def __bool__(self):
        return len(self.mahsulotlar) > 0

    def umumiy_narx(self):
        return sum(x.narx for x in self.mahsulotlar)

    def __str__(self):
        return f"{self.nom} — {len(self.mahsulotlar)} ta mahsulot"

savat = Savat("Mening savatim")
savat.mahsulotlar = [
    Mahsulot("Telefon", 3000000),
    Mahsulot("Noutbuk", 5000000),
    Mahsulot("Sichqoncha", 100000)
]

print(savat)

if savat:
    print("Savat bo'sh emas")
    print("Umumiy narx:", savat.umumiy_narx())
else:
    print("Savat bo'sh")