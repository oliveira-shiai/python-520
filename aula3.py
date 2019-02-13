#!/usr/bin/python3

#arquivo = open('zen.txt').read().upper()
arquivo = open('zen.txt')

#print(arquivo.readlines())

#i = 0
#for linha in arquivo:
#    linha = linha.strip()
#    if  i % 2 == 0:
#        print(linha)

#    i = i+1
 
for i, linha in enumerate(arquivo):
    if i % 2 == 0:
        print(linha.strip())
        
        
