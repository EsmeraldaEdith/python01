#Ademas de expulsar datos o información , los programas reciben valores que de alguna
#forma, manipulan y transforman. Python trae una función incorporada llamada input, 
#que permite ingresar , datos o valores al programa.

print ("hola, dime cual es tu nombre")
name = input ()
print = ("hola" +name)
print ("¿cuantos años tienes?")
#una caracteristica de la funcion input es que solo entrega texto
age = int (input())
print (type(age))

#posibilidades con print
file_result = open('/path/to/file/.txt' ,'w')
print (f"naciste en" 2023-age,sep=": ",file=file_result)
