def pertence_fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a+b
    return False
numero = int(input("Digite um número: "))
if pertence_fibonacci(numero):
    print(numero, "é de Fibonacci.")
else:
    print(numero, "não é de Fibonacci.")