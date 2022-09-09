import time

hora = time.strftime("%H")
minutos = time.strftime("%M")

if  int(hora) >= 19:
    print("Se termino el laburo!")   
else:
    print("Todavia falta :_(, recien son las: ", hora, "Horas, y ", minutos, "Minutos")    
