from model import *

def inicializar_lista():
    lista=list()
    return lista
#################################################################


def inicia_dicionario():
    detalhes_de_jogo={'comprimento':0,
                         'altura':0,
                         'sequencia_vitoria':0,
                         'grelha':0,
                         'jogador_1':{},
                         'jogador_2':{},
                         'pecas_especiais_jgd_1':[],
                         'pecas_especiais_jgd_2':[]}
    return detalhes_de_jogo
#################################################################
def registrar_jogador_lista(lista,jgd): 
    if verifica_jogador(lista,jgd.get('nome'))==True:
        print('\nJogador existente.')
    else:
        lista.append(jgd.copy())
        print('\nJogador  registado com sucesso.')
    return lista    
#################################################################

def verifica_jogador(lista,jgd):
    for aux in lista:
        if aux.get('nome')==jgd:
            return True
    return False    
####################################################################


def remover_jogador(lista,nome_jgd,j_e_jogo):
    
        if verifica_jogador(j_e_jogo,nome_jgd)==True: 
            print('\nJogador participa no jogo em curso. Não pode ser removido de momento!  ')
            return lista
        elif verifica_jogador(j_e_jogo,nome_jgd)==False:
             for jogador in lista:
                if jogador.get('nome')==nome_jgd: 
                   lista.remove(jogador)
                   print('\nJogador removido com sucesso. ')
                   return lista 
############################################################################

def listar_jogadores(lista):
    if len(lista)==0:
        print('\nNão existem jogadores registados. ')
    for i in range(len(lista)):
        for j in range(0,len(lista)-i-1):
            if lista[j]['nome']>lista[j+1]['nome']:
                tem=lista[j+1]
                lista[j+1]=lista[j]
                lista[j]=tem
    for jogador in lista:
        for chave,valor in jogador.items():
            print(chave,':',valor)
    print('\n')                   
                     
############################################################################

def sort_nome(lista):
    for i in range(len(lista)):
        for j in range(0,len(lista)-i-1):
            if lista[j]['nome']>lista[j+1]['nome']:
                tem=lista[j+1]
                lista[j+1]=lista[j]
                lista[j]=tem
    return lista            

#############################################################################


def iniciar_jogo(w,h,n,jogador1,jogador2,lista,j_e_jogo,S_lista_pecas_especiais,dtl_jogo):
        
    if verifica_jogador(lista,jogador1)==False or verifica_jogador(lista,jogador2)==False:
        print('\nJogador não registado. ') 
        return 1

    elif bool(dtl_jogo.get('jogador_1'))==True:   
        print('\nExiste um jogo em curso. ')         
        return 1


    elif (w<0) or (w/2>h) or (w<h): 
        print('\nDimensões de grelha inválidas. ')   
        return 1
    elif n>w:
        print('\nTamanho da sequência inválido. ')
             
    for i in S_lista_pecas_especiais:
            if i>=n:
               print('\nDimensões de peças especiais inválidas. ')
               return 1
    else:
        S_lista_pecas_especiais_aux=S_lista_pecas_especiais.copy()        
    
        

        for aux in lista:
            if aux.get('nome')==jogador1:
                j_e_jogo.append(aux.copy())
        

        for el in lista:    
            if el.get('nome')==jogador2: 
                j_e_jogo.append(el.copy())
        #print(j_e_jogo)
        j_e_jogo=sort_nome(j_e_jogo)#Organizar em função a ordem alfabética
        
        
        dtl_jogo['comprimento']=w
        dtl_jogo['altura']=h
        dtl_jogo['sequencia_vitoria']=n
        dtl_jogo['grelha']=inicializar_grelha(dtl_jogo)
        dtl_jogo['jogador_1']=j_e_jogo[0]
        dtl_jogo['jogador_2']=j_e_jogo[1]
        dtl_jogo['pecas_especiais_jgd_1']=S_lista_pecas_especiais.copy()
        dtl_jogo['pecas_especiais_jgd_2']=S_lista_pecas_especiais_aux.copy()
        return j_e_jogo,dtl_jogo
#########################################################################################################

def inicializar_grelha(dicionario):
    matriz_grelha=[]
    comprimento=dicionario.get('comprimento')
    altura=dicionario.get('altura')
    #Preencher uma matriz com 0. A matriz será do tamanho que o utilizador quiser
    matriz_grelha=[[0 for i in range(comprimento)] for i in range(altura)]
    return matriz_grelha

##########################################################################################################

def detalhes_de_jogo(dicionario_de_detalhes,S_lista_pecas_especiais):
    if dicionario_de_detalhes.get('jogador_1')==' ' or dicionario_de_detalhes.get('jogador_2')==' ':
       print('\nNão existe jogo em curso. ')
    else:
       detalhe_jogador_1=dict()
       detalhe_jogador_2=dict()
       for i in S_lista_pecas_especiais:
           detalhe_jogador_1={i:dicionario_de_detalhes['pecas_especiais_jgd_1'].count(i)}
       for j in S_lista_pecas_especiais:
           detalhe_jogador_2={j:dicionario_de_detalhes['pecas_especiais_jgd_2'].count(j)}         
       print('\n')
       print('Comprimento: ',dicionario_de_detalhes.get('comprimento'),' Altura: ',dicionario_de_detalhes.get('altura'))
       print('\nJogador 1: ',dicionario_de_detalhes.get('jogador_1'))
       for chave in detalhe_jogador_1.keys():
           print(chave,detalhe_jogador_1.get(chave))
       print('\nJogador 2: ',dicionario_de_detalhes.get('jogador_2'))
       for shave in detalhe_jogador_2.keys():
           print(shave,detalhe_jogador_2.get(shave)) 

#################################################################################################################################                

def Desistir_do_jogo(nome_jogador_1,nome_jogador_2,lista,j_e_jogo,dicionario_de_detalhes):
    if verifica_jogador(lista,nome_jogador_1)==False:# or (verifica_jogador(lista,nome_jogador_2)==False and nome_jogador_2!=' '):
        print('\nJogador não registado. ') 
        return dicionario_de_detalhes,j_e_jogo,lista
    elif dicionario_de_detalhes.get('jogador_1')==' ' or dicionario_de_detalhes.get('jogador_2')==' ':       
        print('\nNão existe jogo em curso. ')
        return dicionario_de_detalhes,j_e_jogo,lista
    elif verifica_jogador(j_e_jogo,nome_jogador_1)==False:
        print('\nJogador não participa no jogo em curso.')
        return dicionario_de_detalhes,j_e_jogo,lista
    elif nome_jogador_2!=' ':
        if verifica_jogador(j_e_jogo,nome_jogador_2)==False:
            print('\nJogador não participa no jogo em curso.')
            return dicionario_de_detalhes,j_e_jogo,lista
        else:#Caso os 2 jogadores desistam incrementa um jogo que jogado
            jogador_1='jogador_1'
            jogador_2='jogador_2'
            if jogador_1 in dicionario_de_detalhes:
                # Se o jogador 1 desistir, então o jogador 1 recebe + 1 jogo jogado e o jogador 2 recebe 1 jogo jogado e 1a vitória 
                 
                 detail=dicionario_de_detalhes[jogador_1] 
                 if nome_jogador_1 == detail.get('nome'): 
                
                     detail['jogos']=detail.get('jogos')+1
                     lista,detail=actualiza_jogos_vitorias_nos_registros(lista,detail)
                     dicionario_de_detalhes.update(detail)

                # else:# nome_jogador_2 == detail.get('nome'):
                     detail=dicionario_de_detalhes[jogador_2]  
                     detail['jogos']=detail.get('jogos')+1
                     detail['vitorias']=detail.get('vitorias')+1
                     lista,detail=actualiza_jogos_vitorias_nos_registros(lista,detail)
                     dicionario_de_detalhes.update(detail)      

            elif jogador_2 in dicionario_de_detalhes:
                # Se o jogador 2 desistir, então o jogador 2 recebe 1 jogo jogado e o jogador 1 recebe 1 jogo jogado e 1a vitória
                detail=dicionario_de_detalhes[jogador_2]           
                if nome_jogador_2 == detail.get('nome'):
                    
                    detail['jogos']=detail.get('jogos')+1
                    lista,detail=actualiza_jogos_vitorias_nos_registros(lista,detail)
                    dicionario_de_detalhes.update(detail)
                          
                #else: #nome_jogador_1 == detail.get('nome'):
                    detail=dicionario_de_detalhes[jogador_1]
                    detail['jogos']=detail.get('jogos')+1
                    detail['vitorias']=detail.get('vitorias')+1
                    lista,detail=actualiza_jogos_vitorias_nos_registros(lista,detail)
                    dicionario_de_detalhes.update(detail)     
                 

            lista=sort_nome(lista)
            print('\nDesistência com sucesso. Jogo terminado.')
            j_e_jogo.clear()
            return dicionario_de_detalhes,j_e_jogo,lista
            
    
    else:# Caso um dos 2 desista incrementa 1 vitoria e um jogo jogado para o vencedor e apenas incrementa um jogo jogado para o perdedor  
        jogador_1='jogador_1'
        jogador_2='jogador_2'
         
        
        if (jogador_1 in dicionario_de_detalhes) and (jogador_2 in dicionario_de_detalhes):
                    detail=dicionario_de_detalhes[jogador_1]
                    
                    detail['jogos']=detail.get('jogos')+1
                    lista,detail=actualiza_jogos_vitorias_nos_registros(lista,detail)
                    dicionario_de_detalhes.update(detail)

        #elif jogador_2 in dicionario_de_detalhes:                                      
                    detail=dicionario_de_detalhes[jogador_2]
                    
                    detail['jogos']=detail.get('jogos')+1
                    lista,detail=actualiza_jogos_vitorias_nos_registros(lista,detail)
                    dicionario_de_detalhes.update(detail)


        lista=sort_nome(lista)

        print('\nDesistência com sucesso. Jogo terminado.')
        j_e_jogo.clear()
        return dicionario_de_detalhes,j_e_jogo,lista

##################################################################################################################################

def colocacao_peca_no_jogo(nome_jogador,tamanho_peca,posicao,sentido,dicionario_de_detalhes,j_e_jogo,mat_grelha,lista_registro):
    if bool(dicionario_de_detalhes.get('jogador_1'))==False:
        print('\nNão existe jogo em curso. ')     
        return mat_grelha,j_e_jogo,dicionario_de_detalhes,lista_registro
    
    elif bool(dicionario_de_detalhes.get('jogador_2'))==False:
         print('\nNão existe jogo em curso. ')
         return mat_grelha,j_e_jogo,dicionario_de_detalhes,lista_registro
    
    elif verifica_jogador(j_e_jogo,nome_jogador)==False:
         print('\nJogador não participa no jogo em curso. ')
         return mat_grelha,j_e_jogo,dicionario_de_detalhes,lista_registro

    elif tamanho_peca >1:
        jogador_1='jogador_1'
        jogador_2='jogador_2'

        if jogador_1 in dicionario_de_detalhes:
            detalhe=dicionario_de_detalhes[jogador_1]
                
            if nome_jogador==detalhe.get('nome'):
                dicionario_de_detalhes.update(detalhe) 
                if tamanho_peca not in dicionario_de_detalhes['pecas_especiais_jgd_1']:
                    print('\nTmanho de peça não disponível. ')
                        
                elif bool(sentido)==True:
                    #if type(colocacao_peca_especial(nome_jogador,tamanho_peca,posicao,sentido,dicionario_de_detalhes,j_e_jogo,mat_grelha,lista_registro))!=bool:
                        mat_grelha,dicionario_de_detalhes,j_e_jogo,lista_registro=colocacao_peca_especial(nome_jogador,tamanho_peca,posicao,sentido,dicionario_de_detalhes,j_e_jogo,mat_grelha,lista_registro)
                        #return mat_grelha,j_e_jogo,dicionario_de_detalhes,lista_registro

        elif jogador_2 in dicionario_de_detalhes:
            
            detalhe=dicionario_de_detalhes[jogador_2]
            if nome_jogador==detalhe.get('nome'):

                dicionario_de_detalhes.update(detalhe)
                if tamanho_peca not in dicionario_de_detalhes['pecas_especiais_jgd_2']:
                    print('\nTmanho de peça não disponível. ')
                
                elif bool(sentido)==True:
                    #if type(colocacao_peca_especial(nome_jogador,tamanho_peca,posicao,sentido,dicionario_de_detalhes,j_e_jogo,mat_grelha,lista_registro))!=bool:
                        mat_grelha,dicionario_de_detalhes,j_e_jogo,lista_registro=colocacao_peca_especial(nome_jogador,tamanho_peca,posicao,sentido,dicionario_de_detalhes,j_e_jogo,mat_grelha,lista_registro)
                        #return mat_grelha,j_e_jogo,dicionario_de_detalhes,lista_registro

    elif posicao > len(mat_grelha[0]):
        print('\nPosição irregular. ') 
    
    elif bool(sentido)==False:
        #if type(colocacao_peca_unitaria(nome_jogador,tamanho_peca,posicao,sentido,dicionario_de_detalhes,j_e_jogo,mat_grelha))!=bool:
            mat_grelha,j_e_jogo,dicionario_de_detalhes,lista_registro=colocacao_peca_unitaria(nome_jogador,tamanho_peca,posicao,sentido,dicionario_de_detalhes,j_e_jogo,mat_grelha,lista_registro) 
            #return mat_grelha,j_e_jogo,dicionario_de_detalhes,lista_registro


    return mat_grelha,j_e_jogo,dicionario_de_detalhes,lista_registro           
#############################################################################################################################################


def colocacao_peca_unitaria(nome_jogador,posicao,dicionario_de_detalhes,j_e_jogo,mat_grelha,lista_registro):
    sequencia_vitoria=dicionario_de_detalhes.get('sequencia_vitoria')
    sequencia=0
    altura=len(mat_grelha)-1
    jogador_1='jogador_1'
    jogador_2='jogador_2'
    detalhe=dict()

    while True:
        if altura<0:
            print('\nPosição irregular. ')
            return mat_grelha
    
        elif (mat_grelha[altura][posicao]==1) or (mat_grelha[altura][posicao]==2):
            altura-=1 
            continue
    
        elif mat_grelha[altura][posicao]==0:
            if jogador_1 in dicionario_de_detalhes:
                detalhe=dicionario_de_detalhes[jogador_1]
                
                if nome_jogador==detalhe.get('nome'):   # 
                    mat_grelha[altura][posicao]=1
                    dicionario_de_detalhes.update(detalhe)
                    break
             
            elif jogador_2 in dicionario_de_detalhes:
                detalhe=dicionario_de_detalhes[jogador_2]
                
                if nome_jogador==detalhe.get('nome'):
                    mat_grelha[altura][posicao]=2
                    dicionario_de_detalhes.update(detalhe)
                    break

    for i in range(len(mat_grelha)):
        for j in range(len(mat_grelha[i])-1):
            if mat_grelha[i][j]==0:
                sequencia=0
                continue
            elif sequencia==sequencia_vitoria:
                print('\nSequência conseguida. Jogo terminado. ')
                dicionario_de_detalhes,j_e_jogo,lista_registro=definir_vencedor_perdedor(nome_jogador,dicionario_de_detalhes,j_e_jogo,lista_registro)
                return True
            elif mat_grelha[i][j]==mat_grelha[i][j+1]:
                sequencia+=1
    
    for i in range(len(mat_grelha)-1):   
       if (mat_grelha[i][j]==0):
          sequencia=0
          continue
       
       elif sequencia==sequencia_vitoria:
          print('\nSequência conseguida. Jogo terminado. ')
          dicionario_de_detalhes,j_e_jogo,lista_registro=definir_vencedor_perdedor(nome_jogador,dicionario_de_detalhes,j_e_jogo,lista_registro)
          return True

       if mat_grelha[i][posicao]==mat_grelha[i+1][posicao]:
         sequencia+=1   

    print('\nPeça colocada. ')
    return mat_grelha,j_e_jogo,dicionario_de_detalhes,lista_registro            


    

####################################################################################################################




def definir_vencedor_perdedor(nome_jogador,dicionario_de_detalhes,j_e_jogo,lista_registro):
    
    jogador1='jogador_1'
    jogador2='jogador_2'

    if jogador1 in dicionario_de_detalhes:
        detalhe=dicionario_de_detalhes[jogador1]
        if detalhe.get('nome')==nome_jogador:
            
            detalhe['jogos']=detalhe.get('jogos')+1
            detalhe['vitorias']=detalhe.get('vitorias')+1
            lista_registro,detalhe=actualiza_jogos_vitorias_nos_registros(lista_registro,detalhe)
            dicionario_de_detalhes.update(detalhe)

        elif jogador2 in dicionario_de_detalhes:
            detalhe=dicionario_de_detalhes[jogador2]
            
            detalhe['jogos']=detalhe.get('jogos')+1
            lista_registro,detalhe=actualiza_jogos_vitorias_nos_registros(lista_registro,detalhe)
            dicionario_de_detalhes.update(detalhe)      
    
    elif jogador2 in dicionario_de_detalhes:
         detalhe=dicionario_de_detalhes[jogador2]
        
         if detalhe.get('nome') == nome_jogador:
            
            detalhe['jogos']=detalhe.get('jogos')+1
            detalhe['vitorias']=detalhe.get('vitorias')+1
            lista_registro,detalhe=actualiza_jogos_vitorias_nos_registros(lista_registro,detalhe)
            dicionario_de_detalhes.update(detalhe)
                                        
         elif jogador1 in dicionario_de_detalhes:
               
               detalhe['jogos']=detalhe.get('jogos')+1
               lista_registro,detalhe=actualiza_jogos_vitorias_nos_registros(lista_registro,detalhe)
               dicionario_de_detalhes.update(detalhe)

    
   
    lista_registro=sort_nome(lista_registro)

    j_e_jogo.clear()
    
    return dicionario_de_detalhes,j_e_jogo,lista_registro   

#####################################################################################################



def colocacao_peca_especial(nome_jogador,tam_pec,posicao,sentido,dicionario_de_detalhes,jogadores_jogo,mat_grelha,lista_registro):
    tamanho_pec_especial=tam_pec
    sequencia_vitoria=dicionario_de_detalhes.get('sequencia_vitoria')
    sequencia=0
    altura=0
    jogador_1='jogador_1'
    jogador_2='jogador_2'
    pecas_especiais_jgd_2=list()
    pecas_especiais_jgd_1=list()

    if sentido=='E':
        P_inicial=posicao
        P_final=P_inicial-tamanho_pec_especial
        if P_final<0:
            print('\nPosição irregular. ')
            return mat_grelha
        else:
            for i in range(tamanho_pec_especial):
                altura=len(mat_grelha)-1
                while True:
                    if altura < 0:
                        print('\nPosição irreguar. ')
                        return True
                    elif mat_grelha[altura][posicao]==1 or mat_grelha[altura][posicao]==2:       
                         altura-=1
                         pass
                    elif mat_grelha[altura][posicao]==0:     
                       
                        if jogador_1 in dicionario_de_detalhes: 
                            detalhe=dicionario_de_detalhes[jogador_1]
                            if detalhe.get('nome') == nome_jogador:
                               mat_grelha[altura][posicao]=1
                               #
                               dicionario_de_detalhes.update(detalhe)
                               break
                            
                        elif jogador_2 in dicionario_de_detalhes:
                              detalhe=dicionario_de_detalhes[jogador_2]
                              mat_grelha[altura][posicao]=2
                              #
                              dicionario_de_detalhes.update(detalhe)
                              break
                posicao-=1            

        for i in range(len(mat_grelha)):
            for j in range(len(mat_grelha[i])-1):
                if mat_grelha[i][j]==0:
                   sequencia=0
                   continue
                elif sequencia==sequencia_vitoria:
                    print('\nSequência conseguida. Jogo terminado. ')
                    dicionario_de_detalhes,jogadores_jogo,lista_registro=definir_vencedor_perdedor(nome_jogador,dicionario_de_detalhes,jogadores_jogo,lista_registro)
                    return True
                elif mat_grelha[i][j]==mat_grelha[i][j+1]:
                    sequencia+=1
        for i in range(len(mat_grelha)-1):
            if mat_grelha[i][posicao]==0:    
               sequencia=0
               continue
            elif sequencia==sequencia_vitoria:
                print('\nSequência conseguida. Jogo terminado. ')
                dicionario_de_detalhes,jogadores_jogo,lista_registro=definir_vencedor_perdedor(nome_jogador,dicionario_de_detalhes,jogadores_jogo,lista_registro)
                
                return True
            if mat_grelha[i][posicao]==mat_grelha[i+1][posicao]:
                sequencia+=1
        print('\nPeça colocada. ')

        if jogador_2 in dicionario_de_detalhes:
            detalhe=dicionario_de_detalhes[jogador_2]
            if detalhe.get('nome') == nome_jogador:
                 pecas_especiais_jgd_2=dicionario_de_detalhes['pecas_especiais_jgd_2']
                 pecas_especiais_jgd_2.remove(tamanho_pec_especial)                
                 dicionario_de_detalhes['pecas_especiais_jgd_2']=pecas_especiais_jgd_2                 
                 dicionario_de_detalhes.update(detalhe)
                 return mat_grelha,dicionario_de_detalhes,jogadores_jogo,lista_registro
      
        elif jogador_1 in dicionario_de_detalhes:
            detalhe=dicionario_de_detalhes[jogador_1]
            if detalhe.get('nome') == nome_jogador:
                pecas_especiais_jgd_1=dicionario_de_detalhes['pecas_especiais_jgd_1']
                pecas_especiais_jgd_1.remove(tamanho_pec_especial)
                dicionario_de_detalhes['pecas_especiais_jgd_1']=pecas_especiais_jgd_1
                dicionario_de_detalhes.update(detalhe)
                return mat_grelha,dicionario_de_detalhes,jogadores_jogo,lista_registro    
    
    if sentido=='D':
        P_inicial=posicao
        P_final=P_inicial+tamanho_pec_especial
        if P_final>len(mat_grelha[0]):
            print('\nPosição irregular. ')
            return mat_grelha
        else:
            for i in range(tamanho_pec_especial):
                altura=len(mat_grelha)-1
                while True:
                    if altura<0:
                        print('\nPosição irregular. ')
                        return True
                    elif mat_grelha[altura][posicao]==1 or mat_grelha[altura][posicao]==2:
                        altura-=1
                        continue
                    elif mat_grelha[altura][posicao]==0:          
                         
                         if jogador_1 in dicionario_de_detalhes:
                            detalhe=dicionario_de_detalhes[jogador_1]
                            if detalhe.get('nome')==nome_jogador:
                                dicionario_de_detalhes.update(detalhe)
                                mat_grelha[altura][posicao]=1
                                break

                         elif jogador_2 in dicionario_de_detalhes:
                                detalhe=dicionario_de_detalhes[jogador_2]
                                if detalhe.get('nome')==nome_jogador:
                                    dicionario_de_detalhes.update(detalhe)
                                    mat_grelha[altura][posicao]=2
                                    break
                posicao+=1

        for i in range(len(mat_grelha)):
            for j in range(len(mat_grelha[i])-1):
                if mat_grelha[i][j]==0:
                    sequencia=0
                    continue
                elif sequencia==sequencia_vitoria:
                    print('\nSequência conseguida. Jogo terminado.')
                    dicionario_de_detalhes,jogadores_jogo,lista_registro=definir_vencedor_perdedor(nome_jogador,dicionario_de_detalhes,jogadores_jogo,lista_registro)
                    return True
                elif mat_grelha[i][j]==mat_grelha[i][j+1]:
                     sequencia=0
                     continue
                elif sequencia==sequencia_vitoria:
                    print('\nSequência conseguida. Jogo terminado. ')        
                    dicionario_de_detalhes,jogadores_jogo,lista_registro=definir_vencedor_perdedor(nome_jogador,dicionario_de_detalhes,jogadores_jogo,lista_registro)
                    return True
                if mat_grelha[i][posicao]==mat_grelha[i+1][posicao]:
                    sequencia+=1
        for i in range(len(mat_grelha)-1):
            if mat_grelha[i][posicao]==0:
                sequencia=0
                continue
            elif sequencia==sequencia_vitoria:
                print('\nSequência conseguida. Jogo terminado.')                  
                dicionario_de_detalhes,jogadores_jogo,lista_registro=definir_vencedor_perdedor(nome_jogador,dicionario_de_detalhes,jogadores_jogo,lista_registro)
                return True
            if mat_grelha[i][posicao]==mat_grelha[i+1][posicao]:
                sequencia+=1
        print('\nPeça colocada. ') 
        if jogador_2 in dicionario_de_detalhes:
            detalhe=dicionario_de_detalhes[jogador_2] 
            
            if detalhe.get('nome')== nome_jogador:
                dicionario_de_detalhes.update(detalhe)                   
                pecas_especiais_jgd_2=dicionario_de_detalhes['pecas_especiais_jgd_2']
                pecas_especiais_jgd_2.remove(tamanho_pec_especial)
                dicionario_de_detalhes['pecas_especiais_jgd_2']=pecas_especiais_jgd_2
                return mat_grelha,dicionario_de_detalhes,jogadores_jogo,lista_registro
            
        elif jogador_1 in dicionario_de_detalhes:
            detalhe=dicionario_de_detalhes[jogador_1]
            if detalhe.get('nome')==nome_jogador:   
                 pecas_especiais_jgd_1=dicionario_de_detalhes['pecas_especiais_jgd_1']
                 pecas_especiais_jgd_1.remove(tamanho_pec_especial)
                 dicionario_de_detalhes['pecas_especiais_jgd_1']=pecas_especiais_jgd_1
                 dicionario_de_detalhes.update(detalhe)
                 return mat_grelha,dicionario_de_detalhes,jogadores_jogo,lista_registro
        
        return mat_grelha,dicionario_de_detalhes,jogadores_jogo,lista_registro                              

##############################################################################################################################################################                
                

                
def mostra_resultado(matriz_grelha,dicionario_de_detalhes,jogadores_jogo):
     
    joggador=''
    if (bool(dicionario_de_detalhes.get('jogador_1'))==False and bool(dicionario_de_detalhes.get('jogador_2'))==False) or bool(jogadores_jogo)==False:
        print('\nNão existe jogo em curso. ')
    else:
        jogador_1='jogador_1'
        jogador_2='jogador_2'
        aux_jogador_1=dict
        aux_jogador_2=dict
       
        for i in range(dicionario_de_detalhes.get('comprimento')):
            for j in range(dicionario_de_detalhes.get('altura')):
                if matriz_grelha[i][j]==1:
                    if jogador_1 in dicionario_de_detalhes:
                        aux_jogador_1=dicionario_de_detalhes[jogador_1]          
                        joggador=aux_jogador_1.get('nome')

                elif matriz_grelha[i][j]==2:                 
                     if jogador_2 in dicionario_de_detalhes:
                        aux_jogador_2=dicionario_de_detalhes[jogador_2]  
                        joggador=aux_jogador_2.get('nome')
                
                elif matriz_grelha[i][j]==0:               
                     joggador='vazio'
                print('Posição ',i+1,j+1,joggador,sep=" ")
        print('\n')        
        for l in range(dicionario_de_detalhes.get('comprimento')):
        
            for c in range(dicionario_de_detalhes.get('altura')):
                
                print(f'[{matriz_grelha[l][c]}]', end='')
            print() 
        print('\n')       

###################################################################################################################################

def actualiza_jogos_vitorias_nos_registros(lista,dicionario_jogador):
    for jogador in lista:
        if jogador.get('nome')==dicionario_jogador.get('nome'):
            lista.remove(jogador)
            lista.append(dicionario_jogador.copy())
    return lista,dicionario_jogador        


def chama_gravacao_file_do_model(Nome_file,lista_registro,dicionario_de_detalhes,mat_grelha,jogadores_em_jogo):
    
    Nome_file=garavar_file(Nome_file,lista_registro,dicionario_de_detalhes,mat_grelha,jogadores_em_jogo)

    

def chama_leitura_file_do_model(Nome_file,lista_registro,dicionario_de_detalhes,mat_grelha,jogadores_em_jogo):

    lista_registro,dicionario_de_detalhes,mat_grelha,jogadores_em_jogo =ler_file(Nome_file,lista_registro,dicionario_de_detalhes,mat_grelha,jogadores_em_jogo)
    

    return lista_registro,dicionario_de_detalhes,mat_grelha,jogadores_em_jogo     