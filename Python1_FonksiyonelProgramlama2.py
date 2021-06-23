#1 Function icinde başka bir functionu cağırabiliyorum yapmam gereken
#sonradan calısacak olan Funciton un adaını parmaetre olarka göndermek


def SampleFunc(number,Callback1,Callback2):
    if number % 2 == 0:
        return Callback1
    return Callback2

def Callback1(massage):
    print("cif sayi",massage)


def Callback2(massage):
    print("tek sayi",massage)


number=int(input("Bir Sayi giriniz : "))
f= SampleFunc(number,Callback1,Callback2)
f(number)
