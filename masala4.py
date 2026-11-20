class Shakl:
    def yuza(self):
        pass

class Kvadrat(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2

class TogriTortburchak(Shakl):
    def __init__(self, uzunlik, en):
        self.uzunlik = uzunlik
        self.en = en

    def yuza(self):
        return self.uzunlik * self.en

shakllar = [Kvadrat(5), TogriTortburchak(4, 6)]

for shakl in shakllar:
    print(shakl.yuza())