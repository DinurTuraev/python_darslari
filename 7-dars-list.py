#08.09.2021
#Python dasturlash asoslari
#7-dars "List"

#Ismlar degan ro'yhat yarating va kamida uchta yaqin do'stingizning ismini kiriting
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring
# ismlar = ["Arslon","Qanot", "Xursand"]
# print("Salom ", ismlar[0], "bugun choyxona bormi?")
# print(f"{ismlar[0]}, {ismlar[1]} va {ismlar[2]} birga mazza qilib o\'tirardik")

#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
#sonlar = ['10', '-7', '11', '99.9']
#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
#sonlar[0]=sonlar[0]+sonlar[-1]
#del sonlar[0]

#t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
#t_shaxslar = ["Al Xorazmiy", "Beruniy", "Buxoriy", "Termiziy"]
#z_shaxslar = ["Abdukarim Mirzayev", "Muhammadali Eshonqulov", "Anvar Narzullayev", "Saidbek Arislanov",]
#print("Men tarixiy shaxslardan ", t_shaxslar.pop(2), "va zamonaviy shaxslardan", z_shaxslar.pop(2),"bilan uchrashishni hohlayman")

#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append("Xursand") 
friends.append("Qanot") 
friends.append("Arslon") 
friends.append("Akmal") 
friends.append("Abdukarim") 
friends.append("Ali") 
#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove("Akmal")
friends.remove("Abdukarim")
friends.remove("Ali")
#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append("Abdulloh")
friends.insert(0, "Muhammad")
friends.insert(2, "Abdulmalik")
#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))
print("\nKelgan mehmonlar", mehmonlar)