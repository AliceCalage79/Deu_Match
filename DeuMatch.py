#DEF PARA LOCALIZAR PROCESSO SELETIVO E MOSTRAR NO PRINT PRA COLOCAR AS NOTAS
def processoSeletivo(opcao): 
    if opcao == 1:
         return ('Entrevista')
    elif opcao == 2 :
        return  ('Teste Teórico')
    elif opcao == 3:
        return ('Teste Prático')
    elif opcao == 4:
        return  ('Avaliação Soft Skill')
    
#DEF PARA PROCURAR DENTRO DA STRING PALAVRA, AS NOTAS QUE ESTÃO EM FORMATO STRING E DEVOLVELAS EM FORMATO INTEIRO  
def buscaNota (palavra):
    nota=[]
    for i in range(len(palavra)):
        if palavra [i].isdigit():
            if palavra[i] != '0' and palavra [i-1] !='1' and palavra[i] != '1':
                nota.append(int(palavra[i]))

            elif palavra[i] == '1' and palavra[i+1]=='0':
                nota.append (int(10))
    return nota

#DEF PARA VALIDAR AS ENTRADAS DO USUARIO NO MOMENTO DE CADASTRAR AS NOTAS, SOMENTE INTEIROS DE 0 A 10
def validaNotasUsuario (nota):
            while nota not  in ('0','1','2','3','4','5','6','7','8','9','10'):
                print ('Digite um numero inteiro de (0) a (10):')
                nota= input()
            return nota
        
#DEF PARA BUSCAR OS CANDIDATOS QUE ATENDEM AOS CRITERIOS DE BUSCA SÃO GUARDADOS EM UMA STRING PARA SEREM MOSTRADOS    
def buscaCandidato (notaMinima, listaPrincipal): 
    candidato=''
    contador = 0
    for x in range (0,len(listaPrincipal),1):
       palavra = listaPrincipal[x][1]
       nota =buscaNota(palavra)
       if int(nota[0]) >= int (notaMinima[0]):
         
            if int(nota[1])>= int (notaMinima[1]):
             
                if int(nota[2])>= int (notaMinima[2]):
                    
                    if int(nota[3])>= int(notaMinima[3]):
                        candidato =candidato +str(x+1)+ '.' +listaPrincipal[x][0]+'     '+listaPrincipal[x][1]+'\n'
                        candidato = candidato + '-'*30 +'\n'
                        contador = contador + 1
    if contador == 0:
        print ('-'*30)
        print ('Não há selecionados com esses critérios')
    else:
        print ('Resultado:')
        print ('-'*30)
        print (candidato)
   
# CODIGO PRINCIPAL BOOT INICIAL
listaPrincipal = []                                    # CRIA LISTA PRINCIPAL 
listaCandidatos =[]                                    # CRIA UMA SUBLISTA PARA CADASTRAR OS CANDIDATOS DENTRO DA PRINCIPAL
numProcessos = 5                                       # VARIAVEL NUMERO DE PROCESSOS QUE NO TOTAL SÃO 5
notaMinima =[]                                         # LISTA QUE VAI GUARDAR A NOTA MINIMA PARA SER TESTADA
inicio =True        
                                                       # VARIAVEL INICIO QUE VAI CONTROLAR O LAÇO 
while inicio:                                          # LAÇO QUE CONTROLA O CODIGO PRINCIPAL
    print ('='*30)
    print ('\nÓla.''\nQuantos candidatos gostaria de cadastrar:\n')      # OPÇÃO PARA INDICAR O NUMERO DE CANDIDATOS QUE DESEJA CADASTRAR
    numeroDeCandidatos =int(input())                                     # ENTRADA DO NUMERO DE CANDIDATOS

    for x in range  (0,numeroDeCandidatos,1):                            # LAÇO PARA CONTROLAR O NUMERO DE CADASTROS DE CANDIDATOS
        guardaNotas = ('eX_tX_pX_sX_')                                   # STRING QUE VAI GUARDAR AS NOTAS DOS CANDIDATOS
        print ('-'*30)                                                   # LINHA PAARA DEIXAR O PRINT BONITINHO
        print ('Nome do candidato numero  '+str(x+1)+':\n')              # PRINT PARA INICIAR O CADASTRO DOS CANDIDATOS
        nomeCandidato = input()                                          # VARIAVEL GUARDA NOME DO CANDIDATO
        listaCandidatos.append(nomeCandidato)                            # ADICIONA O NOME DO CANDIDATO EM UMA SUBLISTA
        
        for i in range (1,numProcessos,1):                               # LAÇO PARA CADASTRAR AS NOTAS DOS CANDIDATOS
            print ('-'*30)
            print ('\nNota de '+(processoSeletivo(i))+':')               # PRINT PARA SOLICITAR A ENTRADA DE NOTAS AO USUARIO 
            nota = input()                                               # SÃO SOLICITADAS AS NOTAS DE ACORDO COM O PROCESSO SELETIVO
            nota = validaNotasUsuario(nota)                              # CHAMADA A FUNÇÃO PARA VALIDAR A ENTRADA DO USUAARIO
            guardaNotas =  guardaNotas.replace('X',nota,1)               # VARIAVEL GUARDA AS NOTAS DENTRO DE UMA STRING
            
        listaCandidatos.append(guardaNotas)                              # SUBLISTA RECEBE A STRING ONDE ESTÃO GUARDADAS AS NOTAS
        listaPrincipal.append(listaCandidatos)                           # LISTA PRINCIPAL RECEBE A SUBLISTA COM OS DADOS DO CANDIDATO
        listaCandidatos=[]                                               # SUBLISTA ZERADA PARA O PROXIMO CADASTRO
        
    consulta =True                                                       # LAÇO PARA CONSULTAR E COLOCAR AS NOTAS MINIMAS
    while consulta:                                                      # LAÇO CONTROLADO PELA VARIAVEL BOLEANA CONSULTA
        print ('='*30)
        print( 'Por favor digite a nota mínima nos processos,''\npara que retorne os candidatos selecionados:\n')
        for i in range (1,numProcessos,1):                               # LAÇO CADASTRA EM UMA LISTA AS NOTAS MINIMAS EM CADA PROCESSO CELETIVO
            print ('-'*30)
            print ('\nNota de '+(processoSeletivo(i))+':')               # PRINT PARA SOLICITAR A NOTA EM CADA PROCESSO
            notaMin= input()                                             # VARIAVEL NOTAMIN GUARDA A NOTA COLOCADA PELO USUARIO
            notaMinima.append(validaNotasUsuario (notaMin))              # ENTRADA DO USUARIO E VALIDADA E GUARDADA EM UMA LISTA
            
        buscaCandidato (notaMinima, listaPrincipal)                      #CHAMA A FUNÇÃO BUSCA O CANDIDATO QUE ATENDE OS CRITÉRIOS 
        print ('='*30)
        print ('Gostaria de voltar a consultar candidatos ou cadastrar novos: \n1.Consultar\n2.Cadastrar\n3.Sair')
        opcaofinal = input()    
                                                                         # SOLICITA SE O USUARIO QUER SAIR, VOLTAR A CADASTRAR OU CONSULTAR
        while  not opcaofinal in ('1','2','3'):                          # TESTA A ENTRADO DO USUARIO E CONDICIONA A RESPOSTA
            print('\n Opção Invalida digite novamente:  \n1.Consultar\n2.Cadastrar\n3.Sair')
            opcaofinal =input()
        if opcaofinal == '1':                                            # DEIXA VAZIA A LISTA DA NOTA MINIMA PARA VOLTAR A CONSULTAR
            notaMinima = []
            consulta = True
        elif opcaofinal =='2':                                           # INICIO RECEBE TRUE  PARA VOLTAR A CADASTRAR CANDIDATOS
            notaMinima = []
            consulta =False
            inicio == True
        elif opcaofinal == '3':                                          # OPÇÃO SAIR 
            exit()
