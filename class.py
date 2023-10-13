#mashq
class User:
    def __init__(self, ism, familiya, email, telefon):
        self.ism = ism
        self.familiya = familiya
        self.email = email
        self.telefon = telefon
        
    def get_name(self):
        return self.ism
    
    def get_surname(self):
        return self.surname
    
    def get_email(self):
        return self.email
    
    def get_phoneNumber(self):
        return self.telefon
        
user1 = User("Anvar", "Narzullayev", "anvar1980@mail.ru", "90-909-10-10")
user2 = User("Farrux", "Ashurov", "ashurovfarrux1996@gmail.com", "90-638-11-11")

print(user1.ism)
print(user2.familiya)
print(user2.get_email())
print(user1.get_phoneNumber())









