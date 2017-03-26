import random
sayi = random.randint(1,100)
print ("Tahmin Oyununa Hos Geldiniz")
sayac=1
tahmin=0

while tahmin != sayi:
    tahmin = int(input("Sayi Girin:"))

    if tahmin == sayi:
        print ("\nTebrikler {} denemede bildiniz!" .format(sayac))
        break

    elif tahmin < sayi:
        print ("Daha Buyuk Bir Sayi Girin")
        sayac += 1

    else: #tahmin > sayi
        print ("Daha Kucuk Bir Sayi Girin")
        sayac += 1
