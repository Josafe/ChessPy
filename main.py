
#Operadors de comparació:

nombre = input('Com et dius?')
print('Hola' + nombre)

edad = int(input('Quants anys tens'))

masDe12 = edad >= 12

##Si es fill del dueño de la montaña rusa podra passar encara que tingue menys de 12 anys, nomes cal que digue "Si"
respuestaHijoDelDueño = input('Ets fill del jefe?')

hijoDelDueño = respuestaHijoDelDueño == 'Si' #Si es = a true en el bool

puedePasar = masDe12 or hijoDelDueño #Si te +12 anys o es fill del dueño pot passar

if puedePasar:
    print('Puedes pasar')
else:
    print('No puedes pasar')


if edad > 18:
    print("Es major d'edat")
else:
    print("Es menor d'edat")


#Comparador aritmetics
