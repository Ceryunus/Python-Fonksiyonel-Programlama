#Tuple olan veriyi Maaşı en fazla olana göre sıralama
employeeList = [
    # ("ad","pozisyon","Tl maas","Dolar maas")
    ("Ahmet", "Amir", 10000, 0),
    ("Ezgi", "İdari İşler", 8000, 0),
    ("Elif", "Hukuk", 5000, 0),
    ("Jhon", "İdari İşler Müdürü", 0, 5000)

]
dolarrate = 8.29
employeeList.sort(key=lambda employee: employee[2] if employee[2] != 0 else employee[3] * dolarrate, reverse=True)
# employee[2] eğer 0 değilse employee[2] göre sıralama yap eğer 0 sa employee[3]*dolar ile carp ve öyle sırala diyoruz

print(employeeList)
