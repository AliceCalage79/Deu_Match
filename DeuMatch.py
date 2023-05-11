
def processoSeletivo(opcao): #def para licalizar qual o processo seletivo
    if opcao == 1:
         return ('Entrevista')
    elif opcao == 2 :
        return  ('Teste Teórico')
    elif opcao == 3:
        return ('Teste Prático')
    elif opcao == 4:
        return  ('Avaliação Soft Skill')
def buscaCandidato (notaMinima, listaPrincipal): 
 candidato=''
 contador = 0
 for x in range (0,len(listaPrincipal),1):
     palavra = listaPrincipal[x][1]
     if int(palavra[1]) >= notaMinima[0]:
         if int(palavra[4])>= notaMinima[1]:
             if int(palavra[7])>= notaMinima[2]:
                 if int(palavra[10])>= notaMinima[3]:
                     candidato =candidato + ' ' +listaPrincipal[x][0]+ listaPrincipal[x][1]
                     contador = contador + 1
 if contador == 0:
    print ('não ha candidato')
 else:
    print ('======================================================')
    print ('Os selecionados são:')
    print (candidato)



listaPrincipal = []
listaCandidatos =[]
numProcessos = 5
notaMinima =[]

print ('Quantos candidatos gostaria de cadastrar:')
numeroDeCandidatos =int(input())

for x in range  (0,numeroDeCandidatos,1):
    guardaNotas = ('eX_tX_pX_sX_')
    print ('Nome do candidato:')
    nomeCandidato = input()
    listaCandidatos.append(nomeCandidato)
    for i in range (1,numProcessos,1):
        print ('Nota de '+(processoSeletivo(i))+'')
        nota = input()
        guardaNotas =  guardaNotas.replace('X',nota,1)
    listaCandidatos.append(guardaNotas)
    listaPrincipal.append(listaCandidatos)
    listaCandidatos=[]



print( 'Por favor digite a nota mínima nos processos, para que retorne os candidatos selecionados:')
for i in range (1,numProcessos,1):
      print ('Nota de '+(processoSeletivo(i))+'')
      nota= int(input())
      notaMinima.append(nota)
buscaCandidato (notaMinima, listaPrincipal)
