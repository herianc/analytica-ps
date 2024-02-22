def frequencia_numeros() -> None:
    numeros = []

    while True:
        entrada = input()
        if entrada == 'f':
            break
        elif entrada.isdigit():  # Verificando se é um dígito
            numeros.append(entrada)

    numeros_unicos = []

    # Printando a frequencia de cada palavra
    for num in numeros:
        if num not in numeros_unicos:  # Verificação para evitar repetições no print
            numeros_unicos.append(num)
            repeticao = numeros.count(num)

            if repeticao > 1:
                print(f'O número {num} apareceu {repeticao} vezes')
            else:
                print(f'O número {num} apareceu {repeticao} vez')


if __name__ == '__main__':
    frequencia_numeros()
