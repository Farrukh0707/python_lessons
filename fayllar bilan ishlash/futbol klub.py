
while True:
    clubs = input("Sevimli futbol klubingiz haqida ma'lumot kiriting(To'xtatish uchun 'Enter' bosing): ")
    if not clubs:
        break
    with open('footbal_club.txt', 'a') as file:
        file.write(clubs + '\n')