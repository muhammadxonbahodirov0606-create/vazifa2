class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

class Oqituvchi(Xodim):
    def __init__(self, ism, maosh, fan):
        super().__init__(ism, maosh)
        self.fan = fan

    def malumot(self):
        print("Ism:", self.ism)
        print("Maosh:", self.maosh)
        print("Fan:", self.fan)

class Farrosh(Xodim):
    def __init__(self, ism, maosh, qavat):
        super().__init__(ism, maosh)
        self.qavat = qavat

    def malumot(self):
        print("Ism:", self.ism)
        print("Maosh:", self.maosh)
        print("Qavat:", self.qavat)

oqituvchi = Oqituvchi("Abdulborit", 3000000, "Matematika")
farrosh = Farrosh("Abdulbosit", 2000000, 2)

oqituvchi.malumot()
farrosh.malumot()