from pygame_functions import *
from pygame import *


def entrada_tempo():
    msm = ['00', ':', '00', ':', '00']
    texto = '''Entre com o tempo  feito pelo paciente.
     minutos : segundos : miléssimos
Caso ele não tenha  tenha feito deixe 00:00:00.

Entre com o tempo e confirme.'''
    instru = makeLabel(texto, 30, 130, 160, 'black', 'Arial',
                       'clear')
    showLabel(instru)
    tempo = makeLabel((''.join(msm)), 40, 150, 320, 'red')
    showLabel(tempo)
    Sim = makeSprite('Confirme.png')
    moveSprite(Sim, 636, 315)
    showSprite(Sim)
    pronto = True

    while pronto:
        for e in pygame.event.get():
            if e.type == QUIT:
                quit()
                sys.exit()

            # -----------------------------------------------------------------> CLICAR EM SIM CONFIRMA ENTRADA DE TEMPO
            elif 636 < mouseX() < 676 and 315 < mouseY() < 355:
                if e.type == MOUSEBUTTONDOWN:
                    hideSprite(Sim)
                    hideLabel(tempo)
                    hideLabel(instru)
                    pronto = False

            # -----------------------------------------------------------------------> CLICAR EM MIN ABRE CAIXA DE INPUT
            elif 150 < mouseX() < 190 and 320 < mouseY() < 360:
                if e.type == MOUSEBUTTONDOWN:
                    Min = makeTextBox(150, 328, 38, 0, '00', 2, 20)
                    showTextBox(Min)
                    msm[0] = textBoxInput(Min)
                    hideTextBox(Min)
                    if msm[0].isnumeric():
                        if len(msm[0]) < 2:
                            msm[0] = '0' + msm[0]
                        hideLabel(tempo)
                        tempo = makeLabel((''.join(msm)), 40, 150, 320, 'red')
                        showLabel(tempo)

                    # -----------------------------------------------------------> PÕE MSM[1] PRA ZERO SE ENTRADA ERRADA
                    else:
                        msm[0] = '00'
                        hideLabel(tempo)
                        tempo = makeLabel((''.join(msm)), 40, 150, 320, 'red')
                        showLabel(tempo)

            # -----------------------------------------------------------------------> CLICAR EM SEG ABRE CAIXA DE INPUT
            elif 192 < mouseX() < 232 and 320 < mouseY() < 360:
                if e.type == MOUSEBUTTONDOWN:
                    Seg = makeTextBox(194, 328, 38, 0, '00', 2, 20)
                    showTextBox(Seg)
                    msm[2] = textBoxInput(Seg)
                    hideTextBox(Seg)

                    if msm[2].isnumeric():
                        if len(msm[2]) < 2:
                            msm[2] = '0' + msm[2]
                        hideLabel(tempo)
                        tempo = makeLabel((''.join(msm)), 40, 150, 320, 'red')
                        showLabel(tempo)

                    # -----------------------------------------------------------> PÕE MSM[2] PRA ZERO SE ENTRADA ERRADA
                    else:
                        msm[2] = '00'
                        hideLabel(tempo)
                        tempo = makeLabel((''.join(msm)), 40, 150, 320, 'red')
                        showLabel(tempo)

            # ----------------------------------------------------------------------> CLICAR EM MILS ABRE CAIXA DE INPUT
            elif 234 < mouseX() < 274 and 320 < mouseY() < 360:
                if e.type == MOUSEBUTTONDOWN:
                    Mils = makeTextBox(240, 328, 38, 0, '00', 2, 20)
                    showTextBox(Mils)
                    msm[4] = textBoxInput(Mils)
                    hideTextBox(Mils)
                    if msm[4].isnumeric():
                        if len(msm[4]) < 2:
                            msm[4] += '0'
                        hideLabel(tempo)
                        tempo = makeLabel((''.join(msm)), 40, 150, 320, 'red')
                        showLabel(tempo)

                    # -----------------------------------------------------------> PÕE MSM[4] PRA ZERO SE ENTRADA ERRADA
                    else:
                        msm[4] = '00'
                        hideLabel(tempo)
                        tempo = makeLabel((''.join(msm)), 40, 150, 320, 'red')
                        showLabel(tempo)

    return msm


def sim_nao():
    sn = True
    SimOuNao = ''
    Sim = makeSprite('Confirme.png')
    moveSprite(Sim, 636, 315)
    showSprite(Sim)
    Nao = makeSprite('Negative.png')
    moveSprite(Nao, 552, 315)
    showSprite(Nao)
    while sn:
        for e in pygame.event.get():
            if e.type == QUIT:
                quit()
                sys.exit()

            elif 552 < mouseX() < 592 and 315 < mouseY() < 355:
                if e.type == MOUSEBUTTONDOWN:
                    SimOuNao = 'Não'
                    hideSprite(Sim)
                    hideSprite(Nao)
                    sn = False

            elif 636 < mouseX() < 676 and 315 < mouseY() < 355:
                if e.type == MOUSEBUTTONDOWN:
                    SimOuNao = 'Sim'
                    hideSprite(Sim)
                    hideSprite(Nao)
                    sn = False

    return SimOuNao


def confirme():
    Sim = makeSprite('Confirme.png')
    moveSprite(Sim, 636, 315)
    showSprite(Sim)
    conf = True
    while conf:
        for e in pygame.event.get():
            if e.type == QUIT:
                quit()
                sys.exit()

            elif 636 < mouseX() < 676 and 315 < mouseY() < 355:
                if e.type == MOUSEBUTTONDOWN:
                    hideSprite(Sim)
                    conf = False


def draw_options():
    drawEllipse(180, 200, 20, 20, 'blue', 2)
    drawEllipse(180, 225, 20, 20, 'blue', 2)
    drawEllipse(180, 250, 20, 20, 'blue', 2)
    drawEllipse(180, 275, 20, 20, 'blue', 2)
    drawEllipse(180, 300, 20, 20, 'blue', 2)
    drawEllipse(180, 325, 20, 20, 'blue', 2)
    drawEllipse(180, 350, 20, 20, 'blue', 2)


def falha():
    ficar = True
    texto = ['Marque a opção que melhor representa a falha do paciente no teste.',
'               Tentou mas não conseguiu.',
'               Não conseguiu executar sem ajuda.',
'               Não tentou, o avaliador sentiu-se inseguro.',
'               Não tentou, o paciente sentiu-se inseguro.',
'               O paciente não conseguiu entender as instruções.',
'               Outros, ',
'               O paciente recusou participação.']
    instru = makeLabel('\n'.join(texto), 24, 130, 160, 'black', 'Arial', 'clear')
    showLabel(instru)
    Sim = makeSprite('Confirme.png')
    moveSprite(Sim, 636, 315)
    showSprite(Sim)
    draw_options()
    i = 0
    while ficar:
        for e in pygame.event.get():
            if e.type == QUIT:
                quit()
                sys.exit()

            elif 636 < mouseX() < 676 and 315 < mouseY() < 355:
                if e.type == MOUSEBUTTONDOWN:
                    if 8 > i > 0:
                        if i == 6:
                            outros = makeTextBox(270, 310, 350, 0, "Digite e pressione 'enter'", 0, 20)
                            showTextBox(outros)
                            texto[i] = texto[i] + textBoxInput(outros)
                            hideTextBox(outros)
                        hideSprite(Sim)
                        hideLabel(instru)
                        clearShapes()
                        ficar = False

            elif 170 < mouseX() <200 and 190 < mouseY() < 210:
                if e.type == MOUSEBUTTONDOWN:
                    clearShapes()
                    draw_options()
                    drawEllipse(180, 200, 10, 10,'black')
                    i = 1
            elif 170 < mouseX() < 200 and 215 < mouseY() < 235:
                if e.type == MOUSEBUTTONDOWN:
                    clearShapes()
                    draw_options()
                    drawEllipse(180, 225, 10, 10, 'black')
                    i = 2
            elif 170 < mouseX() < 200 and 240 < mouseY() < 260:
                if e.type == MOUSEBUTTONDOWN:
                    clearShapes()
                    draw_options()
                    drawEllipse(180, 250, 10, 10, 'black')
                    i = 3
            elif 170 < mouseX() < 200 and 265 < mouseY() < 285:
                if e.type == MOUSEBUTTONDOWN:
                    clearShapes()
                    draw_options()
                    drawEllipse(180, 275, 10, 10, 'black')
                    i = 4
            elif 170 < mouseX() < 200 and 290 < mouseY() < 310:
                if e.type == MOUSEBUTTONDOWN:
                    clearShapes()
                    draw_options()
                    drawEllipse(180, 300, 10, 10, 'black')
                    i = 5
            elif 170 < mouseX() < 200 and 315 < mouseY() < 335:
                if e.type == MOUSEBUTTONDOWN:
                    clearShapes()
                    draw_options()
                    drawEllipse(180, 325, 10, 10, 'black')
                    i = 6
            elif 170 < mouseX() < 200 and 340 < mouseY() < 360:
                if e.type == MOUSEBUTTONDOWN:
                    clearShapes()
                    draw_options()
                    drawEllipse(180, 350, 10, 10, 'black')
                    i = 7

    return texto[i].strip()


def tela_inicial():
    fechars = makeSprite('FecharS.png')
    moveSprite(fechars, 922, 40)

    relatorios = makeSprite('RelatorioS.png')
    moveSprite(relatorios, 175, 350)

    iniciars = makeSprite('IniciarS.png')
    moveSprite(iniciars, 425, 350)

    sobres = makeSprite('SobreS.png')
    moveSprite(sobres, 676, 350)

    homeicon = makeSprite('HomeIcon.png')
    moveSprite(homeicon, 888, 40)

    homeicons = makeSprite('HomeIconS.png')
    moveSprite(homeicons, 888, 40)

    inicio = makeSprite('Inicio.png')
    moveSprite(inicio, 175, 40)

    Relatorio = makeSprite('Relatorio.png')
    moveSprite(Relatorio, 40, 40)

    sobre = makeSprite('Sobre.png')
    moveSprite(sobre, 40, 40)

    tela = True
    while tela:
        showSprite(inicio)
        for e in event.get():

            if e.type == QUIT:
                quit()
                sys.exit()

            # --------------------------------------------------------------------------------------------> FECHAR EM INICIO
            if 922 < mouseX() < 962 and 40 < mouseY() < 80:  # FECHAR
                showSprite(fechars)
                if e.type == MOUSEBUTTONDOWN:  # CLICAR EM FECHAR
                    quit()
                    sys.exit()

            # --------------------------------------------------------------------------------------> AQUI DENTRO: RELATÓRIO
            elif 175 < mouseX() < 325 and 350 < mouseY() < 540:
                showSprite(relatorios)
                if e.type == MOUSEBUTTONDOWN:  # AO CLICAR EM RELATORIO
                    hideAll()
                    showSprite(Relatorio)

                    # ----------------------------------------------------------------------------> INICIO DA TELA RELATÓRIO
                    ficar = True
                    while ficar:
                        for e in pygame.event.get():
                            # -------------------------------------------------------------------> HABILITAR FECHAR ENQUALTO
                            if e.type == QUIT:
                                quit()
                                sys.exit()

                            # --------------------------------------------------> VOLTAR PARA INICIAR DE DENTRO DE RELATÓRIO
                            if 888 < mouseX() < 962 and 40 < mouseY() < 120:
                                showSprite(homeicons)
                                if e.type == MOUSEBUTTONDOWN:  # AO CLICAR EM HOME
                                    hideAll()
                                    ficar = False
                            else:
                                hideSprite(homeicons)

            # ----------------------------------------------------------------------------------------> AQUI DENTRO: INICIAR
            elif 425 < mouseX() < 575 and 350 < mouseY() < 540:
                showSprite(iniciars)
                if e.type == MOUSEBUTTONDOWN:  # AO CLICAR EM INICIAR
                    hideAll()
                    tela = False

            elif 676 < mouseX() < 826 and 350 < mouseY() < 540:  # SOBRE
                showSprite(sobres)
                if e.type == MOUSEBUTTONDOWN:  # CLICAR EM RELATORIO          v  DENTRO DE RELATORIO v
                    hideAll()
                    showSprite(sobre)

                    # --------------------------------------------------------------------------------> INICIO DA TELA SOBRE
                    ficar = True
                    while ficar:

                        for e in pygame.event.get():
                            # -------------------------------------------------------------------> HABILITAR FECHAR ENQUANTO
                            if e.type == QUIT:
                                quit()
                                sys.exit()

                            # -------------------------------------------------------> VOLTAR PRA INICIAR DE DENTRO DE SOBRE
                            if 888 < mouseX() < 962 and 40 < mouseY() < 120:
                                showSprite(homeicons)
                                if e.type == MOUSEBUTTONDOWN:
                                    hideAll()
                                    ficar = False
                            else:
                                hideSprite(homeicons)

            #
            else:
                hideSprite(relatorios)
                hideSprite(sobres)
                hideSprite(iniciars)
                hideSprite(fechars)


def cadastro():
    global nome, idade, sexo, testeequilibrio, testecaminhada, testesentalevanta, relatorio

    Nome = makeLabel(nome, 24, 270, 194, 'blue', 'Arial', 'clear')

    Idade = makeLabel(idade, 24, 270, 294, 'blue', 'Arial', 'clear')

    registroidoso = makeSprite('RegistroIdoso.png')
    moveSprite(registroidoso, 40, 75)

    homeicon = makeSprite('HomeIcon.png')
    moveSprite(homeicon, 888, 40)

    homeicons = makeSprite('HomeIconS.png')
    moveSprite(homeicons, 888, 40)

    caixatextoidades = makeSprite('CaixaTextoIdadeS.png')
    moveSprite(caixatextoidades, 265, 294)

    caixatextonomes = makeSprite('CaixaTextoNomeS.png')
    moveSprite(caixatextonomes, 265, 194)

    registres = makeSprite('RegistreS.png')
    moveSprite(registres, 833, 282)

    CheckC = makeSprite('CheckC.png')
    CheckCM = False
    CheckCF = False
    showSprite(registroidoso)

    # --------------------------------------------------------------------> INICIO DA TELA REGISTRO DO IDOSO
    ficar = True
    while ficar:
        showSprite(homeicon)
        showLabel(Nome)
        showLabel(Idade)
        for e in pygame.event.get():
            # -------------------------------------------------------------------> HABILITAR FECHAR ENQUALTO
            if e.type == QUIT:
                quit()
                sys.exit()

            # ---------------------------------------------------> VOLTAR PARA INICIAR DE DENTRO DE REGISTRO
            if 888 < mouseX() < 962 and 40 < mouseY() < 120:
                showSprite(homeicons)
                if e.type == MOUSEBUTTONDOWN:  # CLICAR EM HOME
                    hideAll()
                    hideLabel(Nome)
                    hideLabel(Idade)
                    ficar = False
                    testeequilibrio = False
                    testecaminhada = False
                    testesentalevanta = False

            # --------------------------------------------------------------------> AQUI DENTRO: EDITAR NOME
            elif 265 < mouseX() < 765 and 194 < mouseY() < 224:  # NOME
                showSprite(caixatextonomes)
                if e.type == MOUSEBUTTONDOWN:  # AO CLICAR EM NOME
                    hideLabel(Nome)
                    NomeBox = makeTextBox(265, 190, 505, 0, "Digite e pressione 'enter'", 0, 24)
                    showTextBox(NomeBox)
                    nome = textBoxInput(NomeBox)
                    hideTextBox(NomeBox)
                    Nome = makeLabel(nome, 24, 270, 194, 'blue', 'Arial', 'clear')
                    showLabel(Idade)

            # -------------------------------------------------------------------> AQUI DENTRO: EDITAR IDADE
            elif 265 < mouseX() < 475 and 294 < mouseY() < 324:  # IDADE
                showSprite(caixatextoidades)

                if e.type == MOUSEBUTTONDOWN:  # AO CLICAR EM IDADE
                    hideLabel(Idade)
                    IdadeBox = makeTextBox(265, 290, 220, 0, "Apenas números", 0, 24)
                    showTextBox(IdadeBox)
                    idade = textBoxInput(IdadeBox)
                    if idade.isnumeric() == False:
                        idade = ' --- Idade --- '
                    elif int(idade) > 130:
                        idade = ' --- Idade --- '
                    hideTextBox(IdadeBox)
                    Idade = makeLabel(idade, 24, 270, 294, 'blue', 'Arial', 'clear')
                    showLabel(Idade)

            # --------------------------------------------------------------------> AQUI DENTRO: MARCAR SEXO
            elif 595 < mouseX() < 625 and 249 < mouseY() < 274:
                if e.type == MOUSEBUTTONDOWN:
                    sexo = 'Feminino'
                    hideSprite(CheckC)
                    moveSprite(CheckC, 592, 238)
                    showSprite(CheckC)
            elif 595 < mouseX() < 625 and 294 < mouseY() < 324:
                if e.type == MOUSEBUTTONDOWN:
                    sexo = 'Masculino'
                    hideSprite(CheckC)
                    moveSprite(CheckC, 592, 283)
                    showSprite(CheckC)

            # ----------------------------------------------------> AQUI DENTRO: BOTÃO REGISTRE INICIA TESTE
            elif 282 < mouseY() < 328 and 833 < mouseX() < 955:
                showSprite(registres)
                if e.type == MOUSEBUTTONDOWN:
                    if idade.isnumeric() and (
                            sexo == 'Masculino' or sexo == 'Feminino') and nome != ' --- Nome Completo --- ':
                        ficar = False
                        hideAll()
                        hideLabel(Nome)
                        hideLabel(Idade)
                        relatorio = (nome+', '+idade+', '+sexo+'.')

            else:
                hideSprite(registres)
                hideSprite(homeicons)


# RELATORIO - OK
def equilibrio():
    global nome, idade, sexo, testeequilibrio, relatorio, Nome, Idade, pt1, pt2, pt3, tempo1, tempo2, tempo3, pt_eq
    if testeequilibrio:
        #---------------------------------------------------------> VARIÁVEIS EM TESTE DE EQUILIBRIO
        q_01 = ''  # p_01 junto
        q_02 = ''  # p_01 parcial frente
        q_03 = ''  # p_01 fremte
        flh_eq = True
        tempo_junto = 0  # p_02 junto
        tempo_pfrente = 0  # p_02 parcial frente
        tempo_frente = 0  # p_02 frente
        pt_eq = 0

        textos = [
f'''Esse será o teste físco de:
{nome}.
As ________ e orientações sarão mostradas 
nessa caixa.

Confirme para continuar.''',

'''Aqui aparecerão algumas
sugestões de como orientar
seu paciente.''',

'''Vamos ao Teste de Equilibrio 1:
O paciente deverá ficar 10 segundos 
cronometrados, em pé, com os calcanhares
e pontas dos pés juntos.

Confirme para continuar.''',

'''Vamos ao Teste de Equilibrio 2:
O paciente deverá ficar 10 segundos 
cronometrados, em pé, com os pés juntos,
parcialmente um a frente do outro.

Confirme para continuar.''',

'''Vamos ao Teste de Equilibrio 3:
O paciente deverá ficar 10 segundos 
cronometrados, em pé, com os pés alinhados,
um a frente do outro.

Confirme para continuar.''']


        masculino = makeSprite('Masculino.png')
        moveSprite(masculino, 773, 93)

        feminino = makeSprite('Feminino.png')
        moveSprite(feminino, 779, 93)

        teste = makeSprite('Teste.png')
        moveSprite(teste, 40, 40)

        Nome = makeLabel(nome, 24, 128, 85, 'blue', 'Arial', 'clear')
        Idade = makeLabel(idade, 24, 626, 85, 'blue', 'Arial', 'clear')

        showLabel(Idade)

        showLabel(Nome)

        if sexo == 'Feminino':
            showSprite(feminino)
        else:
            showSprite(masculino)

        # ---------------------------------------------------------> INICIO DA TELA DE TESTE

        showSprite(teste)
        for e in pygame.event.get():
            # -----------------------------------------------> HABILITAR FECHAR ENQUANTO
            if e.type == QUIT:
                quit()
                sys.exit()

            # --------------------------------------------> INICIO DOS COMANTOS EM TESTE
        pergunta = makeLabel('perguntas', 30, 165, 223, 'blue')
        showLabel(pergunta)
        instru = makeLabel(textos[0], 30, 130, 160, 'black', 'Arial', 'clear')
        showLabel(instru)

        confirme()

        hideLabel(instru)
        hideLabel(pergunta)
        instru = makeLabel('\n\n\n\n\nConfirme para continuar.', 30, 130, 160)
        showLabel(instru)
        sugest = makeLabel(textos[1], 24, 718, 160, (186, 47, 125), 'Arial', 'clear')
        showLabel(sugest)

        confirme()

        hideLabel(sugest)
        hideLabel(instru)

        # -------------------------------------------------------> INICIO DOS TESTES
        # --------------------------------------------------------------------> Q_01
        instru = makeLabel(textos[2], 30, 130, 160, 'black', 'Arial', 'clear')
        showLabel(instru)

        drawLine(30, 590, 200, 590, 'green', 4)

        confirme()

        clearShapes()
        hideLabel(instru)
        pergunta = makeLabel('O paciente conseguiu ficar os 10s?', 30, 130, 160, 'blue')
        showLabel(pergunta)

        q_01 = sim_nao()
        hideLabel(pergunta)
        relatorio += '\nO paciente conseguiu ficar 10 segundos equilibrado com os pés juntos? ' + q_01 + '.'


        # ---------------------------------------------------------------------------------------------> BIFURCAÇÃO Q_01
        if q_01 == 'Sim':
            pt_eq += 1
            hideLabel(sugest)
            hideLabel(instru)

            pt1 = makeLabel(str(pt_eq), 40, 120, 500, 'green')
            showLabel(pt1)
            passou1 = makeSprite('CheckC.png')
            moveSprite(passou1, 150, 400)
            showSprite(passou1)

            # ----------------------------------------------------------------> Q_02
            instru = makeLabel(textos[3], 30, 130, 160, 'black', 'Arial', 'clear')
            showLabel(instru)
            drawLine(223, 590, 393, 590, 'green', 4)

            confirme()

            hideLabel(instru)
            clearShapes()
            pergunta = makeLabel('O paciente conseguiu ficar os 10s?', 30, 130, 160,
                                 'blue')
            showLabel(pergunta)

            q_02 = sim_nao()
            hideLabel(pergunta)
            relatorio += '\nO paciente conseguiu ficar 10 segundos equilibrado com os pés juntos, parcialmente a frente? ' + q_02 + '.'

            # -----------------------------------------------------------------------------------------> BIFURCAÇÃO Q_02
            if q_02 == 'Sim':
                pt_eq += 1

                hideLabel(sugest)
                hideLabel(instru)

                pt2 = makeLabel(str(pt_eq), 40, 310, 500, 'green')
                showLabel(pt2)
                passou2 = makeSprite('CheckC.png')
                moveSprite(passou2, 350, 400)
                showSprite(passou2)

                # ------------------------------------------------------------> Q_03
                instru = makeLabel(textos[4], 30, 130, 160, 'black', 'Arial', 'clear')
                showLabel(instru)
                drawLine(416, 590, 586, 590, 'green', 4)

                confirme()

                hideLabel(instru)
                clearShapes()
                pergunta = makeLabel('O paciente conseguiu ficar os 10s?', 30, 130,160, 'blue')
                showLabel(pergunta)

                q_03 = sim_nao()
                relatorio += '\nO paciente conseguiu ficar 10 segundos equilibrado com os pés alinhados a frente? ' + q_03 + '.'
                hideLabel(pergunta)

                # -------------------------------------------------> BIFURCAÇÃO Q_03
                if q_03 == 'Sim':
                    pt_eq += 2

                    pt3 = makeLabel(str(pt_eq), 40, 500, 500, 'green')
                    showLabel(pt3)
                    passou3 = makeSprite('CheckC.png')
                    moveSprite(passou3, 550, 400)
                    showSprite(passou3)
                    flh_eq = False
                    testeequilibrio = False
                    relatorio += '\nO paciente conclui todos os testes de equilibrio.'

                # --------------------------------------------------------> ELSE Q-3
                else:
                    tempo_frente = entrada_tempo()
                    segs = (int(tempo_frente[0]) * 60 + int(tempo_frente[2]) + (int(tempo_frente[4]) / 100))

                    if segs >= 3:
                        tempo3 = makeLabel(''.join(tempo_frente), 20, 510, 430,
                                           'green')
                        showLabel(tempo3)
                        pt_eq += 1
                        pt3 = makeLabel(str(pt_eq), 40, 500, 500, 'green')
                        showLabel(pt3)
                        flh_eq = False
                        testeequilibrio = False
                        relatorio += '\nO paciente ficou ' + ''.join(tempo_frente) + '.'

                    else:
                        tempo3 = makeLabel(''.join(tempo_frente), 20, 510, 430, 'red')
                        showLabel(tempo3)
                        showLabel(falha3)


            # ------------------------------------------------------------> ELSE Q-2
            else:
                tempo_pfrente = entrada_tempo()

                tempo2 = makeLabel(''.join(tempo_pfrente), 20, 310, 430, 'red')
                showLabel(tempo2)
                relatorio += '\nO paciente ficou ' + ''.join(tempo_pfrente) + '.'
                showLabel(falha2)
                showLabel(falha3)
                relatorio += '\nO paciente foi dispensado dos outros testes de equilibrio.'

        # ---------------------------------------------------------------> ELSE Q-01
        else:
            tempo_junto = entrada_tempo()

            tempo1 = makeLabel((''.join(tempo_junto)), 20, 110, 430, 'red')
            showLabel(tempo1)
            relatorio += '\nO paciente ficou '+ ''.join(tempo_junto)+'.'
            showLabel(falha1)
            showLabel(falha2)
            showLabel(falha3)
            relatorio += '\nO paciente foi dispensado dos outros testes de equilibrio.'

        relatorio += '\nA pontuação total no teste de equilíbrio foi ' + str(pt_eq) + '.'
        if flh_eq:
            flh_eq = falha()
            testeequilibrio = False
            relatorio += '\nFalha: '+flh_eq
        else:
            flh_eq = ''
            testeequilibrio = False


# RELATORIO - OK
def caminhada():
    global teste, tam_test, pt4, tempo4, tempo5, testecaminhada, falha4, relatorio, apoioA, apoioB, pt_cm

    tam_test = 0
    pt_cm = 0
    flh_cm = True

    textos = [
f'''Vamos ao Teste de Caminhada.
Este será divido em dois testes (A e B),
com sua distância de 3 ou 4 metros,
devidamente demarcado no chão e o tempo
do paciente deverá ser cronometrado.
Confirme para continuar.''',

'''De quantos metros será a pista que
o paciente percorrerá, 3 metro ou 4 metro?''']


    if testecaminhada:
        # showSprite(teste)
        for e in pygame.event.get():
            # -----------------------------------------------> HABILITAR FECHAR ENQUANTO
            if e.type == QUIT:
                quit()
                sys.exit()

        # --------------------------------------------> INICIO DOS COMANTOS EM TESTE
        instru = makeLabel(textos[0], 30, 130, 160, 'black', 'Arial', 'clear')
        showLabel(instru)

        confirme()

        hideLabel(instru)

        # ------------------------------------------> INICIO DOS TESTES <-----------------------------------------------

        # ------------------------------------------------------------------------------> INICIO DO TESTE DE CAMINHADA A
        pergunta = makeLabel(textos[1], 30, 130, 160, 'blue', 'Arial', 'clear')
        showLabel(pergunta)

        drawLine(609, 590, 779, 590, 'green', 4)

        while tam_test != 3 and tam_test != 4:
            Tambox = makeTextBox(300, 250, 110, 0, '3 ou 4', 1, 40)
            showTextBox(Tambox)
            tam_test = textBoxInput(Tambox)
            hideTextBox(Tambox)
            if tam_test.isnumeric():
                tam_test = int(tam_test)

        if tam_test == 3:
            nmetros = makeSprite('3m.png')
        else:
            nmetros = makeSprite('4m.png')
        moveSprite(nmetros, 645, 540)
        showSprite(nmetros)
        relatorio += '\nO teste de caminhada será feito em um percurso de ' + str(tam_test) + 'm.'
        hideLabel(pergunta)
        instru = makeLabel(('Início do Teste de Caminhada A.\n\nO paciente deve caminhar em passos habituais\na '
                            'distância de ' + str(tam_test) + ' metros,\n\nConfirme para continuar.'),30, 130, 160,
                            'black', 'Arial', 'clear')
        showLabel(instru)

        confirme()

        clearShapes()
        hideLabel(instru)
        pergunta = makeLabel('O paciente fez uso de algum apoio?', 30, 130, 160, 'blue')
        showLabel(pergunta)
        apoio1 = sim_nao()

        if apoio1 == 'Sim':
            Tambox = makeTextBox(138, 250, 548, 0, 'Qual tipo de apoio o paciente utilizou?', 0, 35)
            showTextBox(Tambox)
            apoio1 = textBoxInput(Tambox)
            hideTextBox(Tambox)
            relatorio += '\nNo percurso A o paciente fez uso de: ' + apoio1 + '.'
            apoioA = makeLabel(apoio1, 20, 700, 535)
            showLabel(apoioA)

        hideLabel(pergunta)
        caminhadaA = entrada_tempo()
        segs = (int(caminhadaA[0]) * 60 + int(caminhadaA[2]) + (int(caminhadaA[4]) / 100))
        tempo = segs
        if tam_test == 3:
            if 6.52 < tempo > 1:
                tempo4 = makeLabel(''.join(caminhadaA), 20, 690, 418, 'green')
            else:
                tempo4 = makeLabel(''.join(caminhadaA), 20, 690, 418, 'red')
        else:
            if 8.7 < tempo > 1:
                tempo4 = makeLabel(''.join(caminhadaA), 20, 690, 418, 'green')
            else:
                tempo4 = makeLabel(''.join(caminhadaA), 20, 690, 418, 'red')
        showLabel(tempo4)
        relatorio += '\nO tempo no percurso A foi ' + ''.join(caminhadaA) + '.'
        # ------------------------------------------------------------------------------> INICIO DO TESTE DE CAMINHADA B

        instru = makeLabel(('Início do Teste de Caminhada B.\n\nO paciente deve caminhar em passos habituais\na '
                            'distância de ' + str(tam_test) + ' metros,\n\nConfirme para continuar.'), 30, 130, 160,
                           'black', 'Arial', 'clear')
        showLabel(instru)

        confirme()

        clearShapes()
        hideLabel(instru)
        pergunta = makeLabel('O paciente fez uso de algum apoio?', 30, 130, 160, 'blue')
        showLabel(pergunta)
        apoio2 = sim_nao()

        if apoio2 == 'Sim':
            Tambox = makeTextBox(138, 250, 548, 0, 'Qual tipo de apoio o paciente utilizou?', 0, 35)
            showTextBox(Tambox)
            apoio2 = textBoxInput(Tambox)
            hideTextBox(Tambox)
            relatorio += '\nNo percurso B o paciente fez uso de: ' + apoio2 + '.'
            apoioB = makeLabel(apoio2, 20, 700, 555)
            showLabel(apoioB)

        hideLabel(pergunta)
        caminhadaA = entrada_tempo()
        segs = (int(caminhadaA[0]) * 60 + int(caminhadaA[2]) + (int(caminhadaA[4]) / 100))

        if tam_test == 3:
            if 6.52 < segs > 1:
                tempo5 = makeLabel(''.join(caminhadaA), 20, 690, 442, 'green')
            else:
                tempo5 = makeLabel(''.join(caminhadaA), 20, 690, 442, 'red')
        else:
            if 8.7 < segs > 1:
                tempo5 = makeLabel(''.join(caminhadaA), 20, 690, 442, 'green')
            else:
                tempo5 = makeLabel(''.join(caminhadaA), 20, 690, 442, 'red')
        showLabel(tempo5)
        relatorio += '\nO tempo no percurso B foi ' + ''.join(caminhadaA) + '.'

        if tempo == 0:
            tempo = segs
        elif tempo > segs and segs > 0:
            tempo = segs

        relatorio += '\nO melhor tempo equivale à ' + str(tempo) + ' segundos.'

        if tam_test == 3:
            if tempo > 6.52:
                pt_cm = 1
            elif tempo >= 4.66:
                pt_cm = 2
            elif tempo >= 3.62:
                pt_cm = 3
            elif tempo > 1:
                pt_cm = 4
            else:
                pt_cm = 0

        if tam_test == 4:
            if tempo > 8.7:
                pt_cm = 1
            elif tempo >= 6.21:
                pt_cm = 2
            elif tempo >= 4.82:
                pt_cm = 3
            elif tempo > 1:
                pt_cm = 4
            else:
                pt_cm = 0

        relatorio += '\nA pontuação no teste de caminhada foi: ' + str(pt_cm) + ' pontos.'

        if pt_cm == 0:
            showLabel(falha4)
            flh_cm = falha()
            relatorio += '\nFalha: '+flh_cm

        else:
            pt4 = makeLabel(str(pt_cm), 40, 700, 500, 'green')
            showLabel(pt4)
            passou4 = makeSprite('CheckC.png')
            moveSprite(passou4, 750, 400)
            showSprite(passou4)


# RELATORIO OK
def sentalevanta():
    global testesentalevanta, falha5, tempo6, pt5, relatorio, salvarrelatorio, pt_sl, pt_cm, pt_eq

    textos = [
f'''Vamos ao Teste de Sentar e Levantar.
Este será divido em duas partes, sendo a primeira
de uma tentativa para saber se o paciente
conseguirá fazer, e a segunda de 5 tentativas que
deverá ser cronometrada em seu tempo total.
Confirme para continuar.''',

'''Início do Teste de Sentar e Levantar 1:

O paciente irá levantar-se da cadeira com os
braços cruzados no peito.

Confirme para continuar.''',

'''Início do Teste de Sentar e Levantar 2:
O paciente irá levantar-se da cadeira 5 vezes
com os braços cruzados no peito, o tempo deverá
ser cronometrado.

Confirme para continuar.''']

    if testesentalevanta:
        # showSprite(teste)
        for e in pygame.event.get():
            # -----------------------------------------------> HABILITAR FECHAR ENQUANTO
            if e.type == QUIT:
                quit()
                sys.exit()

        # --------------------------------------------> INICIO DOS COMANTOS EM TESTE
        drawLine(802, 590, 972, 590, 'green', 4)
        instru = makeLabel(textos[0], 30, 130, 160, 'black', 'Arial', 'clear')
        showLabel(instru)

        confirme()

        hideLabel(instru)

        instru = makeLabel(textos[1], 30, 130, 160, 'black', 'Arial', 'clear')
        showLabel(instru)

        confirme()

        hideLabel(instru)
        clearShapes()

        pergunta = makeLabel('O paciente conseguiu fazer o movimento\n sem apoio?', 30, 130, 160, 'blue')
        showLabel(pergunta)
        senlev_sn = sim_nao()
        relatorio += '\nO paciente conseguiu fazer o movimento sentar e levantar, sem apoio? ' + senlev_sn + '.'
        hideLabel(pergunta)
        if senlev_sn == 'Sim':
            instru = makeLabel(textos[2], 30, 130, 160, 'black', 'Arial', 'clear')
            showLabel(instru)

            confirme()
            hideLabel(instru)
            pergunta = makeLabel('O paciente conseguiu fazer os 5\nmovimentos sem apoio?', 30, 130, 160, 'blue')
            showLabel(pergunta)
            senlev_sn = sim_nao()
            hideLabel(pergunta)
            relatorio += '\nO paciente conseguiu fazer os 5 movimentos de sentar e levantar, sem apoio? ' + senlev_sn + '.'
            if senlev_sn == 'Sim':
                tempo_sl = entrada_tempo()
                segs = (int(tempo_sl[0]) * 60 + int(tempo_sl[2]) + (int(tempo_sl[4]) / 100))

                tempo6 = makeLabel(''.join(tempo_sl), 20, 890, 418, 'green')
                showLabel(tempo6)
                relatorio += '\nO tempo do paciente foi: ' + ''.join(tempo_sl) + '.'
                if segs > 1:

                    if segs > 16.7:
                        pt_sl = 1
                    elif segs >= 13.7:
                        pt_sl = 2
                    elif segs >= 11.2:
                        pt_sl = 3
                    elif segs > 1:
                        pt_sl = 4

                    relatorio += '\nA pontuação total do Teste Sentar e Levantar foi: ' + str(pt_sl) + ' pontos.'
                    pt5 = makeLabel(str(pt_sl), 40, 900, 500, 'green')
                    showLabel(pt5)
                    passou5 = makeSprite('CheckC.png')
                    moveSprite(passou5, 950, 400)
                    showSprite(passou5)

                else:
                    pt_sl = 0
                    relatorio += '\nA pontuação total do Teste Sentar e Levantar foi: ' + str(pt_sl) + ' pontos.'
                    flh_sl = falha()
                    relatorio += '\nFalha: ' + flh_sl
                    showLabel(falha5)

            else:
                relatorio += '\nO paciente foi do restante do teste de sentar e levantar'
                pt_sl = 0
                relatorio += '\nA pontuação total do Teste Sentar e Levantar foi: ' + str(pt_sl) + ' pontos.'
                flh_sl = falha()
                relatorio += '\nFalha: ' + flh_sl
                showLabel(falha5)
        else:
            relatorio += '\nO paciente foi do restante do teste de sentar e levantar'
            pt_sl = 0
            relatorio += '\nA pontuação total do Teste Sentar e Levantar foi: ' + str(pt_sl) + ' pontos.'
            flh_sl = falha()
            relatorio += '\nFalha: ' + flh_sl
            showLabel(falha5)

        relatorio += '\nA pontuação total final foi: ' + str(pt_eq + pt_cm + pt_sl) + ' pontos.'

        instru = makeLabel('\n\nColeta de dados concluída.\n\n\nConfirme para continuar.', 30, 130, 160, 'black', 'Arial', 'clear')
        showLabel(instru)

        confirme()

        hideLabel(instru)
        salvarrelatorio = True


def salvar():
    global relatorio, salvarrelatorio
    if salvarrelatorio:
        relatorio += '\n\n'
        arquivo = open('relatorio.txt','a')
        arquivo.write(relatorio)
        arquivo.close()

        instru = makeLabel((relatorio + '\n\n\nPressione "Enter" pra continuar.'), 24, 40, 40, 'black', 'Arial', 'clear')
        showLabel(instru)
        waitPress()
        hideLabel(instru)

        relatorio = ''


def limpar_tela():
    global nome, idade, sexo, Nome, Idade, pt1, pt2, pt3, pt4, pt5, falha1, falha2, falha3, falha4, falha5, tempo1,\
        tempo2, tempo3, tempo4, tempo5, tempo6, apoioA, apoioB, pt_sl, pt_cm, pt_eq
    a = [Nome, Idade, pt1, pt2, pt3, pt4, pt5, falha1, falha2, falha3, falha4, falha5, tempo1, tempo2, tempo3, tempo4,
         tempo5, tempo6, apoioA, apoioB]
    hideAll()
    nome = ' --- Nome Completo --- '
    idade = ' --- Idade --- '
    sexo = ''
    pt_cm = 0
    pt_eq = 0
    pt_sl = 0

    for i in a:
        hideLabel(i)


relatorio = ''

# --------------------------------------------------------------------------------------------------------------------->
screenSize(1003, 620)
setBackgroundColour((230, 230, 230))
display.set_icon(pygame.image.load('Icon.png'))
display.set_caption('Radefi - Rápida Avaliação de Desempenho Físico do Idosos')



testeequilibrio = True
testecaminhada = True
testesentalevanta = True
salvarrelatorio = False

nome = ' --- Nome Completo --- '
idade = ' --- Idade --- '
sexo = ''

pt_eq = 0
pt_cm = 0
pt_sl = 0

Nome = ''
Idade = ''
pt1 = ''
pt2 = ''
pt3 = ''
pt4 = ''
pt5 = ''
tempo1 = ''
tempo2 = ''
tempo3 = ''
tempo4 = ''
tempo5 = ''
tempo6 = ''
apoioA = ''
apoioB = ''
falha1 = makeLabel('Falha', 20, 80, 550, 'red', 'Arial', 'yellow')
falha2 = makeLabel('Falha', 20, 280, 550, 'red', 'Arial', 'yellow')
falha3 = makeLabel('Falha', 20, 480, 550, 'red', 'Arial', 'yellow')
falha4 = makeLabel('Falha', 20, 680, 550, 'red', 'Arial', 'yellow')
falha5 = makeLabel('Falha', 20, 880, 550, 'red', 'Arial', 'yellow')

tam_test = ''
nmetros =''

tick(60)

while True:
    tela_inicial()
    cadastro()
    equilibrio()
    caminhada()
    sentalevanta()
    limpar_tela()
    salvar()
    testeequilibrio = True
    testecaminhada = True
    testesentalevanta = True
    salvarrelatorio = False





