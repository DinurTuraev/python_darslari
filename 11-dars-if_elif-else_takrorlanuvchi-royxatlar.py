# 12.09.2021
# Python dasturlash asoslari
# 11-dars "IF ELIF ELSE" "Takrorlanuvchi ro'yxatlar"

# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# son = float(input("Juft son kiriting: "))
# if son%2:
#     print("Bu juft son emas")
# else:
#     print("Rahmat")

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
    # Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
    # Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
    # Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = float(input("Yoshingizni kiriting: "))
# if yosh < 4 or yosh > 60:
#     print("Sizga kirish bepul")
# elif yosh < 18:
#     narh = 10000
#     print(narh)
# else:
#     narh = 20000
#     print(narh)

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x == y: print(f"{x}={y}")
# elif x > y: print(f"{x}>{y}")
# else: print(f"{x}<{y}")

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ['Non', 'Tuxum', 'Sut', 'Qatiq', 'Ayron', 'Asal', 'Suv', 'Uzum', 'Olma', 'Shaftoli']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-maxsulot nomini kiriting: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} mavjud")
#     else:
#         print(f"Do'konimizda {mahsulot} mavjud emas")
        
# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqarin        
# mahsulotlar = ['Non', 'Tuxum', 'Sut', 'Qatiq', 'Ayron', 'Asal', 'Suv', 'Uzum', 'Olma', 'Shaftoli']        
# savat = [] 
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-maxsulot nomini kiriting: "))

# bor_mahsulotlar =[]
# mavjud_emas = []  
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q: ")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulot do'konimizda mavjud")         
 
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
# foydalanuvchilar = ['arslon', 'asad','ali', 'akbar', 'azamat' ]   
# login = input("Yangi login kiriting: ")
# if login.lower() in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {login.title()}!")
        
# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.        
# son = int(input("Butun son kiriting: "))
# for n in range(2,11)        :
#    if not (son%n):
#         print(f"{son} soni {n}ga qoldiqsiz bo'lindi")
        
        
        
        
        
        
        
        
        
        
        
        
        
        