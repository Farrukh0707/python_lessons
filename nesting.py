#MASHQLAR
#1-mashq
#ajdod_1 = {
#    'ism': 'amir temur',
#     'tyil': 1336,
#     'tjoy': 'shahrisabz',
#     'umr': 69,
#     'asarlar': ['temur tuzuklari']
#     }

# ajdod_2 = {
#     'ism': 'alisher navoiy',
#     'tyil': 1441,
#     'tjoy': 'hirot',
#     'umr': 60,
#     'asarlar': ['hamsa', 'mahbub ul-qulub', 'lison ut-tayr', 'muhokamatu-l-lug\'atayn']
#     }

# ajdod_3 = {
#     'ism': 'mirzo ulug\'bek',
#     'tyil': 1394,
#     'tjoy': 'sultoniya',
#     'umr': 55,
#     'asarlar': ['ziji jadidi ko\'ragoniy', 'risolayi Ulug\'bek']
#     }

# ajdod_4 = {
#     'ism': 'abu rayxon al beruniy',
#     'tyil': 973,
#     'tjoy': 'beruniy',
#     'umr': 75,
#     'asarlar': ['geodeziya', 'hindiston', 'mineralogiya']
#     }

# ajdodlar = [ajdod_1, ajdod_2, ajdod_3, ajdod_4]

# for ajdod in ajdodlar:
#     print(f"{ajdod['ism'].title()} "
#           f"{ajdod['tyil']}-yilda "
#           f"{ajdod['tjoy'].title()} shahrida tug'ilgan. "
#           f"{ajdod['umr']} yil umr ko'rgan."
#           )

# for ajdod in ajdodlar:
#     print(f"{ajdod['ism'].title()} ning mashxur asarlari: ")
#     for asar in ajdod['asarlar']:
#         print(asar.capitalize())



#2-mashq
# kinolar = {
#     'anvar': ['titanik', 'baron', 'terminator'],
#     'alisher': ['poyga', 'abdullajon', 'shum bola'],
#     'abbos': ['maftuningman', 'ruh 5.13', 'niqob'],
#     'adham': ['panoh', 'uchrashuv', 'vir-zara']    
#     }

# for ism, kino in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for sevimli_kino in kino:
#         print(sevimli_kino.title())
    


#3-mashq
davlatlar= {
    "o'zbekiston": {
        'poytaxt': 'Toshkent',
        'hududi': 448978,
        'aholisi': '35 000 000',
        'pul birligi': "so'm"
        },
    
    "rossiya": {
        'poytaxt': 'Moskva',
        'hududi': 17098246,
        'aholisi': '149 000 000',
        'pul birligi': "rubl"
        },
    
    "AQSH": {
        'poytaxt': 'Washington',
        'hududi': 9631418,
        'aholisi': '330 000 000',
        'pul birligi': "dollar"
        },
    
    "malayziya": {
        'poytaxt': 'Kuala lumpur',
        'hududi': 329750,
        'aholisi': '30 000 000',
        'pul birligi': "rinngit"
        }
    }

# for davlat, info in davlatlar.items():
#     print(f"\n{davlat}ning poytaxti - {info['poytaxt']} shahri."
#           f"\nHududi: {info['hududi']} kv.km;"
#           f"\nAholisi: {info['aholisi']};"
#           f"\nPul birligi: {info['pul birligi']}."
#           )

user_davlat = input('Davlat nomini kiriting: ').lower()
if user_davlat in davlatlar:
    info = davlatlar[user_davlat]
    print(
          f"\n{user_davlat.capitalize()}ning poytaxti - {info['poytaxt']} shahri."
          f"\nHududi: {info['hududi']} kv.km;"
          f"\nAholisi: {info['aholisi']};"
          f"\nPul birligi: {info['pul birligi']}."
          )
else:
    print("Bizda bunday davlat haqida ma'lumot mavjud emas.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    