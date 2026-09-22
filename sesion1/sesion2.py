def saludo():
    return print(" hOLA MUNDO")

def saludo2(name):
    return print("Hola", name)


def sumar(a,b):
    if b==0:
        return print("El segundo numero es cero")
    else:
        return print("La dividion de ",a," y ",b, " es " ,a/b)

saludo2("Jesus")

sumar(3,0)

try:
    var1 = int (input("Ingrese un numero: "))
except ValueError:
    print("El numero ingresado es: ",var1)