from PyQt5 import  uic,QtWidgets
from time import sleep
from playsound import playsound


turno = 1 #Variavel global que marca os turnos do jogo
backup_lista = ['', '', '', '', '', '', '', '', '']


def verificador(turno): #verifica de quem é a vez com base na variavel global "turno"
    if (turno%2) == 0:
        return "vez do x"
    else:
        return "vez do o"
        

def getCampos(): #pega os valores dos campos do game e transforma em uma lista de inteiros
    l1 = tictac.lineEdit.text()
    l2 = tictac.lineEdit_2.text()
    l3 = tictac.lineEdit_3.text()
    l4 = tictac.lineEdit_4.text()
    l5 = tictac.lineEdit_5.text()
    l6 = tictac.lineEdit_6.text()
    l7 = tictac.lineEdit_7.text()
    l8 = tictac.lineEdit_8.text()
    l9 = tictac.lineEdit_9.text()
    #verifica se os campos tem valores diferentes de 'X' 'O' ou 'vazio'
    if l1 != 'X' and l1 != 'O' and l1 != "" or l2 != 'X' and l2 != 'O' and l2 != "" or l3 != 'X' and l3 != 'O' and l3 != "" or l4 != 'X' and l4 != 'O' and l4 != "" or l5 != 'X' and l5 != 'O' and l5 != "" or l6 != 'X' and l6 != 'O' and l6 != "" or l7 != 'X' and l7 != 'O' and l7 != "" or l8 != 'X' and l8 != 'O' and l8 != "" or l9 != 'X' and l9 != 'O' and l9 != "":
        return True
    else: #retorna os campos em lista e limpa a mensagem de erro caso tenha ocorrido anteriormente
        tictac.label.setText("")#limpa mensagem de erro
        return [l1,l2,l3,l4,l5,l6,l7,l8,l9]


def verify_turn(lista):#verifica de quem é a vez com base no numero de "x" e "o" ja em jogo
    contX = 0
    contO = 0
    
    for i in range(9): #se retornar true é vez do "X" se retornar false é vez do "O"
        if lista[i] == 'X':
            contX = contX + 1
        elif lista[i] == "O":
            contO = contO + 1
    if contO >= contX:
        return "vez do x"
    else:
        return "vez do o"
    
def reset():
    global backup_lista
    global turno
    turno = 1
    backup_lista = ['', '', '', '', '', '', '', '', '']
    tictac.lineEdit.setText("")
    tictac.lineEdit_2.setText("")
    tictac.lineEdit_3.setText("")
    tictac.lineEdit_4.setText("")
    tictac.lineEdit_5.setText("")
    tictac.lineEdit_6.setText("")
    tictac.lineEdit_7.setText("")
    tictac.lineEdit_8.setText("")
    tictac.lineEdit_9.setText("")
    tictac.close()
    primeira.show()
    primeira.label_4.setText("Fim de Jogo")
    
    
    
def win():
    global backup_lista
    global turno
    fim = False
    l1 = tictac.lineEdit.text()
    l2 = tictac.lineEdit_2.text()
    l3 = tictac.lineEdit_3.text()
    l4 = tictac.lineEdit_4.text()
    l5 = tictac.lineEdit_5.text()
    l6 = tictac.lineEdit_6.text()
    l7 = tictac.lineEdit_7.text()
    l8 = tictac.lineEdit_8.text()
    l9 = tictac.lineEdit_9.text()
    
    # vitorias horizontais
    if l1==l2==l3 and l1!="":
        fim = True
    elif l4==l5==l6 and l4!="":
        fim = True
    elif l7==l8==l9 and l7!="":
        fim = True
    elif l1==l4==l7 and l1!="":# vitorias verticais
        
        fim = True
    elif l2==l5==l8 and l2!="":
        
        fim = True
    elif l3==l6==l9 and l3!="":
        
        fim = True
    elif l1==l5==l9 and l1!="":# vitorias diagonais
        
        fim = True
    elif l3==l5==l7 and l3!="":
        
        fim = True
    else:
        if turno == 9:
            tictac.label.setText("Empate")
            fim = True
    
    if fim == True:
        reset()
    
def backup(lista): #faz backup de uma lista
    global backup_lista
    lista = getCampos()
    
    for i in range(9):
        backup_lista[i] = lista[i]

def replace(lista): #adiciona na tela alguma lista 
    tictac.lineEdit.setText(lista[0])
    tictac.lineEdit_2.setText(lista[1])
    tictac.lineEdit_3.setText(lista[2])
    tictac.lineEdit_4.setText(lista[3])
    tictac.lineEdit_5.setText(lista[4])
    tictac.lineEdit_6.setText(lista[5])
    tictac.lineEdit_7.setText(lista[6])
    tictac.lineEdit_8.setText(lista[7])
    tictac.lineEdit_9.setText(lista[8])

def game_dupla():#Incrementa +1 na variavel "turno" para cada lance valido 
    # ===========TURNOS=======================
    global turno #acessa a variavel global vez
    global backup_lista
    
    vez = verificador(turno) #verifica a vez com base no "turno"
    lista = getCampos() #atribui em uma variavel todos os campos do jogo
    verifica = verify_turn(lista) #verifica o turno com base na contagem de "x" e "o"
    
    if lista == True: #caso o usuario digite algo fora do estipulado
        tictac.label.setText("So pode usar letras X ou O maiusculas")
        replace(backup_lista)
    else:
        verifica = verify_turn(lista) #verifica o turno com base na contagem de "x" e "o"
        if vez == verifica:#unica condição que atende ao jogo e 
            turno = turno + 1 #incrementa o turno
            tictac.label.setText("")#limpa alguma mensagem de erro anterior
            backup(lista)#faz backup da lista
            win()#verifica a vitoria
            
        else:
            tictac.label.setText("Lance inapropriado")
            replace(backup_lista)#recupera a ultima tela que esteve correta
    
def game_engine():
    global turno #acessa a variavel global vez
    global backup_lista
    
    vez = verificador(turno) #verifica a vez com base no "turno"
    lista = getCampos() #atribui em uma variavel todos os campos do jogo
    verifica = verify_turn(lista) #verifica o turno com base na contagem de "x" e "o"
    
    if lista == True: #caso o usuario digite algo fora do estipulado
        tictac.label.setText("So pode usar letras X ou O maiusculas")
        replace(backup_lista)
    else:
        verifica = verify_turn(lista) #verifica o turno com base na contagem de "x" e "o"
        if vez == verifica:#unica condição que atende ao jogo e 
            turno = turno + 1 #incrementa o turno
            tictac.label.setText("")#limpa alguma mensagem de erro anterior
            backup(lista)#faz backup da lista
            win()#verifica a vitoria
            
        else:
            tictac.label.setText("Lance inapropriado")
            replace(backup_lista)#recupera a ultima tela que esteve correta

#====================================================|
#                      Qt Designer                   |
#====================================================|

app=QtWidgets.QApplication([])

# =================TELAS====================
tictac = uic.loadUi("templates/tictac-dupla.ui")
engine = uic.loadUi("templates/tictac-engine.ui")
primeira = uic.loadUi("templates/principal.ui")
# ==========================================


#===========================================
def abrir_tela():
    primeira.close()
    tictac.show()
    tictac.label.setText("X começa")
def abrir_engine():
    primeira.close()
    engine.show()
    engine.label.setText("Jogue apenas com X")

primeira.pushButton.clicked.connect(abrir_tela)
primeira.pushButton_2.clicked.connect(abrir_engine)
#===========================================

#=================JOGANDO===================
tictac.pushButton.clicked.connect(game_dupla)
engine.pushButton.clicked.connect(game_engine)
#===========================================


primeira.show() #chama a tela de inicio
playsound("music/mensagem.mp3")#som ao entrar
app.exec()
