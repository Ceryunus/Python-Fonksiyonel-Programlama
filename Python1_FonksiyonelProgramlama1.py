# Fonksiyonel programlama
# functionları bir listeye koyup sonradaan cağırabiliyorum burada

def ActionOne(param="Default"):
    print(f"ActionOne {param}")


def ActionTwo(param="Default"):
    print(f"ActioTwo {param}")


myFuncList = [ActionOne, ActionTwo]
myFuncList[0]("Dememe")
myFuncList[1]("Deneme2")
for i in myFuncList:
    i()
    i("Deneme3")
