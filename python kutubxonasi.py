# import datetime as dt
# from datetime import timedelta


#1
# hozir = dt.date.today()
# vaqtkeyin = hozir + timedelta(14)

# for n in range(1,11):
#     vaqtkeyin += timedelta(1)
#     print(vaqtkeyin)


#2
# ramazon_hayiti = dt.date(2024,4,10)
# print(f"Ramazon hayitiga {(ramazon_hayiti-hozir).days} kun qoldi.")

# qurbon_hayiti = dt.date(2024,6,16)
# print(f"Qurbon hayitiga {(qurbon_hayiti-hozir).days} kun qoldi.")


#3
# hozir = dt.date.today()
# tugilgan_kun = dt.date(1996,8,6)
# farq_yil = hozir.year - tugilgan_kun.year
# farq_oy = hozir.month - tugilgan_kun.month
# farq_kun = hozir.day - tugilgan_kun.day

# print(f"Sizni tug'ilganizga {farq_yil} yil {farq_oy} oy {farq_kun} kun bo'ldi.")


#4
# andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
# msg = "Telefon raqamingizni kiriting: "

# while True:
#     tel_raqam = input(msg)
#     if re.match(andoza,tel_raqam):
#         print("Telefon raqam to'g'ri kiritildi.")
#         break
#     else:
#         print("Telefon raqam noto'g'ri kiritildi.")


#5
import re
matn = """Assalom alaykum hurmatli do'stlar. 
          Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI.
          Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar
          va metodlarini tekshiruvchi dastur yozishni o'rganamiz. 
          Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

andoza1 = "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
manzil = re.findall(andoza1,matn)
print(manzil)






