#MASHQLAR
#1-mashq
#ismlar = ['Dilyor', 'Jasur', 'Musabek']
#print('Salom', ismlar[0], "bugun futbol o'ynaymizmi ?")
#print(ismlar[1], "suzishga boraylik.")
#print(ismlar[2], "kurs ishini tugatdingmi ?")

#2-mashq
#sonlar = [77, -5, 9.8, 66]
#print(sonlar[0] + sonlar[-1])
#sonlar[0] = sonlar[0]*2
#print(sonlar)
#sonlar[1] = sonlar[-1]
#sonlar[0] = sonlar[2]
#print(sonlar)

#3-mashq
#t_shaxslar = ['A.Navoiy', 'A.Temur', 'Z.Bobur']
#z_shaxslar = ['Stive Jobs', 'Bill Geyts', 'Ilon Musk']
#print("Men tarixiy shaxslardan", t_shaxslar.pop(2), "bilan, zamonaviy shaxslardan esa", z_shaxslar.pop(2), "bilan suhbat qilishni istar edim.")

#4-mashq
friendsnew = []
friendsnew.append('Anvar')
friendsnew.append('Bobur')
friendsnew.append('Temur')
friendsnew.append('Ahmad')
friendsnew.append('Muhammad')
#print(friends)

friendsnew.remove('Ahmad')
friendsnew.remove('Temur')
print(friendsnew)
#print(friends)

#friends.insert(0, 'Bekzod')
#friends.insert(3, 'Jalol')
#friends.append('Yunus')
#print(friends)

#5-mashq
mehmonlar = []
mehmonlar.append(friendsnew.pop(0))
mehmonlar.append(friendsnew.pop(1))
mehmonlar.append(friendsnew.pop(-1))

print("Do'stlar: ",friendsnew)
print("Mehmonlar: ",mehmonlar)
