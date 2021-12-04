#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 18:33:32 2021

@author: nara
"""

x = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",
     16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z",27:" ",28:"a",29:"b",30:"c",
     31:"d",32:"e",33:"f",34:"g",35:"h",36:"j",37:"i",38:"k",39:"l",40:"m",41:"n",42:"o",43:"p",44:"q",45:"r",
     46:"s",47:"t",48:"u",49:"v",50:"w",51:"x",52:"y",53:"z",54:"1",55:"2",56:"3",57:"4",58:"5",59:"6",60:"7",61:"8",62:"9",63:"0"}

x_reverse = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14,"O":15,
             "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26, " ":27, "a":28, "b":29, "c":30,
             "d":31, "e":32, "f":33, "g":34, "h":35, "j":36, "i":37, "k":38, "l":39, "m":40, "n":41, "o":42, "p":43, "q":44, "r":45,
             "s":46, "t":47, "u":48, "v":49, "w":50, "x":51, "y":52, "z":53, "1":54, "2":55, "3":56, "4":57, "5":58, "6":59, "7":60, "8":61, "9":62, "0":63}   

#text aus klartext.txt zwischenspeichern 
Klartext=""
datei = open('Klartext.txt','r')
with open('Klartext.txt','r') as infile:
    lines = [line.strip() for line in infile]
for i in lines:
    Klartext = Klartext+str(i+" ")

#anzahl Zeichen im Klartext.txt auslesen
Zeichenlaenge = len(Klartext)
print("Zeichenlaenge:", Zeichenlaenge)

#schlüssel einlesen 
key=""
i = 0
helpi = ""
xy = 0

key=""
datei = open('key.txt','r')
with open('key.txt','r') as infile:
    lines = [line.strip() for line in infile]
for i in lines:
   key = key+str(i+" ")

#verschluesseln()
def verschluesseln():
    # Text in Array umwandeln
    ArrayOfKlartext = []
    for i in Klartext:
        ArrayOfKlartext.append(i)
        
    # Schlüssel in Array umwandeln
    ArrayOfKey = []
    for i in key:
        ArrayOfKey.append(i)
    
    # Textarray in Zahlen umwandeln
    TextZahlenArray=[]
    for i in ArrayOfKlartext:
        arrrg = x_reverse[i]
        TextZahlenArray.append(arrrg)

    # Schlüsselarray in Zahlen umwandeln
    SchlüsselZahlenArray=[]
    for i in ArrayOfKey:
        arrrg = x_reverse[i]
        SchlüsselZahlenArray.append(arrrg)
        
    KeyKey = []
    a = 0 
    while a < Zeichenlaenge:
        helper = TextZahlenArray[a] + SchlüsselZahlenArray[a]
        if helper > 63:
            helper = helper - 63
        KeyKey.append(helper)
        a = a+1
        
    # verschlüsselter text
    SchlüsselterText=[]
    for i in KeyKey:
        arrrg = x[i]
        SchlüsselterText.append(arrrg)
 
    #geheimtxt in datei schreiben
    txt = ""
    datobj = open("chiffrratt.txt", "w")
    for i in SchlüsselterText:
        txt = txt+i
        datobj.write(i)
    datobj.close()
    
# Chiffrat zur Kontrolle auslesen
def kontrolle(): 
    with open("chiffrratt.txt", "r") as infile:
        chiffi = [line.strip() for line in infile]       
    Kon =""
    for i in chiffi:
        Kon = Kon+i
    print(Kon)

#chiffrat erzeugen
verschluesseln()
kontrolle()