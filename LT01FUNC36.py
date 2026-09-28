def calcular_serie(n):
    soma = 1.0
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
        termo = 1 / fatorial
        soma += termo
        print(f"Termo {i}: 1 / {i}! = {termo:.2f}")
    print(f"\nValor total da série = {n}: {soma:.2f}")
    return soma

def main():
    n = int(input("Digite um número inteiro N: "))
    calcular_serie(n)

if __name__ == "__main__":
    main()