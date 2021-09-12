#09.09.2021
#Python dasturlash asoslari
#8-dars "Ro'yxatlar bilan ishlash"

#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ['Uzbekistan', 'Kazakhstan', 'Turkmenistan', 'Tadjikistan', 'Qyrgyzstan']
#Ro'yxatning uzunligini konsolga chiqaring
print(davlatlar)
print(len(davlatlar))
#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True))
#Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)
#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)
#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar = list(range(120,1200,2))
#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
jami = sum(juft_sonlar)
print(jami)
#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
kichik = min(juft_sonlar)
katta = max(juft_sonlar)
print(katta-kichik)
#Ro'yxatdagi elementlar sonini hisoblang
print(len(juft_sonlar))
#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(juft_sonlar[0:21])
print(juft_sonlar[160:181])
print(juft_sonlar[-21:-1])
#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['Palov', 'Manti', 'Qovurdoq','Moshkichri', 'Mastava']
#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('Mastava')
nonushta.remove('Moshkichri')
nonushta.remove('Qovurdoq')
#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar, nonushta)
#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"



























