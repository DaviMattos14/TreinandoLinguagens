def homens40(funcionarios, func_M, func40):
    f = set(funcionarios)
    mulheres = set(func_M)
    h_40 = set(func40)
    return (f - mulheres) - h_40


if __name__ == '__main__':
    func = ['Marcos', 'Lucas', 'Mariana', 'Yan', 'Carlos',
            'Larissa', 'Leticia', 'Debora', 'Alana', 'Alan', 'Caio']
    mulheres = ['Mariana', 'Larissa', 'Leticia', 'Debora', 'Alana']
    homens = ['Marcos', 'Alan', 'Carlos']
    # Lucas, Yan, Caio
    hom_menos_40 = homens40(func, mulheres, homens)
    print(hom_menos_40)
