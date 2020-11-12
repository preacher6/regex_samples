#%%
import re
 
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
patron = "Lorem"
 
x = re.search(patron, texto) #Busca el patron dentro del texto
 
print(x.span()) #Escribe la posicion inicial y final de la ocurrencia

# %%
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit door"
patron1 = "Lorem"
patron2 = "ipsum"
 
x = re.match(patron1, texto) #Busca el patron dentro del texto
print(x.span()) #Escribir la posicion inicial y final
 
y = re.match(patron2, texto) # Devuelve None
print(y.span()) #ERROR!
# %%
texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."""
patron = "dolor"
 
x = re.finditer(patron, texto) #Devuelve un vector con las posiciones de las ocurrencias
 
for i in x:
    print(i.span())
# %%
texto = "010001000100111001"
 
patron = "01+0"
 
x = re.finditer(patron, texto)
for i in x:
    print(i.span())
# %%
## capicúa
import re
 
texto = input("Introduce una secuencia binaria de cinco cifras:\n")
patron = "(0.{3}0)|(1.{3}1)"
 
valido = False
 
#Se comprueba que el input sea valido:
if len(texto) == 5:
    valido = True
    for i in texto:
        if i != '0' and i != '1':
            valido = False
            break
 
#Si el input es valido, se compreuba si es capicua
if valido:
    x = re.search(patron, texto)
    if(x != None):
        print("Es capicua!")
    else:
        print("No es capicua!")
 
#Si el input no es valido, aparece un mensaje de error:
else:
    print("ERROR: texto no valido")
# %%
## Impares
 
texto = "551 889 302 105 012 817 894 206"
 
patron = "[0-9]{2}[13579]"
 
x = re.findall(patron, texto) #Devuelve un vector con los substrings de las ocurrencias
 
for i in x:
    print(i)
# %%
# Descartar valores q contengan el 3 y separa espacios
 
texto = "551 889 302 105 012 817 894 206"
 
patron = "[^8 ]{3}"
 
x = re.findall(patron, texto) #Devuelve un vector con los substrings de las ocurrencias
 
for i in x:
    print(i)
# %%
