#!/usr/bin/python



for l in open('usuarios.csv'):
    nome, idade, email = l.split(',')
    print({
       "nome" : nome.strip(), 
       "email" : email.strip(),
       "idade" : int(idade.strip()) 
    })
