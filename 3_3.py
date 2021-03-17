produkty = {"banany": "kg",
            "ser": "plastry",
            "baton": "sztuki",
            "woda": "litry"}
odwrocony = {value: key for key, value in produkty.items()}
sztuki = [odwrocony["sztuki"]for x in odwrocony]
print(produkty)
print(odwrocony)
print(sztuki)