#MASHQLAR
#1-mashq
# book = ('Sevimli kitoblaringizni kiriting')
# book += "(Dasturni tugatish uchun 'stop' so'zini yozing):"

# while True:
#     books=input(book)
#     if books == 'stop':
#         break

# print('Rahmat')   



#2-mashq
#break
# savol = ('Yoshingiz ')
# savol += "(Dasturni tugatish uchun 'quit' yoki 'exit' ni bosing):"
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
    
#     if yosh < 7:
#         narh = 2000
#     elif 7 <= yosh < 18:
#         narh = 3000
#     elif 18 <= yosh < 65:
#         narh = 10000
#     else:
#         narh = 0
        
#     if narh == 0:
#         print('Sizga kirish bepul.')
#     else:
#         print(f"Chipta {narh} so'm.")
        
     
#ishora
# savol = ('Yoshingiz ')
# savol += "(Dasturni tugatish uchun 'quit' yoki 'exit' ni bosing):"
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         ishora = False
#     yosh = int(qiymat)
    
    
#     if yosh < 7:
#         narh = 2000
#     elif 7 <= yosh < 18:
#         narh = 3000
#     elif 18 <= yosh < 65:
#         narh = 10000
#     else:
#         narh = 0
        
#     if narh == 0:
#         print('Sizga kirish bepul.')
#     else:
#         print(f"Chipta {narh} so'm.")




#3-mashq
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    elif float(qiymat) < 0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng.\n")





































