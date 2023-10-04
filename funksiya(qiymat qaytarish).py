#1-mashq
# def shaxs_info (ism, familiya, tugilgan_yil, yosh, tugilgan_joy, email='', telefon=''):
#     info = {
#         'ism': ism,
#         'familiya': familiya,
#         'tugilgan_yil': tugilgan_yil,
#         'tugilgan_joy': tugilgan_joy,
#         'yosh': 2023 - tugilgan_yil,
#         'email': email,
#         'telefon': telefon
#         }
#     return info

# shaxs = shaxs_info(input('Ismingiz: ').title(), input('Familiyangiz: ').title(), int(input("Tug'ilgan yilingiz: ")), 'yosh', input("Tug'ilgan joyingiz: "))
# print(shaxs)


#2-mashq
# def mijoz_info (ism, familiya, tugilgan_yil, yosh, tugilgan_joy, email = "", telefon = None):
#     mijoz = {
#         'ism': ism,
#         'familiya': familiya,
#         'tugilgan_yil': tugilgan_yil,
#         'tugilgan_joy': tugilgan_joy,
#         'yosh': 2023 - tugilgan_yil,
#         'email': email,
#         'telefon': telefon
#         }
#     return mijoz

# print('Mijozlar ro\'yxati: ')
# mijozlar = []
# while True:
#     print("Quyidagi ma'lumotlarni kiriting: ")
#     ism = input('Ism: ').title()
#     familiya = input('Familiya: ').title()
#     tugilgan_yil = int(input("Tug'ilgan yil: "))
#     yosh = 2023 - tugilgan_yil
#     tugilgan_joy = input("Tug'ilgan joy: ")
#     email = input('Email: ')
#     telefon = input('Telefon raqam: ')
    
#     mijozlar.append(mijoz_info (ism, familiya, tugilgan_yil, yosh, tugilgan_joy, email, telefon))
    
#     javob = input("Yana mijoz qo'shasizmi ? (ha/yo'q) ")
#     if javob == "yo'q":
#         break
    
# for mijoz in mijozlar:
#     print(f"{mijoz['familiya']} {mijoz['ism']} {mijoz['tugilgan_yil']}-yil {mijoz['tugilgan_joy']}da tug'ilgan. {mijoz['yosh']} yoshda. Email: {mijoz['email']}. Telefon raqam: {mijoz['telefon']}.")

    
#3-mashq
# def max_son (x, y, z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return max

# katta_son = max_son(int(input('1-sonni kiriting: ')), int(input('2-sonni kiriting: ')), int(input('3-sonni kiriting: ')))
# print(f"Kiritilgan sonlarning eng kattasi - {katta_son}")    
    
    
#4-mashq
# def aylana_hisobla(radius, diametr='', perimetr='', yuzi=''):
#     aylana = {
#         'radius': radius,
#         'diametr': 2 * radius,
#         'perimetr': 2 * 3.14 * radius,
#         'yuzi': 3.14 * radius**2
#         }    
#     return aylana
    
# aylana_info = aylana_hisobla(int(input('Aylana radiusini kiriting: ')))
# print(aylana_info)
        

#5-mashq
# def tub_son_hisobla(min, max):
#     tub_sonlar = []
#     for son in range(min, max + 1):
#         tub = True
#         if son == 1:
#             tub = False
#         elif son == 2:
#             tub = True
#         else:
#             for x in range(2, son):
#                 if son % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(son)
        
#     return tub_sonlar      
# print(tub_son_hisobla(56, 100))


#6-mashq
# def fibonachchi(son):
#     fibonachchi_royxati = []
#     for x in range(son):
#         if x == 0 or x == 1:
#             fibonachchi_royxati.append(1)
#         else:
#             fibonachchi_royxati.append(fibonachchi_royxati[x - 1] + fibonachchi_royxati[x - 2])
#     return fibonachchi_royxati

# print(fibonachchi(7))



#MASHQ
# def royxat(min, max, oraliq =''):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         if oraliq:
#             min += oraliq
#         else:
#             min += 1
#     return sonlar

# print(royxat(2, 50, 5))
























    
    
    
    
    
    
    
    