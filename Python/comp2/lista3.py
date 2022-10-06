import datetime as dt

if __name__ == '__main__':

    data_atual = dt.datetime.now()

    nomes = open("nomes.txt","r")
    arquivo = nomes.readlines()

    marte = open("Marte.txt","w")
    jupiter = open("Jupiter.txt", "w")

    for linha in arquivo:
        valor = linha.split(", ")
        if (data_atual.year - int(valor[1])) < 30 and valor[3] == 'Marte\n':
            texto = valor[0] + ' - ' + str((valor[2]*38)/100)
            print(texto)
        #if (data_atual.year - int(valor[1])) > 30 and valor[3] == 'Júpiter\n':
        #    print(valor)
    
    nomes.close()
    marte.close()
    jupiter.close()


            
'''
    jupiter = open("Jupiter.txt","w")
    marte = open("Marte.txt","w")
'''