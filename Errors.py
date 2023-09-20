"""
27/11/2020
Dasturlash asoslari
#12-dars: Xatolar
Muallif: Anvar Narzullaev
Web sahifa: https://python.sariq.dev
"""

#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f"{x}>{y}")



#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat=[]

#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#if savat:
#    for mahsulot in savat:
#        if mahsulot in mahsulotlar:
#            print(f"Do'konimizda {mahsulot} bor")
#        else:
#            print(f"Do'konimizda {mahsulot} yo'q")
#else: 
#    print("Savatingiz bo'sh")



#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:"))

#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)

#if mavjud_emas:
#  print("Do'konimizda quyidagi mahsulotlar yo'q:")
#  for mahsulot in mavjud_emas:
#      print(mahsulot)
#else:
#  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    


#users = ['alisher1983','aziza','yasina' 'umar']

#login = input("Yangi login tanlang:")

#if login in users:
#    print('Login band, yangi login tanlang!')
#else:
#   print("Xush kelibsiz!")



son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")














