def calculadora_troco(valor: float) -> None:

    NOTAS = [100, 50, 20, 10, 5, 2]
    MOEDAS = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

    print("NOTAS:")
    for nota in NOTAS:
        quantidade_notas = valor // nota  # Obtendo o número inteiro de notas
        valor -= quantidade_notas * nota  # Retirando o valor em notas do valor total
        print(f"{quantidade_notas} nota(s) de R$ {nota:.2f}")

    print("MOEDAS:")
    for moeda in MOEDAS:
        quantidade_moedas = valor // moeda  # Obtendo o numero inteiro de moedas
        valor -= quantidade_moedas * moeda  # Retirando o valor em moedas do valor total
        print(f"{quantidade_moedas} moeda(s) de R$ {moeda:.2f}")


if __name__ == '__main__':
    entrada = input('Valor: ')

    try:
        valor = float(entrada)
        if valor < 0:
            print("Valor inválido.")
        else:
            calculadora_troco(valor)
    except ValueError:
        print("Entrada inválida.")
