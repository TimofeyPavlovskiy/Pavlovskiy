# TODO Найдите количество книг, которое можно разместить на дискете

InformationVolume = 1.44
Pages = 100
Strings = 50
Symbols = 25
Code = 4
IndexInBytesToMb = 1024*1024

AmountOfBooks = round((InformationVolume*IndexInBytesToMb)/(Pages*Strings*Symbols*Code),0)
AmountNumber = int(AmountOfBooks)

print("Количество книг, помещающихся на дискету:", AmountNumber)
