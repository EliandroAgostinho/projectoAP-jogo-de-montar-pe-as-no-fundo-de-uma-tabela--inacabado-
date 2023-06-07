import pickle


def garavar_file(file,lista_jogadores,dtl_jogo,matriz_grelha,j_e_jogo):
    try:
           arq = open(file,"wb") 
           pickle.dump(lista_jogadores,arq)
           pickle.dump(dtl_jogo,arq)
           pickle.dump(matriz_grelha,arq)
           pickle.dump(j_e_jogo,arq)
       

    except Exception: print('\nOcorreu um erro na gravação. ')

    finally:
         arq.close()
         print('\nJogo gravado. ')
    return file

##########################################################################################

def ler_file(file,lista_jogadores,dtl_jogo,matriz_grelha,j_e_jogo):
    
    lista_jogadores=None
    dtl_jogo=None
    matriz_grelha=None
    j_e_jogo=None
    
    try:
        with open(file,"rb") as arq:  
            lista_jogadores=pickle.load(arq)
            dtl_jogo=pickle.load(arq)
            matriz_grelha=pickle.load(arq)
            j_e_jogo=pickle.load(arq)

    except Exception: print('\nOcorreu um erro no carregamento. ') 

    finally:
        
        print('\nJogo carregado. ')

    return lista_jogadores,dtl_jogo,matriz_grelha,j_e_jogo