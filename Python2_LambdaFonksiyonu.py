# lambda fonksiyonu matamatikteki fonksiyonlar gibi :)
#Kullanım alanları sadece 1 kere fonksiyon kullanılması gerekiyorsa oralarada kulanaıllabilir.
# Bir liste oluşturup index sayısı ile benim verdiğim sayiyı toplayıp index sayısına bölen program

def MyList(listLength):
    return lambda x: [(index + x) / index for index in range(1, listLength)]


f = MyList(4)
print(f(5))
