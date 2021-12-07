n1 = list()
for i in range(15):
    ele = int(input("Introduzca numero: "))
    n1.append(ele)
    
    
S = sum(n1)
Min = min(n1)
Max = max(n1)
Promedio = S / len(n1)

print("El mayor de los números es:", Max)
print("El menor de los números es:", Min)
print("La suma de todos los números es:", S)
print("El promedio de todos los números es:", Promedio)