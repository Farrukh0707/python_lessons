import random

def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha bo'lgan son o'yladim. Topa olasizmi ?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input("O'ylagan soningizni kiriting: "))
        if taxmin > tasodifiy_son:
            print("Men o'ylagan son bundan kichikroq. Yana harakat qilib ko'ring: ")
        elif taxmin < tasodifiy_son:
            print("Men o'ylagan son bundan kattaroq. Yana harakat qilib ko'ring: ")
        else:
            break
    print(f"Tabriklaymiz. {taxminlar}-urinishda topdingiz.")
    return taxminlar

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va 'enter' tugmasini bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == '-':
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar}-urinishda topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user > taxminlar_pc:
            print("Siz yutdingiz.")
        elif taxminlar_user < taxminlar_pc:
            print("Men yutdim.")
        else:
            print("Durang.")
        yana = int(input("Yana o'ynaysizmi ? Ha(1)/Yo'q(0): "))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        