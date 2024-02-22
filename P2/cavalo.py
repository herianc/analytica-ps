COLUNAS = 'abcdefgh'
LINHAS = '12345678'


def validacao_movimento(entrada: str) -> None:
    # Verificando se as posições pertencem ao tabuleiro
    if entrada[1] in LINHAS and entrada[0] in COLUNAS and entrada[4] in LINHAS and entrada[3] in COLUNAS:

        # Separando as colunas e linhas iniciais
        indice_l_ini = LINHAS.index(entrada[1])
        indice_c_ini = COLUNAS.index(entrada[0])

        # Separando as colunas e linhas finais
        indice_c_final = COLUNAS.index(entrada[3])
        indice_l_final = LINHAS.index(entrada[4])

        # Calculando a diferença entre as posições finais e iniciais
        delta_linhas = indice_l_final - indice_l_ini
        delta_colunas = indice_c_final - indice_c_ini

        # Verificando se a movimentação
        if delta_linhas == 1 or delta_linhas == -1:
            if delta_colunas == 2 or delta_colunas == -2:
                print('VÁLIDO')
            else:
                print('INVÁLIDO')

        elif delta_linhas == 2 or delta_linhas == -2:
            if delta_colunas == 1 or delta_colunas == -1:
                print('VÁLIDO')
            else:
                print('INVÁLIDO')
        else:
            print('INVÁLIDO')

    else:
        print('INVÁLIDO')


if __name__ == '__main__':
    while True:
        entrada = input('Posições: ')

        if entrada.lower() == 'f':
            print('Fim...')
            break
        elif len(entrada) != 5:
            print('Entrada inválida')
        else:
            validacao_movimento(entrada)
