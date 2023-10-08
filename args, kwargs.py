#1-mashq
# def kopaytma(*sonlar):
#     natija = 1;
#     for son in sonlar:
#         natija *= son
#     return natija

# print(kopaytma(1,2,3,-5))

#2-mashq
def talaba_info(familiya, ism, **info):
    info['familiya'] = familiya;
    info['ism'] = ism;
    return info

talaba1 = talaba_info("Akbarov", "Ali", yosh="22 yoshda", guruh="410-15 guruh talabasi")
talaba2 = talaba_info("Mallayev", "Akobir", yosh="21 yoshda", guruh="411-15 guruh talabasi")

talabalar = [talaba1, talaba2]
print(talabalar)