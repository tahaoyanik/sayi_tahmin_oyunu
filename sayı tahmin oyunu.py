import random
import time

print("""
******************************
      Sayı Tahmin Oyunu
      
      1 ile 40 arasında
******************************
""")

rastgele_sayi = random.randint(1,40)
tahmin_hakki=10
while True:
    tahmin = int(input("Tahmininiz :"))
    if tahmin<rastgele_sayi:
        print("program Sorgulanıyor...")
        time.sleep(1)
        print("Daha büyük bir sayı giriniz")
        tahmin_hakki-=1

    elif tahmin>rastgele_sayi:
        print("Program sorgulanıyor...")
        time.sleep(1)
        print("Daha küçük bir sayı giriniz.")
        tahmin_hakki-=1

    else:
        print("Program sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler",rastgele_sayi)
        break

    if tahmin_hakki==0:
        print("Hakkınız bitii")
        break