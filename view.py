from controller import*

def func_geral():
    jogador={'nome':'','jogos':0,'vitorias':0}
    detalhes_grelha=inicia_dicionario()
    lista_jogadores=inicializar_lista()
    instrucao=''
    jogadores_em_jogo=inicializar_lista()
    aux_nome_jogador=' '
    aux_nome_jogador2=' '
    tam_lista_pecas_especiais=0
    s=[]
    w=0
    h=0
    n=0 
    tam_lista_pecas_especiais=0
    escolha=''
    aux_mat_grelha=[]
    i=0
    j=0
    Nome_ficheiro=''
    while True:
        
        instrucao=input('\n                                        >> Menu de instruções << '
                        '\n'
                        '\n                                         Registrar jogador (RJ)'
                        '\n                                         Remover jogador (EJ)'
                        '\n                                         Listar jogadores (LJ)'
                        '\n                                         Iniciar jogo (IJ)'
                        '\n                                         Detalhes de jogo (DJ)'
                        '\n                                         Desistir (D)'
                        '\n                                         Colocar peça (CP)'
                        '\n                                         Visualizar resultado (V)'
                        '\n                                         Gravar (G)'
                        '\n                                         Ler (L)'
                        '\n'
                        '\n                                         -> ')
        instrucao=instrucao.upper()                
        
        if instrucao=='RJ':
            jogador['nome']=str(input('\nEscreva o nome do jogador: '))    
            lista_jogadores=registrar_jogador_lista(lista_jogadores,jogador)
            

        elif instrucao=='EJ':
             aux_nome_jogador=input('Digite o nome do jogador quer remover: ')
             lista_jogadores=remover_jogador(lista_jogadores,aux_nome_jogador,jogadores_em_jogo)

        elif instrucao=='LJ':
             listar_jogadores(lista_jogadores)

        elif instrucao=='IJ':
            #detalhes_grelha
            aux_nome_jogador=input('\nDigite o nome do jogador 1: ')       
            aux_nome_jogador2=input('\nDigite o nome do jogador 2: ')
            print('\nATT: A ordem dos jogadores será organizada em função a ordem alfabética pelo programa!')
            w=int(input('\nIndique o comprimento da grelha em peças: '))
            h=int(input('\nIndique a altura da grelha em peças: '))
            print('\nATT: A sequência não pode ser maior que altura e comprimento!')
            n=int(input('\nIndique o número peças em linha para determinar a vitória (TamanhoSequência): '))
            #jogadores_em_jogo.clear()
            tam_lista_pecas_especiais=int(input('\nIndique o tamanho da peça especial: '))  
            aux=0
            for i in range(0,tam_lista_pecas_especiais):
                      aux=int(input('\nDigite uma peça(valor inteiro) que compõe a peça especial: '))
                      s.append(aux)         
           # if type(iniciar_jogo(w,h,n,aux_nome_jogador,aux_nome_jogador2,lista_jogadores,jogadores_em_jogo,s,detalhes_grelha))==int:
            #       break
            #else:    
            jogadores_em_jogo,detalhes_grelha=iniciar_jogo(w,h,n,aux_nome_jogador,aux_nome_jogador2,lista_jogadores,jogadores_em_jogo,s,detalhes_grelha)
            print('\nJogo iniciado entre', detalhes_grelha.get('jogador_1'), 'e',detalhes_grelha.get('jogador_2'),sep=' ', end='\n')
           
        
        elif instrucao=='DJ':
              detalhes_de_jogo(detalhes_grelha,s)
       
        elif instrucao=='D':
            
            aux_nome_jogador=input('\nDigite o nome do jogador 1 que quer desistir: ')
            escolha=input('\nSe quiser inserir outro jogador que quer deisitir. Digite SIM se quiser inserir outro jogador ou NAO se não quiser: ')
            escolha=escolha.upper()
            if escolha=='SIM': 
              aux_nome_jogador2=input('\nDigite o nome do jogador 2 que quer desistir: ')    
              detalhes_grelha,jogadores_em_jogo,lista_jogadores=Desistir_do_jogo(aux_nome_jogador,aux_nome_jogador2,lista_jogadores,jogadores_em_jogo,detalhes_grelha)
            elif escolha=='NAO':
                detalhes_grelha,jogadores_em_jogo,lista_jogadores=Desistir_do_jogo(aux_nome_jogador,aux_nome_jogador2,lista_jogadores,jogadores_em_jogo,detalhes_grelha)
            
            #A lista de jogadores em jogo agora está vazia e os detalhes dos jogadores precisam ser actualizasados na lista de reg
                        
            # Resestar o dicionario de detalhes 
            detalhes_grelha['comprimento']=0
            detalhes_grelha['altura']=0
            detalhes_grelha['sequencia_vitoria']=0
            detalhes_grelha['grelha']=inicializar_grelha(detalhes_grelha)
            detalhes_grelha['jogador_1']={}
            detalhes_grelha['jogador_2']={}                 
            detalhes_grelha['pecas_especiais_jgd_1']=[]
            detalhes_grelha['pecas_especiais_jgd_2']=[]

        elif instrucao=='CP':
             print('\nATT: Se digitar uma peça unitária deve teclar espaço uma vez para o sentido e para teclaa especial deve digitar E ou D! ')
             print('\n')
             aux_nome_jogador=input('\nDigite o nome do jogador 1 que quer colocar a peça: ')
             if verifica_jogador(lista_jogadores,aux_nome_jogador)==True:

               tam_peca=int(input('\nDigite o tamanho da peça a colocar na grelha: '))
               pos=int(input('\nDigite a posição que quer colocar a peça: '))
               sentid=input('\nSE quiser colocar a peça mais a esquerda digite E ou mais a direita digite D: ')
               sentid=sentid.upper()
               detalhes_grelha['grelha'],jogadores_em_jogo,detalhes_grelha,lista_jogadores=colocacao_peca_no_jogo(aux_nome_jogador,tam_peca,pos,sentid,detalhes_grelha,jogadores_em_jogo,detalhes_grelha.get('grelha'),lista_jogadores)
             
               aux_nome_jogador_2=input('\nDigite o nome do jogador 2 que quer colocar a peça: ')
             
             elif aux_nome_jogador_2!=aux_nome_jogador and verifica_jogador(lista_jogadores,aux_nome_jogador_2)==True:
                tam_peca=int(input('\nDigite o tamanho da peça a colocar na grelha: '))
                pos=int(input('\Digite a posição que quer colocar a peça: '))
                sentid=input('\nSE quiser colocar a peça mais a esquerda digite E ou mais a direita digite D: ')
                sentid=sentid.upper()
                detalhes_grelha['grelha'],jogadores_em_jogo,detalhes_grelha,lista_jogadores=colocacao_peca_no_jogo(aux_nome_jogador_2,tam_peca,pos,sentid,detalhes_grelha,jogadores_em_jogo,detalhes_grelha.get('grelha'),lista_jogadores)
             else:
                continue                
            
        
        elif instrucao=='V':
            mostra_resultado(detalhes_grelha.get('grelha'),detalhes_grelha.copy(),jogadores_em_jogo.copy())
        
        elif instrucao=='G':

             Nome_ficheiro=str(input('\nEscreva o nome de ficheiro de gravação: '))
             Nome_ficheiro=Nome_ficheiro+'.pkl'
             print('\nATT: foi adicionada uma extensão ao nome do ficheiro .pkl ')
             chama_gravacao_file_do_model(Nome_ficheiro,lista_jogadores,detalhes_grelha,detalhes_grelha.get('grelha'),jogadores_em_jogo)
        
        elif instrucao=='L':
            Nome_ficheiro=str(input('\nEscreva o nome do que usou para gravar o ficheiro: '))
            Nome_ficheiro=Nome_ficheiro+'.pkl'
            print('\nATT: foi adicionada uma extensão ao nome do ficheiro .pkl ')
            lista_jogadores,detalhes_grelha,detalhes_grelha['grelha'],jogadores_em_jogo= chama_leitura_file_do_model(Nome_ficheiro,lista_jogadores,detalhes_grelha,detalhes_grelha.get('grelha'),jogadores_em_jogo)                 
        
        else:
            print('Instrução inválida.')
       
        ###########################################################################

        opc=int(input('Digite 0-para fechar programa ou 1-para voltar ao menu de instruções'
        '\n-> '))

        if opc==0:
            print('Fim.')
            break

        elif opc==1:
            continue

        else:
            print('Opção inválida!')
        
        ###########################################################################

    return 