def get_tipo_dia(dia):
    dias = {
        1: 'Fim de Semana',
        2: 'Dia de Semana',
        3: 'Dia de Semana',
        4: 'Dia de Semana',
        5: 'Dia de Semana',
        6: 'Dia de Semana',
        7: 'Fim de Semana',
    }
    return dias.get(dia, 'Data Inválida')

if __name__ == '__main__':
    for dia in range(0,9):
        print(f'{dia}: {get_tipo_dia(dia)}')