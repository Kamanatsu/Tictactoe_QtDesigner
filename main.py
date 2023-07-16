from PyQt5 import  uic,QtWidgets


def vez_de_quem():
    vez = vez + 1


def estado(): #retorna o estado dos campos do jogo
    
    vez = vez_de_quem()
    if vez % 2 == 0:
        tictac.label.setText("Vez do O")
    else:
        tictac.label.setText("Vez do X")
    
    
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

app=QtWidgets.QApplication([])



# =================TELAS====================
tictac = uic.loadUi("templates/tictac.ui")
# ==========================================

#=================JOGANDO===================
tictac.pushButton.clicked.connect(estado)

#===========================================



tictac.show() #chama a tela do jogo da velha
app.exec()