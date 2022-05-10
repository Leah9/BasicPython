
def checker(string1, string2):
    string1a = sorted(string1.upper())
    string2a = sorted(string2.upper())
    if string1a == string2a:
        return(True)
    else:
        return(False)



print(checker("freight", "Fighter"))
