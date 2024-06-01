import math
numero=int(input("Ingrese un numero: "))

for i in range(2,int(math.sqrt(numero))+1):
    if (numero % i == 0):
      resultado="No es Primo"
    else:
      resultado="Es Primo"
      
print("El numero "+resultado)





