def añobisiesto(año):
    if año % 4 != 0:
        return "No es bisiesto"
    elif año % 4 == 0 and año % 100 != 0:
        return "Es bisiesto"
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
        return "No es bisiesto"
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
        return "Es bisiesto"
    
print(añobisiesto(2020))
print(añobisiesto(2021))
