
def processoSeletivo(opcao):
    if opcao == 1:
         return ('Entrevista')
    elif opcao == 2 :
        return  ('Teste Teórico')
    elif opcao == 3:
        return ('Teste Prático')
    elif opcao == 4:
        return  ('Avaliação Soft Skill')


listaPrincipal = []
listaCandidatos =[]
numProcessos = 5

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


print (listaPrincipal)
#e = 5
#c= 8
#d= 3
#candidato=''
#contador =0
#for x in range (0,len(lista),1):
     #palavra = lista[x][1]
     #if int(palavra[1]) >=e:
         #if int(palavra[4])>=c:
             #if int(palavra[7])>=d:
                # candidato =candidato + ' ' +lista[x][0]
                 #contador = contador + 1
     #elif contador==0:
         #candidato = ('nao ha candidato')
    
#print (candidato)
