
def angulo_ponteiros(horario: str) -> None:
    try:
        hora, minutos = horario.split(':')
        hora, minutos = int(hora), int(minutos)
    except ValueError:
        print('Input Inválido!')

    # Verificando se os valores estão dentro do alcance
    if not hora in range(0, 25) or not minutos in range(0, 60):
        print('Input inválido')
    else:
        if hora > 12:
            hora = hora - 12

        # Este calculo leva em consideração a movimentação do ponteiro da hora com o passar dos minutos
        angulo = abs(hora * 60 - 11 * minutos)/2

        # Se o valor encontrado for maior que 180, o menor angulo é o complementar
        if angulo > 180:
            angulo = 360 - angulo
        print(f'O menor angulo é {angulo:.0f}º')


if __name__ == '__main__':
    while True:
        horario = input('Horário: ')

        if horario.lower() == 'f':
            print('Fim...')
            break
        if len(horario) != 5:
            print('Input inválido')
        else:
            angulo_ponteiros(horario)
