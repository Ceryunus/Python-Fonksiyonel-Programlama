#Lambda ile Soyadına göre sıralama
nameList= ["Yunus Emre","Abdul kadir", "Fatih","Hasan Can","Cüneyt arkın"]
nameList.sort(key=lambda name:name.split(" ")[-1].lower())
print(nameList)