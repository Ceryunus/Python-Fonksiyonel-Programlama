#Lambda ile yaşlarına göre sıralama
myList = [ { "name" : "Arif"  , "age" : 26 },
           { "name" : "Serhat", "age" : 28 },
           { "name" : "Şahin" , "age" : 29 },
           {"name"  : "Ali"   , "age" : 10 }]

#ilk yas
myList.sort(key=lambda item :item["age"])
print(myList)