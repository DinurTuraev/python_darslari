#11.09.2021
#Python dasturlash asoslari
#9-dars "For takrorlash operatori"

#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#ismlar = ['Muhammad', 'Abdulloh', 'Abdurrahmon', 'Abdukarim', 'Abdulmalik']
#for ism in ismlar:
#       print(f"Salom {ism}")

#Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#print("kod", len(ismlar), "marta takrorlandi")

#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
#toq_sonlar = list(range(11,100,2))
#for kub in toq_sonlar:
#    print(kub**3)
    
#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
#kinolar = []
#print("5 ta sevgan kinoingizni kiriting:")
#for sevimli in range(5):
#    kinolar.append(input(f"{sevimli+1}-kino:"))
#print(kinolar)
#Buni ishlay olmadim shuning uchun Anvar Narzullaevdan ko'chirdim

#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
#suhbatdoshlar = int(input("Bugun qancha odam bilan suhbatlashdingiz? "))
#suhbatlashganlar = []
#for s in range(suhbatdoshlar):
#    print(suhbatlashganlar.append(input("Suhbatdoshlaringiz nomini kiriting   ")))
#print(f"Bugun siz {suhbatlashganlar} lar bilan gaplashgansiz")

#Buyam Anvar Narzullaevdan nagli ko'chirildi
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)




































































   
    


    





