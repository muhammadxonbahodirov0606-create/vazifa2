class Hayvon:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi

    def ovoz(self):
        print("Hayvon ovoz chiqardi")

class It(Hayvon):
    def qoriqlash(self):
        print(self.nomi, "uyni qo'riqlaydi")

class Mushuk(Hayvon):
    def sichqon_tutish(self):
        print(self.nomi, "sichqon tutadi")

it = It("Bobik", 3)
mushuk = Mushuk("Mosh", 2)

it.ovoz()
it.qoriqlash()

mushuk.ovoz()
mushuk.sichqon_tutish()