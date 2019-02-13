usuario = {'nome' : 'Belphegor', 'idade' : 65000, 'username' : 'bel'}


for k in usuario:
    print('{0} -> {1}'.format(k, usuario[k]))


print(usuario.keys())

print(usuario.values())


for k, v in usuario.items():
    print('{0} => {1}'.format(k, v))
