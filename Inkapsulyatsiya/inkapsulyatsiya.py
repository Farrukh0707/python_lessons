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
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil,raqam="Berilmagan"):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        self.__raqam = uuid4()
        Talaba.talabalar_soni += 1
    
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
    
    
class Fan():
    def __init__(self,fan):
        self.fan = fan
        
    def get_fan(self):
        return self.fan
    
    def del_fan(self):
        return self.fan

class Foydalanuvchi(Shaxs):
    def __init__(self,ism,familiya,sharif,passport,tyil,tel):
        super().__init__(ism, familiya, passport, tyil)
        self.sharif = sharif
        self.tel = tel
    
    def get_sharif(self):
        return self.sharif
    
    def get_tel(self):
        return self.tel
    
    def get_info(self):
        info = f"{self.ism} {self.familiya} {self.sharif}. "
        info += f"{self.tyil}-yilda tug'ilgan. ID raqami: {self.passport}. Telefon raqam: {self.tel}"
        return info


class Admin(Foydalanuvchi):
    def __init__(self,ism,familiya,sharif,passport,tyil,tel, user):
        super().__init__(ism, familiya, sharif, passport, tyil, tel)
        self.user = user
    
    def ban_user(self, user):
        return "Foydalanuvchi bloklandi."



# shaxs = Shaxs("Adham", "Qorjovov", "AD8888777", 1993, "Erkak")
# print(shaxs.get_odamlar_soni())

talaba = Talaba("Farrux", "Ashurov", "AA1111222", 1996, "AD123456", "Qashqadaryo viloyati")
print(talaba.get_talaba_soni())   
    
    

    
    