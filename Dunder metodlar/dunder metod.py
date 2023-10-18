#MASHQLAR
from uuid import uuid4

class Shaxs:
    __odamlar_soni = 0
    def __init__(self, ism,familiya,passport,tyil,jinsi="Noma'lum"):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__jinsi = jinsi
        Shaxs.__odamlar_soni += 1
        
    def __repr__(self):
        return f"{self.ism} {self.familiya}ning shaxsiy ma'lumotlari."
    
    def __lt__(self,y):
        return self.tyil < y.tyil
    
    def __eq__(self,y):
        return self.tyil == y.tyil
    
    @classmethod
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        return yil - self.tyil

    def get_jins(self):
        return self.__jinsi
    
class Manzil:
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
      

class Talaba(Shaxs):
    talabalar_soni = 0
    def __init__(self,ism,familiya,passport,tyil,idraqam,bosqich,manzil,raqam="Berilmagan"):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = bosqich
        self.manzil = manzil
        self.fanlar = []
        self.__raqam = uuid4()
        Talaba.talabalar_soni += 1
    
    
    def __repr__(self):
        return f"{self.ism} {self.familiya}"
    
    def __lt__(self,y):
        return self.bosqich < y.bosqich
    
    def __eq__(self,y):
        return self.bosqich == y.bosqich
    
    @classmethod
    def get_talaba_soni(cls):
        return cls.talabalar_soni
    
    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

    def fanga_yozil(self,fan):
        return self.fanlar.append(fan)
    
    def remove_fan(self,fan):
        if fan in self.fanlar:
            return self.fanlar.remove(fan)
        else:
            return f"Siz {fan} faniga yozilmagansiz."
        
    def get_raqam(self):
        return f"Talabaning maxfiy raqami: {self.__raqam}."
    
    
class Fan:
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar = []
        
    def __repr__(self):
        return f"{self.nomi} faniga yozilgan talabalar ro'yxati:\n{self.talabalar}"
    
    def get_fan(self):
        return self.nomi
    
    def add_talaba(self, *qiymat):
        for talaba in qiymat:
            if isinstance(talaba, Talaba):
                self.talabalar.append(talaba)
            else:
                print("Talaba obyektini kiriting.")

    def __getitem__(self,index):
        return self.talabalar[index]

    def __setitem__(self,index,value):
        if isinstance(value, Talaba):
            self.talabalar[index] = value

    def __len__(self):
        return len(self.talabalar)
    
    def __add__(self,qiymat):
        if isinstance(qiymat, Fan):
            return self.talabalar + qiymat.talabalar
    
    def __call__(self,*qiymat):
        if qiymat:
            for talaba in qiymat:
                self.add_talaba(talaba)
        else:
            return [talaba for talaba in self.talabalar]

    
# shaxs1 = Shaxs("Adham", "Qorjovov", "AD8888777", 1993, "Erkak")
# shaxs2 = Shaxs("Ural", "Qurbonov", "AD2222333", 1991, "Erkak")

fan1 = Fan("Matematika")
fan2 = Fan("Matematika")

talaba1 = Talaba("Farrux", "Ashurov", "AA1111222", 1996, "AD123456", 4, "Qashqadaryo viloyati")
talaba2 = Talaba("Sodiq", "Nishonov", "AA1234567", 1991, "AC654321", 2, "Toshkent viloyati")
talaba3 = Talaba("Jamshid", "Otaniyozov", "AB3333222", 1996, "AD444444", 3, "Buxoro viloyati")
# print(talaba1<talaba2)

fan1.add_talaba(talaba1,talaba2)
fan2.add_talaba(talaba3)
# print(fan1+fan2)

fan1(talaba3)
print(fan1())

    

    
    