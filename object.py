#Mashqlar
class Avto:
    def __init__(self, model, rang, korobka, narh):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = 0
        
    def set_km(self, kilometr):
        self.kilometr = kilometr
    
    def update_km(self, km):
        self.kilometr += km
        
    def get_info(self):
        return f"{self.rang} {self.model}. {self.korobka}. Narxi: {self.narh}. Yurgan masofasi, km: {self.kilometr}."
                 


class Avtosalon():
    def __init__(self, nomi):
        self.nomi = nomi
        self.sotuvdagi_avtomobillar = []
        
    
    def add_avtomobil(self, avtomobil):
        self.sotuvdagi_avtomobillar.append(avtomobil)
    
    def get_avtomobil(self):
        return [x.get_info() for x in self.sotuvdagi_avtomobillar]

avtomobillar = Avtosalon("Qarshi_avtosalon")
avto1 = Avto("Malibu-2", "Qora", "Avtomat", 35000)
avto2 = Avto("Captiva-4", "Oq", "Avtomat", 30000)
avto3 = Avto("Toyota Camry", "Qora", "Avtomat", 48000)
avto4 = Avto("BMW X7", "Qora", "Avtomat", 150000)
avto5 = Avto("Mercedes-Benz EQS450", "Qora", "Avtomat", 180000)

avtomobillar.add_avtomobil(avto1)
avtomobillar.add_avtomobil(avto2)
avtomobillar.add_avtomobil(avto3)
avtomobillar.add_avtomobil(avto4)
avtomobillar.add_avtomobil(avto5)

# print(avtomobillar.get_avtomobil())

# print(avto1.__dict__)
# print(avto1.__dict__.keys())

def metodlar(klass):
    return [metod for metod in dir(klass) if metod.startswith('__') is False]

print(metodlar(Avto))






