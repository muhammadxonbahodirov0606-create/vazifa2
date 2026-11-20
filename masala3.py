class Transport:
    def harakatlanish (self):
        print("Transport harakatlanmoqda")

class Mashina(Transport):
    def harakatlanish(self):
        print ("Mashina yurmoqda")

class velosiped (Transport):
    def harakatlanish(self):
        print ("velosiped yurmoqda")

class poyezd (Transport):
    def harakatlanish(self):
        print ("poyezd signal chalmoqda")

Transportlar= [Mashina(), velosiped(), poyezd()]

for transport in Transportlar:
    transport.harakatlanish()