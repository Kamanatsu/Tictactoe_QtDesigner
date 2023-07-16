from PyQt5 import  uic,QtWidgets


#===================FUNCIONAMENTO=====================
#|  1. Puxa os dados dos campos do game
#|  2. Verifica as alterações feitas e  se são validas
#|  3. Seta permanentemente os valores digitados
#| 
#|
#|
#|

def vez_de_quem(contador):
    if contador % 2 == 0:
        tictac.label.setText("Vez do O")
    else:
        tictac.label.setText("Vez do X")

def contagem():
    l1 = tictac.lineEdit.text()
    l2 = tictac.lineEdit_2.text()
    l3 = tictac.lineEdit_3.text()
    l4 = tictac.lineEdit_4.text()
    l5 = tictac.lineEdit_5.text()
    l6 = tictac.lineEdit_6.text()
    l7 = tictac.lineEdit_7.text()
    l8 = tictac.lineEdit_8.text()
    l9 = tictac.lineEdit_9.text()
    
    contador = 0
    for lista in lista:
        if lista[lista] == "X":
            contadorX = contadorX + 1
    
    if contagem != contador:
        tictac.label.setText("Vc nao digitou um campo")


def estado(): #retorna o estado dos campos do jogo
    l1 = tictac.lineEdit.text()
    l2 = tictac.lineEdit_2.text()
    l3 = tictac.lineEdit_3.text()
    l4 = tictac.lineEdit_4.text()
    l5 = tictac.lineEdit_5.text()
    l6 = tictac.lineEdit_6.text()
    l7 = tictac.lineEdit_7.text()
    l8 = tictac.lineEdit_8.text()
    l9 = tictac.lineEdit_9.text()
    
    lista = [l1,l2,l3,l4,l5,l6,l7,l8,l9]
    contador = 0
    for lista in lista:
        if lista[lista] == "":
            contador = contador + 1
    
    if vez != contador:
        tictac.label.setText("Vc nao digitou um campo")
    
    
    
    if l1 != 'X' or l1 != 'O' or l2 != 'X' or l2 != 'O' or l3 != 'X' or l3 != 'O' or l4 != 'X' or l4 != 'O' or l5 != 'X' or l5 != 'O' or l6 != 'X' or l6 != 'O' or l7 != 'X' or l7 != 'O' or l8 != 'X' or l8 != 'O' or l9 != 'X' or l9 != 'O':
        tictac.label.setText("So pode usar letras X ou O maiusculas")
    
    # vitorias horizontais
    if l1==l2==l3:
        return()
    if l3==l4==l5:
        return()
    if l6==l7==l8:
        return()
    
    # vitorias verticais
    if l1==l3==l6:
        return()
    if l2==l4==l7:
        return()
    if l3==l5==l8:
        return()
    
    # vitorias diagonais
    if l1==l4==l8:
        return()
    if l3==l4==l6:
        return()

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
        tictac.label.setText("So pode usar letras X ou O maiusculas")
        return[]
    else: #transforma os campos em inteiros e limpa a mensagem de erro caso tenha ocorrido anteriormente
        if l1 == "X":
            l1 = 1
        elif l1 == "O":
            l1 = 2
        else:
            l1 = 0
        
        if l2 == "X":
            l2 = 1
        elif l2 == "O":
            l2 = 2
        else:
            l2 = 0
        
        if l3 == "X":
            l3 = 1
        elif l3 == "O":
            l3 = 2
        else:
            l3 = 0
            
        if l4 == "X":
            l4 = 1
        elif l4 == "O":
            l4 = 2
        else:
            l4 = 0
        
        if l5 == "X":
            l5 = 1
        elif l5 == "O":
            l5 = 2
        else:
            l5 = 0
            
        if l6 == "X":
            l6 = 1
        elif l6 == "O":
            l6 = 2
        else:
            l6 = 0
            
        if l7 == "X":
            l7 = 1
        elif l7 == "O":
            l7 = 2
        else:
            l7 = 0
            
        if l8 == "X":
            l8 = 1
        elif l8 == "O":
            l8 = 2
        else:
            l8 = 0
        
        if l9 == "X":
            l9 = 1
        elif l9 == "O":
            l9 = 2
        else:
            l9 = 0
        tictac.label.setText("")#limpa mensagem de erro
        return [l1,l2,l3,l4,l5,l6,l7,l8,l9]

def game_dupla():#trata o jogo como turnos
    # ===========TURNO 1=================
    lista = getCampos()
    print(lista[0])
    
    


app=QtWidgets.QApplication([])

# =================TELAS====================
tictac = uic.loadUi("templates/tictac.ui")
# ==========================================


#=================JOGANDO===================
tictac.pushButton.clicked.connect(game_dupla)
#===========================================


tictac.show() #chama a tela do jogo da velha
app.exec()