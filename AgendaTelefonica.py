def mostraLinhasEmensagens(msg):
    print()
    print("*"*50)
    print(msg)
    print("*" * 50)
    print()


def armazenaValoresInformadosPeloUsuarioNoVetor(vetor):
    vetor.append(str(input("NOME      : ")))
    vetor.append(int(input("TELEFONE  : ")))
    print("|*************************************************|")
    print()
    return vetor




matriz = []
vetor = []
continuar = True
codigo = 0
codigo2 = 0


while True:
    print("|**************************************|")
    print("|>>     MINHA AGENDA DE CONTATOS     <<|")
    print("|**************************************|")
    print("|>  1 - Cadastrar  novo contato       <|")
    print("|>  2 - Alterar  contato              <|")
    print("|>  3 - Excluir  contato              <|")
    print("|>  4 - Listar todos os contatos      <|")
    print("|>  5 - Listar contato por código     <|")
    print("|>  6 - Listar contatos por nome      <|")
    print("|>  7 - Sair                          <|")
    print("|**************************************|")
    print()
    print("|*************************************************|")
    opcao = int(input(">>>>>>>>   INFORME A OPÇÃO DESEJADA   : "))
    print("|*************************************************|")
    print()

    if opcao == 1:
        if len(matriz) < 11 :
            mostraLinhasEmensagens("|>>>>     CADASTRAR CONTATOS        <<<<|")
            print("|*************************************************|")
            codigo = (int(input("CODIGO    : ")))
            if len(matriz) == 0:
                vetor.append(codigo)
                armazenaValoresInformadosPeloUsuarioNoVetor(vetor)
                matriz.append(vetor)
                vetor = []
                mostraLinhasEmensagens("|>>>  CONTATO CADASTRADO COM SUCESSO  <<<|")
            else:
                jaEmUso = 0
                for l in range (len(matriz)):
                    if codigo == matriz[l][0]:
                        jaEmUso += 1

                if jaEmUso >= 1 :

                    mostraLinhasEmensagens("|>>>>>>>> CODIGO INFORMADO JA ESTA EM USO <<<<<<<<|")
                    print("|*************************************************|")
                    codigo2 = int(input(">>>>>>>> INFORME UM NOVO CODIGO     :"))
                    if codigo != codigo2:
                        vetor.append(codigo)
                        armazenaValoresInformadosPeloUsuarioNoVetor(vetor)
                        matriz.append(vetor)
                        vetor = []
                        mostraLinhasEmensagens("|>>>  CONTATO CADASTRADO COM SUCESSO  <<<|")

                    else:
                        mostraLinhasEmensagens("|>>>  O CODIGO INFORMADO É IGUAL AO ANTERIOR <<<|")

                else:
                    vetor.append(codigo)
                    armazenaValoresInformadosPeloUsuarioNoVetor(vetor)
                    matriz.append(vetor)
                    vetor = []


        else:
            mostraLinhasEmensagens("| >>>>>>     NÃO HA ESPAÇO NA AGENDA    <<<<<<< |")
    elif opcao == 2 :
            if len(matriz)== 0:
                mostraLinhasEmensagens("|>>>>>>>  A LISTA ESTA VAZIA <<<<<<<<|")
            else:

                mostraLinhasEmensagens("|>>>>    ALTERAR CONTATO         <<<<|")

                print("|*************************************************|")
                codigo = int(input(" INFORME O CODIGO DO CONTATO QUE DESEJA ALTERAR :"))
                print("|*************************************************|")
                print()
                print("|*******************|")
                print("|  1 - NOME         |")
                print("|  2 - TELEFONE     |")
                print("|*******************|")
                print()
                print("|*************************************************|")
                resposta = int(input("INFORME A OPÇAO QUE DESEJA ALTERAR : "))
                print("|*************************************************|")
                for l in range(len(matriz)):
                    if codigo == matriz[l][0]:
                        if resposta == 1:
                            mostraLinhasEmensagens(">>>> ALTERAR NOME DO CONTATO <<<<")
                            print("|-------------------------------------------|")
                            novoNome = str(input("INFORME O ""NOVO"" NOME DO CONTATO :"))
                            print()
                            numero = matriz[l][2]
                            del(matriz[l][1])
                            del (matriz[l][1])
                            matriz[l].append(novoNome)
                            matriz[l].append(numero)
                            print("|-------------------------------------------|")
                            mostraLinhasEmensagens("|>>>  CONTATO ALTERADO COM SUCESSO  <<<|")
                        elif resposta == 2 :
                            mostraLinhasEmensagens(">>>> ALTERAR NUMERO DO CONTATO <<<<")

                            novoNumero = int(input("INFORME O ""NOVO"" NUMERO DO CONTATO :"))
                            del(matriz[l][2])
                            matriz[l].append(novoNumero)
                            print("|-------------------------------------------|")
                            mostraLinhasEmensagens("|>>>  CONTATO ALTERADO COM SUCESSO    <<<|")
                        else:
                            mostraLinhasEmensagens(">>>>  A OPAÇÃO ESCOLHIDA É INVALIDA <<<<")
                    else:
                        if l == len(matriz):
                            mostraLinhasEmensagens("|>>>>>>>  NÃO HA CONTATO CADASTRADO COM O CODIGO INFORMADO <<<<<<<<|")



    elif opcao == 3:
        continuar = True
        if len(matriz)== 0:
            mostraLinhasEmensagens("|>>>>>>>  A LISTA ESTA VAZIA <<<<<<<<|")
        else:

            print("|-----------------------------------------------------------|")
            codigo = int(input("INFORME O CODIGO DO CONTATO A SER EXCLUIDO  : "))
            print("|-------------------------------------------------------------|")
            print()
            while continuar:
                for l in range(len(matriz)):
                    if codigo == matriz[l][0]:
                        del(matriz[l])
                        mostraLinhasEmensagens("|>>>>  CONTATO EXCLUIDO COM SUCESSO     <<<<|")
                        continuar = False
                    else:
                        mostraLinhasEmensagens("|>>>>>>>  NÃO HA CONTATO CADASTRADO COM O CODIGO INFORMADO <<<<<<<<|")
                        continuar = False


    elif opcao == 4:
        if len(matriz)== 0:
            mostraLinhasEmensagens("|>>>>>>>  A LISTA ESTA VAZIA <<<<<<<<|")
        else:
            for l in range(len(matriz)):
                print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
                print(f"|>>>>    CONTATO - {l+1}   <<<<|")
                print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
                print(f" # CODIGO   - {matriz[l][0]}")
                print(f" # NOME     - {matriz[l][1]}")
                print(f" # TELEFONE - {matriz[l][2]} ")
                print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
                print()

    elif opcao == 5:
        if len(matriz) == 0:
            mostraLinhasEmensagens("|>>>>>>>  A LISTA ESTA VAZIA <<<<<<<<|")
        else:
            print()
            print("|----------------------------------------------------------------------|")
            codigo = int(input(">>>>> INFORME O CODIGO DO CONTATO QUE DESEJA BUSCAR <<<<<"))
            print("|-----------------------------------------------------------------------|")
            print()
            while continuar:
                cont = 0
                for l in range(len(matriz)):
                    if codigo == matriz[l][0]:
                        print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
                        print(f"|>>>>    CONTATO - {l + 1}   <<<<|")
                        print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
                        print(f" # CODIGO   - {matriz[l][0]}")
                        print(f" # NOME     - {matriz[l][1]}")
                        print(f" # TELEFONE - {matriz[l][2]} ")
                        print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
                        print()
                        continuar = False
                    else:
                        cont += 1
                        if cont == len(matriz):
                            mostraLinhasEmensagens("|>>>>>>>  NÃO HA CONTATO CADASTRADO COM O CODIGO INFORMADO <<<<<<<<|")
                            continuar = False


    elif opcao == 6 :
        c = 0
        contNome = 0
        if len(matriz) == 0:
            mostraLinhasEmensagens("|>>>>>>>  A LISTA ESTA VAZIA <<<<<<<<|")
        else:
            print()
            print("|-----------------------------------------------------------|")
            nome = str(input("INFORME O NOME DO CONTATO QUE DESEJA BUSCAR    : "))
            print("|-------------------------------------------------------------|")
            print()
            for l in range(len(matriz)):
                if nome == matriz[l][1]:
                    contNome +=1
                    print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
                    print(f"|>>>>    CONTATO - {l + 1}   <<<<|")
                    print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
                    print(f" # CODIGO   - {matriz[l][0]}")
                    print(f" # NOME     - {matriz[l][1]}")
                    print(f" # TELEFONE - {matriz[l][2]} ")
                    print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
                    print()
                    print()

                else:
                    c = c+1
                    if c == len(matriz):
                        mostraLinhasEmensagens("|>>>      O NOME INFORMADO NÃO ESTA NA LISTA          <<<|")


            if contNome > 1 :
                    print("-="*30)
                    print(f"EXISTEM {contNome} CONTATOS SALVOS COM O MESMO NOME :")
                    print("-=" * 30)
                    print()
                    continuar = False

    elif opcao == 7:
        mostraLinhasEmensagens(" >>>>>> FINALIZANDO PROGRAMA .... <<<<<<")
        break
    else:
        mostraLinhasEmensagens(" >>>>>> A OPÇÃO ESCOLHIDA NÃO EXISTE <<<<<<")

                    
                    









