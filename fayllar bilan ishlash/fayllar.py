#MASHQLAR
# filename = "Dars tushunchalari.txt"
# information = "Pythonning fayllar bilan ishlash darsida fayl yaratib uning ichiga ma'lumot kiritish, ularni tahrirlash va shu kabilar o'rganildi."
# with open(filename, 'w') as file:
#     file.write(information)

import pickle

fayl_nomi = 'pi_million_digits.txt'
with open(fayl_nomi) as fayl:
    pi = fayl.read()
pi = pi.rstrip()
pi = pi.replace("\n", "")
pi = pi.replace(" ", "")


tkun_tyil = input("Tug'ilgan kuningiz va yilingizni kiriting: ")
print(tkun_tyil in pi)

pi = float(pi)

with open('pi_float.dat', 'wb') as file:
    pickle.dump(pi, file)