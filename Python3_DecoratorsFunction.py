# Dekoratöreler yazılmış bir fonksiyona işlevsellik eklemek veya
# o fonksiyonun öncesi yada sonrasında yapılmasını istediğimiz koşulları da eklememize yardımcı olurlar.
# Kodun okuurluğubu da kolaylaştırır.

def f1(a1Param):
    print("is 1 ")

    def f2():
        print("is 2")
        return a1Param()

    return f2


@f1  # = karsılığı=f1(a1) la aynı şey
def a1():
    print("baslangıc fonk : a1")


a1()
