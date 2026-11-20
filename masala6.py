class Inson:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

class Talaba(Inson):
    def __init__(self, ism, yosh, universitet, baho):
        super().__init__(ism, yosh)
        self.universitet = universitet
        self.baho = baho

    def natija(self):
        if self.baho >= 86:
            print("A'lo")
        elif self.baho >= 71:
            print("Yaxshi")
        elif self.baho >= 56:
            print("Qoniqarli")
        else:
            print("Qoniqarsiz")

talaba = Talaba("Ali", 20, "TATU", 90)
talaba.natija()