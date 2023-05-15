
def processoSeletivo(opcao): #def para licalizar qual o processo seletivo
    if opcao == 1:
         return ('Entrevista')
    elif opcao == 2 :
        return  ('Teste Teórico')
    elif opcao == 3:
        return ('Teste Prático')
    elif opcao == 4:
        return  ('Avaliação Soft Skill')
    
def buscaNota (palavra):
    nota=[]
    for i in range(len(palavra)):
        if palavra [i].isdigit():
            if palavra[i] != '0' and palavra [i-1] !='1' and palavra[i] != '1':
                nota.append(int(palavra[i]))

            elif palavra[i] == '1' and palavra[i+1]=='0':
                nota.append (int(10))
    return nota

def buscaCandidato (notaMinima, listaPrincipal): 
    candidato=''
    contador = 0
    for x in range (0,len(listaPrincipal),1):
       palavra = listaPrincipal[x][1]
       nota =buscaNota(palavra)
       if int(nota[0]) >= notaMinima[0]:
         
            if int(nota[1])>= notaMinima[1]:
             
                if int(nota[2])>= notaMinima[2]:
                    
                    if int(nota[3])>= notaMinima[3]:
                        candidato =candidato +str(x+1)+ '.' +listaPrincipal[x][0]+'       '+listaPrincipal[x][1]+' \n____________________________________\n'
                        contador = contador + 1
    if contador == 0:
        print ('não ha candidato')
    else:
        print ('==============================')
        print ('Os selecionados são:\n')
        print (candidato)



listaPrincipal = []
listaCandidatos =[]
numProcessos = 5
notaMinima =[]
inicio =True
while inicio:
    print ('===================================================')
    print ('\nÓla.''\nQuantos candidatos gostaria de cadastrar:\n')
    numeroDeCandidatos =int(input())

    for x in range  (0,numeroDeCandidatos,1):
        guardaNotas = ('eX_tX_pX_sX_')
        print ('Nome do candidato:\n')
        nomeCandidato = input()
        listaCandidatos.append(nomeCandidato)

        for i in range (1,numProcessos,1):
            print ('\nNota de '+(processoSeletivo(i))+':')
            nota = input()
            guardaNotas =  guardaNotas.replace('X',nota,1)
        listaCandidatos.append(guardaNotas)
        listaPrincipal.append(listaCandidatos)
        listaCandidatos=[]
    cadastro =True
    while cadastro:
        print ('============================================')
        print( 'Por favor digite a nota mínima nos processos,''\npara que retorne os candidatos selecionados:\n')

        for i in range (1,numProcessos,1):
            print ('\nNota de '+(processoSeletivo(i))+':')
            nota= int(input())
            notaMinima.append(nota)
        buscaCandidato (notaMinima, listaPrincipal)

        print ('Gostaria de voltar a consultar candidatos ou cadastrar novos: \n1.Consultar\n2.Cadastrar\n3.Sair')
        opcaofinal = input()
        while  not opcaofinal in ('1','2','3'):
            print('\n Opção Invalida digite novamente:  \n1.Consultar\n2.Cadastrar\n3.Sair')
            opcaofinal =input()
        if opcaofinal == '1':
            cadastro = True
        elif opcaofinal =='2':
            cadastro =False
            inicio == True
        elif opcaofinal == '3':
            exit()
