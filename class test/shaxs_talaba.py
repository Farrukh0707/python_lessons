#MASHQLAR
class Shaxs:
    def __init__(self, ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ilgan."
        return info
        
    def get_age(self,yil):
        return yil - self.tyil

    
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
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
    
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


talaba1 = Talaba('Nizom', 'Nizomov', 'AD3334455', 1994, 'FA111222',"Manzil")         
fan1 = Fan("Matematika")
fan2 = Fan("Fizika")
fan3 = Fan("Ingliz tili")
fan4 = Fan("Kimyo")

talaba1.fanga_yozil(fan1.get_fan())
talaba1.fanga_yozil(fan2.get_fan())
talaba1.fanga_yozil(fan3.get_fan())

user1 = Foydalanuvchi("Nizom", "Nizomov", "Qamariddin o'g'li", "AD2223344", 1994, 941777777)

admin = Admin("Rajabov", "Oybek", "Adhamovich", "AA22223333", "1960", 901111111, user1)
# print(admin.ban_user(user1.get_info()))




    
    
    
    
    
    
    
    
    
    
    