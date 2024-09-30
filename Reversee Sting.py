def Revsese_String(string):
    if(len(string) == 1):
        return string[0]
    
    first_character = string[0]

    return Revsese_String(string[1:]) + first_character

print(Revsese_String("Yash"))