def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

if __name__=='__main__':
    numero=int(input('Ingrese el numero a calcular:'))
    if numero < 0:
        print("El numero debe ser positivo")
    else:
        resultado=factorial(numero)
        print(f'{numero}!={resultado}')

