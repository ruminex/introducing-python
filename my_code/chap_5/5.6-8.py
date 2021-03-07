'''names = ['duck', 'gourd', 'spitz']
for name in names :
    cap_name = name.capitalize()
    print("%sy Mc%sface" % (cap_name,cap_name))''' #python 2 style

'''names = ['duck', 'gourd', 'spitz']
for name in names :
    cap_name = name.capitalize()
    print('{}y Mc{}face'.format(cap_name,cap_name))''' # python 3 style

names = ['duck', 'gourd', 'spitz']
for name in names :
    cap_name = name.capitalize()
    print(f'{cap_name}y Mc{cap_name}face') # python 3.6~ style