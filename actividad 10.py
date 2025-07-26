def menu():
    print("MENU RECURSIVIDAD")
    print("1. invertir una cadena a texto")
    print("2. calcular la suma ede los N numeros naturales")
    print("3. imprimir una cuenta recursiva de N hasta 1")
    print("4. sumar los digitos de un numero")
    print("5 contar cuantos digitos tiene un numero")
    print("6. salir")
def cadena_texto(cadena):
    letras=reversed(cadena)
    return  letras

def suma_numeros(numero):
    n = numero

menu()
op=int(input("ingrese opcion a ejecutar"))
if op==1:
    cad=input ("ingrese cadena a texto")
    print(cadena_texto(cad))
elif op==2:
    num=int(input("ingrese numero"))
