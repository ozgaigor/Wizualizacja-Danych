def dzien_tygodnia(a):
    dzien=["Poniedzialek",
        "Wtorek",
        "Środa",
        "Czwartek",
        "Piatek",
        "Sobota",
        "Niedziela"]
    return dzien[a-1]


def skrot(b):
    skrot = {'PON': "Poniedziałek", 
                'WT': 'Wtorek', 
                'ŚR': 'Środa', 
                'CZW': 'Czwartek',
                'PT': 'Piątek',
                'SOB':'Sobota',
                'ND': 'Niedziela'}
    return (skrot[b])
