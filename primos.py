num = int(input("inserta un numero \n"))
es_primo = 1
for i in range(2,num):
    if num % i == 0:
        es_primo = 0

if es_primo == 1:
    print("Tu numero es primo")
else:
    print("Tu numero no es primo")
