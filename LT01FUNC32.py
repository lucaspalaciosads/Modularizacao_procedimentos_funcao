def calcular_fatorial(numero: int) -> int:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial


def main():
    n = int(input("Digite um valor inteiro para calcular o fatorial: "))
    if n < 0:
        print("Não existe fatorial de número negativo.")
    else:
        resultado = calcular_fatorial(n)
        print(f"O fatorial de {n} é: {resultado}")


if __name__ == "__main__":
    main()