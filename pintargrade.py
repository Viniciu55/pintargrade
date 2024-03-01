from PIL import Image, ImageDraw
import os

verdes = []
azuis =[]
vermelhas = []
arq_necessarios=["assets/verde.txt","assets/azul.txt","assets/vermelho.txt"]
for a in arq_necessarios:
    try:
        arq = open(a,"r")
    except FileNotFoundError:
        comando = "touch"+" "+a
        os.system(comando)
try:
    arq = open("./assets/GRADE_NEW.jpeg", "r")
except FileNotFoundError:
    print("ERRO!!")
    print("a imagem base não foi encontrada, encerrando programa")
    exit()

#lendo os arquivos
with open("assets/verde.txt","r") as arquivo:
    for linha in arquivo:
        verdes.append(linha.strip())
with open("assets/vermelho.txt","r") as arquivo:
    for linha in arquivo:
        vermelhas.append(linha.strip())
with open("assets/azul.txt","r") as arquivo:
    for linha in arquivo:
        azuis.append(linha.strip())

# Abrindo a imagem
imagem = Image.open("./assets/GRADE_NEW.jpeg")
objeto = ImageDraw.Draw(imagem)

semestres = [0,115,299,480,655,835,1019,1199] 
altura = [0,23,101,179,257,334,410]
materias1 = {"F1":(1, 2),"F1exp":(1, 1),"IAL":(1, 3),"C1":(1, 4),"IEC":(1, 5),"APC":(1,6)}
materias2 = {"F2exp":(2, 1),"F2":(2, 2),"PE":(2, 3),"C2":(2, 4),"ED":(2, 6)} #semestre x altura
materias3 = {"SSTC":(3, 3),"C3":(3, 4),"MP":(3, 6)}
materias4 = {"SD":(4,1),"labSD":(4,2),"eletromag":(4,3),"CN":(4,4),"TP1":(4,6)}
materias5 = {"sismic":(5,1),"lab sismic":(5,2),"SSTD:":(5,3),"ICE":(5,4),"OAC":(5,5),"LP":(5,6)}
materias6 = {"CE":(6,1),"labCE":(6,2),"TR1":(6,3),"SB":(6,4),"PAA":(6,5),"ES":(6,6)}
materias7 = {"Eletrônica":(7,1),"labEletrônica":(7,2),"TR2":(7,3),"SO":(7,4)}
m = (materias1,materias2,materias3,materias4,materias5,materias6,materias7)

def Menu():
        print("==MENU PRINCIPAL==")
        print("[1] adicionar em verde, [2] adicionar em azul, [3] adicionar em vermelho")
        print("[4] salvar alterações, [5] remover pontos")
        print("[6] gerar imagem, [0] para sair")
        print('digite "help" ou "sos" para ver todos os comandos')
        print()

def Gravarlista():
    print("qual lista de matérias deseja salvar?")
    print('[1] para a lista "verdes"')
    print('[2] para a lista "azuis"')
    print('[3] para a lista "vermelhas"')
    print('[4] para salvar todas')
    print()
    res = int(input())
    if res == 1:
        with open("assets/verde.txt", "w") as arquivo:
            for materia in verdes:
                arquivo.write(materia + "\n")
        os.system('clear')
        print("matérias salvas em assets/verde.txt")
    elif res == 2:
        with open("assets/azul.txt", "w") as arquivo:
            for materia in azuis:
                arquivo.write(materia + "\n")
        os.system('clear')
        print("matérias salvas em assets/azul.txt")
    elif res == 3:
        with open("assets/vermelho.txt", "w") as arquivo:
            for materia in vermelhas:
                arquivo.write(materia + "\n")
        os.system('clear')
        print("matérias salvas em vermelhas.txt")
    elif res == 3:
        with open("assets/verde.txt", "w") as arquivo:
            for materia in verdes:
                arquivo.write(materia + "\n")
        with open("assets/azul.txt", "w") as arquivo:
            for materia in azuis:
                arquivo.write(materia + "\n")
        with open("assets/vermelho.txt", "w") as arquivo:
            for materia in vermelhas:
                arquivo.write(materia + "\n")
        os.system('clear')
        print("todas as listas foram salvas!")

def Inserirverdes():
    print('LISTA VERDE')
    print("digite quais matérias deseja inserir: ")
    print('digite "pronto" quando tiver terminado')
    print()
    flag=True
    while flag:
        ins = input()
        if ins == "pronto":
            flag = False
            break
        else:
            if ins in verdes:
                print('ERRO:', ins, 'já está na lista das verdes')
            elif ins in azuis:
                print('ERRO:', ins, 'já está na lista das azuis')
            elif ins in vermelhas:
                print('ERRO:', ins, 'já está na lista das vermelhas')
            else:
                verdes.append(ins)
    print('deseja salvar as alterações? [s] para "sim"')
    res = input()
    if res== "s":
        with open("assets/verde.txt", "w") as arquivo:
            for materia in verdes:
                arquivo.write(materia + "\n")
        os.system('clear')
        print("matérias salvas em assets/verde.txt")

def Inserirazul():
    print('LISTA AZUL')
    print('digite quais matérias de  deseja inserir: ')
    print('digite "pronto" quando tiver terminado')
    print()
    flag=True
    while flag:
        ins = input()
        if ins == "pronto":
            flag = False
            break
        else:
            if ins in verdes:
                print('ERRO:', ins, 'já está na lista das verdes')
            elif ins in azuis:
                print('ERRO:', ins, 'já está na lista das azuis')
            elif ins in vermelhas:
                print('ERRO:', ins, 'já está na lista das vermelhas')
            else:
                azuis.append(ins)
    print('deseja salvar as alterações? [s] para "sim"')
    res = input()
    if res== "s":
        with open("assets/azul.txt", "w") as arquivo:
            for materia in azuis:
                arquivo.write(materia + "\n")
        os.system('clear')
        print("matérias salvas em assets/azul.txt")

def Inserirvermelhas():
    print('LISTA VERMELHA')
    print("digite quais matérias deseja inserir: ")
    print('digite "pronto" quando tiver terminado')
    print()
    flag=True
    while flag:
        ins = input()
        if ins == "pronto":
            flag = False
            break
        else:
            if ins in verdes:
                print('ERRO:', ins, 'já está na lista das verdes')
            elif ins in azuis:
                print('ERRO:', ins, 'já está na lista das azuis')
            elif ins in vermelhas:
                print('ERRO:', ins, 'já está na lista das vermelhas')
            else:
                vermelhas.append(ins)
    print('deseja salvar as alterações? [s] para "sim"')
    res = input()
    if res == "s":
        with open("assets/vermelho.txt", "w") as arquivo:
            for materia in vermelhas:
                arquivo.write(materia + "\n")
        os.system('clear')
        print("matérias salvas em assets/vermelho.txt")

def Removermateria():
    print("digite qual matéria deseja remover")
    print('digite "pronto" quando tiver terminado de remover')
    print()
    flag = True
    while flag:
        materia = input()
        if materia in verdes:
            verdes.remove(materia)
            print(materia, 'foi removida da lista verde')
        elif materia in vermelhas:
            vermelhas.remove(materia)
            print(materia, 'foi removida da lista vermelha')
        elif materia in azuis:
            azuis.remove(materia)
            print(materia, 'foi removida da lista azul')
        elif materia == "pronto":
            break
        else:
            print(materia, "não foi encontrada nas listas")
    with open("assets/vermelho.txt", "w") as arquivo:
        for materia in vermelhas:
            arquivo.write(materia + "\n")
    with open("assets/azul.txt", "w") as arquivo:
        for materia in azuis:
            arquivo.write(materia + "\n")
    with open("assets/verde.txt", "w") as arquivo:
        for materia in verdes:
            arquivo.write(materia + "\n")

def Pronto():
    print("preparando imagem... ")
    #colocando os pontos na imagem
    for i in range(0,6):
        for materia in m[i].keys():
            if materia in verdes:
                objeto.ellipse((semestres[m[i][materia][0]]-5, altura[m[i][materia][1]]-5, semestres[m[i][materia][0]]+5, altura[m[i][materia][1]]+5), fill="green")
    for i in range(0,6):
        for materia in m[i].keys():
            if materia in azuis:
                objeto.ellipse((semestres[m[i][materia][0]]-5, altura[m[i][materia][1]]-5, semestres[m[i][materia][0]]+5, altura[m[i][materia][1]]+5), fill="blue")
    for i in range(0,6):
        for materia in m[i].keys():
            if materia in vermelhas:
                objeto.ellipse((semestres[m[i][materia][0]]-5, altura[m[i][materia][1]]-5, semestres[m[i][materia][0]]+5, altura[m[i][materia][1]]+5), fill="red")
    #Salvar a imagem modificada
    imagem.save("./grade_pintada.jpg", quality=100)

os.system('clear')
print("bem vindo ao programa de pintar a grade de matérias!")
Menu()
F=True
#Menu principal
while F:
    user = input()
    if user == "sair" or user == "0" or user == "exit":
        os.system('clear')
        F = False

    elif user == "passei" or user == "verde" or user == "1":
        os.system('clear')
        Inserirverdes()
        os.system('clear')
        Menu()

    elif user == "atual" or user == "azul" or user == "2":
        os.system('clear')
        Inserirazul()
        os.system('clear')
        Menu()

    elif user == "emergência" or user == "vermelho" or user == "3":
        os.system('clear')
        Inserirvermelhas()
        os.system('clear')
        Menu()

    elif user == "salvar" or user == "4":
        os.system('clear')
        Gravarlista()
        Menu()
    
    elif user == "remover" or user == "5":
        os.system('clear')
        Removermateria()
        os.system('clear')
        Menu()

    elif user == "gerar" or user == "6":
        os.system('clear')
        Pronto()
        print("tudo pronto, a imagem foi gerada")
        print('encerrando programa')
        break

    elif user == "ver" or user == "7":
        os.system('clear')
        exemplo = Image.open("./grade_pintada.jpg")
        exemplo.show()
        os.system('clear')
        _ = input('pressione enter para fechar')
        exemplo.close()
        Menu()

    elif user == "help" or user == "sos":
        os.system('clear')
        print("para usar o programa, diga qual função você deseja usar")
        print('digite [0] ou "sair" para sair do programa')
        print('digite [1] ou "verde" para inserir uma nova matéria na lista verde')
        print('digite [2] ou "azul" para inserir uma nova matéria na lista verde')
        print('digite [3] ou "vermelho" para inserir uma matéria na lista vermelha')
        print('digite [4] ou "salvar" para entrar no menu de salvar as informações')
        print('digite [5] ou "remover" para remover a marcação de alguma matéria')
        print('digite [6] ou "gerar" quando tiver tudo pronto, e então o programa irá gerar a sua imagem')
        print('digite [7] ou "ver" para ver a imagem')
        print()
    else:
        os.system('clear')
        print("desculpe, não entendi o que disse")
        print("tente novamente")
        print()
        Menu()
