def ler_texto(texto):
    pontuacao = {1:'.', 2:',',3:';', 4:'?', 5:'!', 6:':'}
    return 0
if __name__ == '__main__':
    txt = 'super super! choque, pão, presunto?, presunto'
    x = txt.split( )
    pontuacao = {1:'.', 2:',',3:';', 4:'?', 5:'!', 6:':'}
    for e in x:
        y = ''
        for pont in pontuacao.values():
            y = e.strip(pont)
        print(y)   
        