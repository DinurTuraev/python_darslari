# 12.09.2021
# Python dasturlash asoslari
# 14-dars "Lug'at"

# Otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

dadam = {'ism' : 'Dilshod', 't_yil' : '1979', 't_shaxar' : 'Turtkul'}
print(f"Dadamning ismi {dadam['ism'].title()}, {dadam['t_yil']}-yilda, {dadam['t_shaxar'].title()} shaxrida da tug'ilgan.")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
s_taom = {'Bobom':'besh barmoq',
          'Buvim':'manti',
          'dadam':'palov',
          'onam':'norin',
          'Ukam':'qovurdoq'
          }
print(f"Bobomning sevimli taomi {s_taom['Bobom']},\
      \nBuvimning sevimli taomi {s_taom['Buvim']},\
      \nUkamning sevimli taomi {s_taom['Ukam']}. ")

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
python = {'string':'matn',
          'integer':'butun son',
          'float':"o'nli son",
          'for':'uchun',
          'in':'ichida',
          'if':'agar',
          'elif':'aks holda',
          'else':"bo'lmasa",
          'upper':'hamma harfini katta yozadi',
           'lover':'hamma harfni kichkina yozadi'
          } 

#Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

kalit = input("Kalit so'zni kiriting: ").lower()
print(python.get(kalit, "Bunday izoh mavjud emas!")) # 1-usul

# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring
   
if kalit in python:
    print(f"python[kalit] # 2-usul
else:
    print("Bunday izoh mavjud emas!")

kalit = input("Kalit so'z kiriting:").lower() # 3-usul
tarjima = python.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")












