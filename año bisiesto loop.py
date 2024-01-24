print("Vamos a calcular cuantos años bisiestos hay en un rango de años")
año_elegido=1900
minimototal=0
while año_elegido>=1900 and año_elegido<2199:
 año_elegido=int(input("Escoge cualquier año desde 1900 hasta 2199"))

 añominimo= 1900
 
 añomaximo =2199
 var1= 1

 if año_elegido >= añominimo and año_elegido<= añomaximo:
 
   cantbisiesto = año_elegido - añominimo
 
   resultbisiesto= cantbisiesto/4

   if resultbisiesto==1:
 
    print("la cantidad de años bisiesto entre 1900 y", año_elegido, "es de")
    print(int(resultbisiesto + 1))
    


   elif resultbisiesto>1:
    print("la cantidad de años bisiesto entre 1900 y", año_elegido, "es de")


    print(int(resultbisiesto))
    
   else:
    print("La cantidad de años bisiestos que hay entre 1900 y ", año_elegido, "es de 1")


if año_elegido <1900 or año_elegido>2199:
 print("Error, no ingresaste los datos solicitados")
 quit()
