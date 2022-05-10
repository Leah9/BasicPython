from datetime import datetime

presDict = {"Lyndon B Johnson" : (1908, 8, 27),
            "Richard Nixon" : (1913, 1, 9),
            "Gerald Ford" : (1913, 7, 14),
            "Jimmy Carter" : (1924, 10, 1),
            "Ronald Reygan" : (1911, 2, 6),
            "George H W Bush" : (1924, 6, 12),
            "Bill Clinton" : (1946, 8, 19),
            "George W Bush" : (1946, 7, 6),
            "Barak Obama" : (1961, 8, 4),
            "Donald Trump" : (1946, 6, 14)}

presidents = presDict.keys()

print(presidents)
for president in presDict:
    dt = presDict.get(president)
    #print(dt)
    adt = datetime(*dt)
    #print(adt.weekday())
    if adt.weekday() == 0:
        print(president + " was born on Sunday")