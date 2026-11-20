class Kitob:
    def __init__(self, nom, muallif, sahifa_soni):
        self.nom = nom
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def malumot(self):
        print("Nomi:", self.nom)
        print("Muallif:", self.muallif)
        print("Sahifalar:", self.sahifa_soni)


class ElektronKitob(Kitob):
    def __init__(self, nom, muallif, sahifa_soni, format, fayl_hajmi):
        super().__init__(nom, muallif, sahifa_soni)
        self.format = format
        self.fayl_hajmi = fayl_hajmi

    def malumot(self):
        super().malumot()
        print("Format:", self.format)
        print("Fayl hajmi:", self.fayl_hajmi)


kitob = Kitob("Python", "Aliyev", 150)
elektron = ElektronKitob("Python", "Aliyev", 150, "PDF", "5 MB")

kitob.malumot()
print("--------------")
elektron.malumot()