def miesiace():
    miesiace = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']
    for i in range(0, 12, 1):
        yield miesiace[i]

miesiace = miesiace()
for i in range(0, 12, 1):
    print(next(miesiace))